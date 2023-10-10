import wx
import subprocess
import pickle
import webbrowser

class WelcomeDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        super(WelcomeDialog, self).__init__(parent, id, title)
        
        panel = wx.Panel(self)
        
        # Texto de boas-vindas na caixa de diálogo
        welcome_text = wx.StaticText(panel, -1, "Olá, estamos felizes por você querer testar nosso programa!")
        disclaimer_text = wx.StaticText(panel, -1, "Lembre-se que todas as alterações são feitas por você e não somos responsáveis ​​por quaisquer problemas.")
        restore_text = wx.StaticText(panel, -1, "Antes de fazer qualquer coisa, crie um ponto de restauração no seu PC para evitar eventuais problemas.")
        
        # Botão "Ok, quero continuar" na caixa de diálogo
        ok_button = wx.Button(panel, label="Ok, quero continuar")
        ok_button.Bind(wx.EVT_BUTTON, self.on_ok)
        
        # Layout da caixa de diálogo
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(welcome_text, 0, wx.ALL, 10)
        sizer.Add(disclaimer_text, 0, wx.ALL, 10)
        sizer.Add(restore_text, 0, wx.ALL, 10)
        sizer.Add(ok_button, 0, wx.CENTER|wx.ALL, 10)
        
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
        self.lista_de_comandos.InsertColumn(1, "Descrição", width=150)
        self.lista_de_comandos.InsertColumn(2, "Comando", width=200)
        self.lista_de_comandos.InsertColumn(3, "Tipo", width=100)
        
        # Criar o menu "Adicionar Comandos"
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        add_command_item = file_menu.Append(wx.ID_ANY, "Adicionar Comandos", "Adicionar um novo comando")
        self.Bind(wx.EVT_MENU, self.on_add_command, add_command_item)
        menu_bar.Append(file_menu, "Comandos")
        
        # Criar o menu "Ferramentas" e adicionar itens
        tools_menu = wx.Menu()
        open_github_repo_item = tools_menu.Append(wx.ID_ANY, "Abrir Repositório no GitHub", "Abrir o repositório no GitHub")
        download_latest_github_item = tools_menu.Append(wx.ID_ANY, "Baixar Versão Mais Recente do GitHub", "Baixar a versão mais recente do GitHub")
        self.Bind(wx.EVT_MENU, self.open_github_repo, open_github_repo_item)
        self.Bind(wx.EVT_MENU, self.download_latest_github, download_latest_github_item)
        menu_bar.Append(tools_menu, "Ferramentas")

        self.SetMenuBar(menu_bar)
        
        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lista_de_comandos, 1, wx.EXPAND|wx.ALL, 10)
        
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
        dlg = AddCommandDialog(self, -1, "Adicionar Comandos")
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
        download_url = "https://github.com/seu-usuario/seu-repositorio/releases/latest"
        webbrowser.open(download_url)

    def create_context_menu(self):
        menu = wx.Menu()

        edit_item = wx.MenuItem(menu, wx.ID_ANY, "Editar")
        self.Bind(wx.EVT_MENU, self.on_edit_command, edit_item)
        menu.Append(edit_item)

        remove_item = wx.MenuItem(menu, wx.ID_ANY, "Remover Comando")
        self.Bind(wx.EVT_MENU, self.on_remove_command, remove_item)
        menu.Append(remove_item)

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
            dlg = AddCommandDialog(self, -1, "Editar Comando")
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
            # Confirme se o usuário deseja remover o comando
            confirm_dialog = wx.MessageDialog(self, "Tem certeza de que deseja remover este comando?", "Remover Comando", wx.YES_NO | wx.ICON_QUESTION)
            result = confirm_dialog.ShowModal()
            confirm_dialog.Destroy()

            if result == wx.ID_YES:
                # Remova o item da lista
                self.lista_de_comandos.DeleteItem(selected_item)
                # Remova o comando da lista de comandos
                del self.commands[selected_item]
                # Salve as alterações no arquivo
                save_commands(self.commands)

class AddCommandDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        super(AddCommandDialog, self).__init__(parent, id, title)
        
        panel = wx.Panel(self)
        
        # Adicione os elementos para entrada de nome, descrição, comando e tipo de comando
        name_label = wx.StaticText(panel, -1, "Nome:")
        self.name_text = wx.TextCtrl(panel, -1, "")
        
        desc_label = wx.StaticText(panel, -1, "Descrição:")
        self.desc_text = wx.TextCtrl(panel, -1, "")
        
        cmd_label = wx.StaticText(panel, -1, "Comando:")
        self.cmd_text = wx.TextCtrl(panel, -1, "")
        
        type_label = wx.StaticText(panel, -1, "Tipo de Comando:")
        self.type_combo = wx.ComboBox(panel, -1, choices=["CMD", "Powershell"], style=wx.CB_READONLY)
        
        # Botões "Ok" e "Cancelar"
        ok_button = wx.Button(panel, label="Ok")
        ok_button.Bind(wx.EVT_BUTTON, self.on_ok)
        
        cancel_button = wx.Button(panel, label="Cancelar")
        cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)
        
        # Layout da caixa de diálogo
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(name_label, 0, wx.ALL, 10)
        sizer.Add(self.name_text, 0, wx.EXPAND|wx.ALL, 10)
        sizer.Add(desc_label, 0, wx.ALL, 10)
        sizer.Add(self.desc_text, 0, wx.EXPAND|wx.ALL, 10)
        sizer.Add(cmd_label, 0, wx.ALL, 10)
        sizer.Add(self.cmd_text, 0, wx.EXPAND|wx.ALL, 10)
        sizer.Add(type_label, 0, wx.ALL, 10)
        sizer.Add(self.type_combo, 0, wx.EXPAND|wx.ALL, 10)
        sizer.Add(ok_button, 0, wx.CENTER|wx.ALL, 10)
        sizer.Add(cancel_button, 0, wx.CENTER|wx.ALL, 10)
        
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
        output_text = wx.TextCtrl(panel, -1, value=output, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL|wx.VSCROLL)
        
        # Botão "Fechar"
        close_button = wx.Button(panel, label="Fechar")
        close_button.Bind(wx.EVT_BUTTON, self.on_close)
        
        # Layout da caixa de diálogo
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(output_text, 1, wx.EXPAND|wx.ALL, 10)
        sizer.Add(close_button, 0, wx.CENTER|wx.ALL, 10)
        
        panel.SetSizer(sizer)
    
    def on_close(self, event):
        self.EndModal(wx.ID_OK)

def save_commands(commands):
    try:
        with open("commands", "wb") as file:
            pickle.dump(commands, file)
    except Exception as e:
        print("Erro ao salvar comandos:", e)

def load_commands():
    try:
        with open("commands", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        print("Erro ao carregar comandos:", e)
        return []

app = wx.App()

# Exibir a caixa de diálogo inicial
dlg = WelcomeDialog(None, -1, "Bem-Vindo ao Aurora")
result = dlg.ShowModal()
dlg.Destroy()

if result == wx.ID_OK:
    frame = MyFrame(None, -1, "Aurora: Otimizador para Windows ™")
    frame.Show()

app.MainLoop()
