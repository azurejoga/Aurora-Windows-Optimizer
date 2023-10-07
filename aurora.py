import wx
import webbrowser
import sys
import os

class WelcomeDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        super(WelcomeDialog, self).__init__(parent, id, title)
        
        panel = wx.Panel(self)
        
        # Texto de boas-vindas na caixa de diálogo
        welcome_text = wx.StaticText(panel, -1, "Olá, estamos felizes por você querer testar nosso programa!")
        disclaimer_text = wx.StaticText(panel, -1, "Lembre-se que todas as alterações são feitas por você mesmo e não temos quaisquer responsabilidade.")
        disclaimer_text2 = wx.StaticText(panel, -1, "Todos os riscos são assumidos por você mesmo!")
        restore_text = wx.StaticText(panel, -1, "Antes de fazer qualquer coisa, crie um ponto de restauração no seu PC para prevenir eventuais problemas.")
        
        # Botão "Ok, quero continuar" na caixa de diálogo
        ok_button = wx.Button(panel, label="Ok, quero continuar")
        ok_button.Bind(wx.EVT_BUTTON, self.on_ok)
        
        # Layout da caixa de diálogo
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(welcome_text, 0, wx.ALL, 10)
        sizer.Add(disclaimer_text, 0, wx.ALL, 10)
        sizer.Add(disclaimer_text2, 0, wx.ALL, 10)
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
        empty_list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT)
        empty_list.InsertColumn(0, "Itens", width=300)
        
        # Botões "Abrir Repositório no GitHub" e "Baixar Versão Mais Recente"
        github_button = wx.Button(panel, label="Abrir Repositório no GitHub")
        github_button.Bind(wx.EVT_BUTTON, self.open_github)
        
        download_button = wx.Button(panel, label="Baixar Versão Mais Recente")
        download_button.Bind(wx.EVT_BUTTON, self.download_latest_version)
        
        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(empty_list, 1, wx.EXPAND|wx.ALL, 10)
        sizer.Add(github_button, 0, wx.CENTER|wx.TOP|wx.BOTTOM, 10)
        sizer.Add(download_button, 0, wx.CENTER|wx.TOP|wx.BOTTOM, 10)
        
        panel.SetSizer(sizer)
    
    def open_github(self, event):
        # Abrir o navegador no link do GitHub
        webbrowser.open("https://github.com/azurejoga/Aurora-otimisador-para-windows-")
    
    def download_latest_version(self, event):
        # Abrir o navegador no link de download da versão mais recente
        webbrowser.open("https://link_para_download_da_versao_mais_recente")

app = wx.App()

# Exibir a caixa de diálogo inicial
dlg = WelcomeDialog(None, -1, "Bem-Vindo ao Aurora")
result = dlg.ShowModal()
dlg.Destroy()

if result == wx.ID_OK:
    frame = MyFrame(None, -1, "Aurora: Otimizador para Windows ™")
    frame.Show()

app.MainLoop()
