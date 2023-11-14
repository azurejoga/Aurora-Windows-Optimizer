#!/usr/bin/python
# -*- coding: <encoding name> -*-
# Importe as bibliotecas necessárias (wx, subprocess, pickle, webbrowser, ctypes)
import wx
import subprocess
import pickle
import webbrowser
import ctypes
import languageHandler
# Constantes da API do Windows para criar um ponto de restauração
languageHandler.setLanguage("system")
SMGR_CREATE = 0x100
SMGR_CONFIRM = 0x200
SMGR_AUTO = 0x400
SMGR_NOCHANGE = 0x800
SMGR_NORESTORE = 0x1000
SMGR_NOTSUPPORTED = 0x2000
SMGR_LOCK = 0x4000
SMGR_UNLOCK = 0x8000
SMGR_NOSMPAGEFILE = 0x10000

class WelcomeDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        super(WelcomeDialog, self).__init__(parent, id, title)

        panel = wx.Panel(self)

        # Texto de boas-vindas na caixa de diálogo
        welcome_text = wx.StaticText(panel, -1, _("Olá, estamos felizes por você querer testar nosso programa!"))
        disclaimer_text = wx.StaticText(panel, -1, _("Lembre-se que todas as alterações são feitas por você e não somos responsáveis por quaisquer problemas."))
        restore_text = wx.StaticText(panel, -1, _("Antes de fazer qualquer coisa, crie um ponto de restauração no seu PC para evitar eventuais problemas."))

        # Botão "Ok, quero continuar" na caixa de diálogo
        ok_button = wx.Button(panel, label=_("Ok, quero continuar"))
        ok_button.Bind(wx.EVT_BUTTON, self.on_ok)

        # Layout da caixa de diálogo
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(welcome_text, 0, wx.ALL, 10)
        sizer.Add(disclaimer_text, 0, wx.ALL, 10)
        sizer.Add(restore_text, 0, wx.ALL, 10)
        sizer.Add(ok_button, 0, wx.CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        super(MyFrame, self).__init__(parent, id, title, size=(400, 300))

        panel = wx.Panel(self)

        # Lista vazia
        self.lista_de_comandos = wx.ListCtrl(panel, -1, style=wx.LC_REPORT)
        self.lista_de_comandos.InsertColumn(0, "Nome", width=100)
        self.lista_de_comandos.InsertColumn(1, _("Descrição"), width=150)
        self.lista_de_comandos.InsertColumn(2, _("Comando"), width=200)
        self.lista_de_comandos.InsertColumn(3, _("Tipo"), width=100)

        # Criar o menu "Adicionar Comandos"
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        add_command_item = file_menu.Append(wx.ID_ANY, _("Adicionar Comandos"), _("Adicionar um novo comando"))
        self.Bind(wx.EVT_MENU, self.on_add_command, add_command_item)
        menu_bar.Append(file_menu, _("Comandos"))

        # Criar o menu "Ferramentas" e adicionar itens
        tools_menu = wx.Menu()
        open_github_repo_item = tools_menu.Append(wx.ID_ANY, _("Abrir Repositório no GitHub"), _("Abrir o repositório no GitHub"))
        download_latest_github_item = tools_menu.Append(wx.ID_ANY, _("Baixar Versão Mais Recente do GitHub"), _("Baixar a versão mais recente do GitHub"))
        create_restore_point_item = tools_menu.Append(wx.ID_ANY, _("Criar Ponto de Restauração"), _("Criar um ponto de restauração no sistema"))
        sort_commands_item = tools_menu.Append(wx.ID_ANY, _("Ordenar Comandos"), _("Ordenar os comandos em ordem alfabética"))
        check_updates_item = tools_menu.Append(wx.ID_ANY, _("Verificar Atualizações"), _("Verificar atualizações e fechar Aurora"))
        self.Bind(wx.EVT_MENU, self.open_github_repo, open_github_repo_item)
        self.Bind(wx.EVT_MENU, self.download_latest_github, download_latest_github_item)
        self.Bind(wx.EVT_MENU, self.create_system_restore_point, create_restore_point_item)
        self.Bind(wx.EVT_MENU, self.sort_commands, sort_commands_item)
        self.Bind(wx.EVT_MENU, self.check_updates, check_updates_item)
        menu_bar.Append(tools_menu, _("Ferramentas"))
        self.SetMenuBar(menu_bar)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lista_de_comandos, 1, wx.EXPAND | wx.ALL, 10)
        panel.SetSizer(sizer)

        # Bind para a tecla Enter ou Espaço na lista de comandos
        self.lista_de_comandos.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_execute_command)

        # Vincule o evento EVT_CONTEXT_MENU
        self.lista_de_comandos.Bind(wx.EVT_CONTEXT_MENU, self.on_context_menu)

        # Carregue os comandos do arquivo
        self.commands = load_commands()

        # Preencha a lista de comandos
        for command in self.commands:
            self.add_command_to_list(command)

    def on_execute_command(self, event):
        # Obtenha o comando selecionado na lista
        selected_item = self.lista_de_comandos.GetFirstSelected()
        if selected_item >= 0:
            cmd = self.lista_de_comandos.GetItemText(selected_item, col=2)
            type = self.lista_de_comandos.GetItemText(selected_item, col=3)
            # Executar o comando
            self.run_command(cmd, type)

    def on_add_command(self, event):
        # Abrir a caixa de diálogo para adicionar comandos
        dlg = AddCommandDialog(self, -1, _("Adicionar Comandos"))
        result = dlg.ShowModal()
        if result == wx.ID_OK:
            name = dlg.name_text.GetValue()
            desc = dlg.desc_text.GetValue()
            cmd = dlg.cmd_text.GetValue()
            type = dlg.type_combo.GetValue()

            # Adicionar o comando à lista
            command = {"name": name, "desc": desc, "cmd": cmd, "type": type}
            self.commands.append(command)
            self.add_command_to_list(command)
            # Salvar os comandos no arquivo
            save_commands(self.commands)

        dlg.Destroy()

    def add_command_to_list(self, command):
        index = self.lista_de_comandos.InsertItem(self.lista_de_comandos.GetItemCount(), command["name"])
        self.lista_de_comandos.SetItem(index, 1, command["desc"])
        self.lista_de_comandos.SetItem(index, 2, command["cmd"])
        self.lista_de_comandos.SetItem(index, 3, command["type"])

    def run_command(self, command, type):
        try:
            if "CMD" in type.upper():
                # Executa o comando CMD e captura a saída
                result = subprocess.run(["cmd", "/c", command], shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            elif "POWERSHELL" in type.upper():
                # Executa o comando PowerShell e captura a saída
                result = subprocess.run(["powershell", "-Command", command], shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            else:
                print("Tipo de comando não suportado:", type)
                return

            # Exibir a saída em uma caixa de diálogo
            output_dialog = OutputDialog(self, -1, "Resultado do Comando", result.stdout)
            output_dialog.ShowModal()

        except subprocess.CalledProcessError as e:
            # Se ocorrer um erro na execução do comando, exibir a saída de erro em uma caixa de diálogo
            output_dialog = OutputDialog(self, -1, "Erro ao Executar Comando", e.stderr)
            output_dialog.ShowModal()
        except Exception as e:
            print("Erro ao executar comando:", e)

    def open_github_repo(self, event):
        # URL do repositório no GitHub
        github_url = "https://github.com/azurejoga/Aurora-otimisador-para-windows-/"
        webbrowser.open(github_url)

    def download_latest_github(self, event):
        # URL para baixar a versão mais recente do GitHub
        download_url = "https://github.com/azurejoga/Aurora-Windows-Optimizer/releases/"
        webbrowser.open(download_url)

    def create_system_restore_point(self, event):
        # Abrir uma caixa de diálogo para inserir a descrição do ponto de restauração
        description = wx.GetTextFromUser(_("Insira uma descrição para o ponto de restauração:"), _("Criar Ponto de Restauração"))
        if description:
            create_system_restore_point(description)

    def sort_commands(self, event):
        # Ordenar os comandos em ordem alfabética
        self.lista_de_comandos.DeleteAllItems()
        self.commands.sort(key=lambda x: x["name"])
        for command in self.commands:
            self.add_command_to_list(command)

    def create_context_menu(self):
        menu = wx.Menu()

        edit_item = wx.MenuItem(menu, wx.ID_ANY, _("Editar"))
        self.Bind(wx.EVT_MENU, self.on_edit_command, edit_item)
        menu.Append(edit_item)

        remove_item = wx.MenuItem(menu, wx.ID_ANY, _("Remover Comando"))
        self.Bind(wx.EVT_MENU, self.on_remove_command, remove_item)
        menu.Append(remove_item)

        move_to_top_item = wx.MenuItem(menu, wx.ID_ANY, _("Mover para o Topo"))
        self.Bind(wx.EVT_MENU, self.move_command_to_top, move_to_top_item)
        menu.Append(move_to_top_item)

        move_to_bottom_item = wx.MenuItem(menu, wx.ID_ANY, _("Mover para o Final"))
        self.Bind(wx.EVT_MENU, self.move_command_to_bottom, move_to_bottom_item)
        menu.Append(move_to_bottom_item)

        return menu

    def on_context_menu(self, event):
        selected_item = self.lista_de_comandos.GetFirstSelected()
        if selected_item >= 0:
            menu = self.create_context_menu()
            self.PopupMenu(menu)
            menu.Destroy()

    def on_edit_command(self, event):
        selected_item = self.lista_de_comandos.GetFirstSelected()
        if selected_item >= 0:
            # Obtenha os detalhes do comando selecionado
            name = self.lista_de_comandos.GetItemText(selected_item, col=0)
            desc = self.lista_de_comandos.GetItemText(selected_item, col=1)
            cmd = self.lista_de_comandos.GetItemText(selected_item, col=2)
            type = self.lista_de_comandos.GetItemText(selected_item, col=3)

            # Use a mesma caixa de diálogo para edição
            dlg = AddCommandDialog(self, -1, _("Editar Comando"))
            dlg.name_text.SetValue(name)
            dlg.desc_text.SetValue(desc)
            dlg.cmd_text.SetValue(cmd)
            dlg.type_combo.SetValue(type)

            result = dlg.ShowModal()
            if result == wx.ID_OK:
                # Atualize os detalhes do comando na lista
                updated_name = dlg.name_text.GetValue()
                updated_desc = dlg.desc_text.GetValue()
                updated_cmd = dlg.cmd_text.GetValue()
                updated_type = dlg.type_combo.GetValue()

                self.lista_de_comandos.SetItem(selected_item, 0, updated_name)
                self.lista_de_comandos.SetItem(selected_item, 1, updated_desc)
                self.lista_de_comandos.SetItem(selected_item, 2, updated_cmd)
                self.lista_de_comandos.SetItem(selected_item, 3, updated_type)

                # Atualize os detalhes do comando na lista de comandos
                self.commands[selected_item]["name"] = updated_name
                self.commands[selected_item]["desc"] = updated_desc
                self.commands[selected_item]["cmd"] = updated_cmd
                self.commands[selected_item]["type"] = updated_type

                # Salve as alterações no arquivo
                save_commands(self.commands)

            dlg.Destroy()

    def on_remove_command(self, event):
        selected_item = self.lista_de_comandos.GetFirstSelected()
        if selected_item >= 0:
            # Remova o comando da lista e da exibição
            del self.commands[selected_item]
            self.lista_de_comandos.DeleteItem(selected_item)
            # Salve as alterações no arquivo
            save_commands(self.commands)

    def check_updates(self, event):
        subprocess.run(["update.exe"], shell=True)


 
    def move_command_to_top(self, event):
        selected_item = self.lista_de_comandos.GetFirstSelected()
        if selected_item > 0:
            # Mova o comando para o topo da lista
            self.commands.insert(0, self.commands.pop(selected_item))
            self.lista_de_comandos.DeleteAllItems()
            for command in self.commands:
                self.add_command_to_list(command)
            self.lista_de_comandos.Select(0)

    def move_command_to_bottom(self, event):
        selected_item = self.lista_de_comandos.GetFirstSelected()
        if selected_item >= 0 and selected_item < len(self.commands) - 1:
            # Mova o comando para o final da lista
            self.commands.append(self.commands.pop(selected_item))
            self.lista_de_comandos.DeleteAllItems()
            for command in self.commands:
                self.add_command_to_list(command)
            self.lista_de_comandos.Select(len(self.commands) - 1)

class AddCommandDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        super(AddCommandDialog, self).__init__(parent, id, title)

        panel = wx.Panel(self)

        # Adicione os elementos para entrada de nome, descrição, comando e tipo de comando
        name_label = wx.StaticText(panel, -1, _("Nome:"))
        self.name_text = wx.TextCtrl(panel, -1, "")

        desc_label = wx.StaticText(panel, -1, _("Descrição:"))
        self.desc_text = wx.TextCtrl(panel, -1, "")

        cmd_label = wx.StaticText(panel, -1, _("Comando:"))
        self.cmd_text = wx.TextCtrl(panel, -1, "", style=wx.TE_MULTILINE)  # Permite várias linhas

        type_label = wx.StaticText(panel, -1, _("Tipo de Comando:"))
        self.type_combo = wx.ComboBox(panel, -1, choices=["CMD", "Powershell"], style=wx.CB_READONLY)

        # Botões "Ok" e "Cancelar"
        ok_button = wx.Button(panel, label=_("Ok"))
        ok_button.Bind(wx.EVT_BUTTON, self.on_ok)

        cancel_button = wx.Button(panel, label=_("Cancelar"))
        cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)

        # Layout da caixa de diálogo
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(name_label, 0, wx.ALL, 10)
        sizer.Add(self.name_text, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(desc_label, 0, wx.ALL, 10)
        sizer.Add(self.desc_text, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(cmd_label, 0, wx.ALL, 10)
        sizer.Add(self.cmd_text, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(type_label, 0, wx.ALL, 10)
        sizer.Add(self.type_combo, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(ok_button, 0, wx.CENTER | wx.ALL, 10)
        sizer.Add(cancel_button, 0, wx.CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)

class OutputDialog(wx.Dialog):
    def __init__(self, parent, id, title, output):
        super(OutputDialog, self).__init__(parent, id, title, size=(400, 300))

        panel = wx.Panel(self)

        # Texto de saída do comando
        if output:
            output_text = wx.TextCtrl(panel, -1, value=output.strip(), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.VSCROLL)
        else:
            output_text = wx.TextCtrl(panel, -1, value=_('O comando foi executado com sucesso!'), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.VSCROLL)

        # Botão "Fechar"
        close_button = wx.Button(panel, label=_("Fechar"))
        close_button.Bind(wx.EVT_BUTTON, self.on_close)

        # Layout da caixa de diálogo
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(output_text, 1, wx.EXPAND | wx.ALL, 10)
        sizer.Add(close_button, 0, wx.CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)

    def on_close(self, event):
        self.EndModal(wx.ID_OK)

def save_commands(commands):
    try:
        with open("commands"+languageHandler.curLang[:2], "wb") as file:
            pickle.dump(commands, file)
    except Exception as e:
        print("Erro ao salvar comandos:", e)

def load_commands():
    try:
        with open("commands-"+languageHandler.curLang[:2], "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        print("Erro ao carregar comandos:", e)
        return []

def create_system_restore_point(description):
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "powershell.exe", "Checkpoint-Computer -Description '{}'".format(description), "", 1)
        wx.MessageBox(_("Ponto de restauração criado com sucesso!"), _("Ponto de Restauração"), wx.OK | wx.ICON_INFORMATION)
    except Exception as e:
        wx.MessageBox(_("Erro ao criar o ponto de restauração:\n") + str(e), _("Erro de Ponto de Restauração"), wx.OK | wx.ICON_ERROR)

app = wx.App()

# Exibir a caixa de diálogo inicial
dlg = WelcomeDialog(None, -1, _("Bem-Vindo ao Aurora"))
result = dlg.ShowModal()
dlg.Destroy()

if result == wx.ID_OK:
    frame = MyFrame(None, -1, _("Aurora: Otimizador para Windows ™"))
    frame.Show()

app.MainLoop()
