import wx
import requests
import os
import subprocess

class AtualizadorApp(wx.App):
    def OnInit(self):
        self.VerificarAtualizacao()
        return True

    def VerificarAtualizacao(self):
        versao_atual = self.ObterVersaoAtual()
        ultima_versao_github = self.ObterUltimaVersaoGitHub()

        if versao_atual < ultima_versao_github:
            self.MostrarDialogAtualizacao(ultima_versao_github)
        else:
            self.MostrarDialogAppAtualizado()

    def ObterVersaoAtual(self):
        try:
            with open("version", "r") as file:
                return file.read().strip()
        except FileNotFoundError:
            return "aurora0"

    def ObterUltimaVersaoGitHub(self):
        url = "https://api.github.com/repos/azurejoga/Aurora-Windows-Optimizer/releases/latest"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("tag_name", "aurora0")
        return "aurora0"

    def MostrarDialogAtualizacao(self, ultima_versao_github):
        dlg = wx.MessageDialog(None, f"New version available: {ultima_versao_github}\nDo you want to update?", "Update Available", wx.YES_NO | wx.ICON_INFORMATION)
        result = dlg.ShowModal()
        dlg.Destroy()

        if result == wx.ID_YES:
            self.AtualizarApp(ultima_versao_github)

    def MostrarDialogAppAtualizado(self):
        dlg = wx.MessageDialog(None, "the APP is already updated", "Update Complete", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def AtualizarApp(self, ultima_versao_github):
        install_url = f"https://github.com/azurejoga/Aurora-Windows-Optimizer/releases/download/{ultima_versao_github}/aurora-install.exe"
        install_file = "aurora-install.exe"

        response = requests.get(install_url)
        if response.status_code == 200:
            with open(install_file, "wb") as file:
                file.write(response.content)
            subprocess.run([install_file])
        else:
            dlg = wx.MessageDialog(None, "Failed to download the installer.", "Update Error", wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()

if __name__ == '__main__':
    app = AtualizadorApp(False)
    app.MainLoop()
