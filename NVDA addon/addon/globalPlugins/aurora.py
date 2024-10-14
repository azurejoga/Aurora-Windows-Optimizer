import globalPluginHandler
import ui
import os
import subprocess
import json
import shutil  # Para mover arquivos

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_config()  # Chama a função para criar o config.json ao inicializar o complemento
        ui.message("Add-on installed successfully! Press NVDA+SHIFT+A to run Aurora and optimize your PC!")  # Mensagem de sucesso

    def create_config(self):
        """Cria um arquivo de configuração na pasta Documents/aurora e move os arquivos necessários."""
        documentsPath = os.path.join(os.path.expanduser("~"), "Documents", "aurora")
        os.makedirs(documentsPath, exist_ok=True)  # Cria a pasta se não existir

        config_path = os.path.join(documentsPath, "config.json")  # Atualiza o caminho do config.json

        # Cria o arquivo de configuração se não existir
        if not os.path.exists(config_path):
            with open(config_path, "w") as config_file:
                json.dump({"installed": True}, config_file)

            # Move os arquivos para a nova pasta
            self.move_files(documentsPath)

    def move_files(self, destination):
        """Move os arquivos necessários para a pasta de destino."""
        addonDir = os.path.dirname(__file__)  # Obtém o caminho do complemento
        files_to_move = ["Aurora.exe", "commands", "version", "update.exe"]

        for file_name in files_to_move:
            src = os.path.join(addonDir, file_name)  # Caminho original do arquivo
            dst = os.path.join(destination, file_name)  # Caminho de destino

            if os.path.exists(src):  # Verifica se o arquivo existe
                try:
                    shutil.move(src, dst)  # Move o arquivo
                    ui.message(f"Moved {file_name} to {destination}.")
                except Exception as e:
                    ui.message(f"Error moving {file_name}: {str(e)}")

    def script_runAurora(self, gesture):
        # Mensagem de status no NVDA
        ui.message("Attempting to run Aurora Windows Optimizer!")

        # Caminho do executável na pasta Documents/aurora
        documentsPath = os.path.join(os.path.expanduser("~"), "Documents", "aurora")
        exePath = os.path.join(documentsPath, "Aurora.exe")

        # Verifica se o arquivo existe
        if os.path.exists(exePath):
            try:
                # Comando para executar o Aurora usando PowerShell com o parâmetro WD
                command = f"Start-Process -FilePath '{exePath}' -WorkingDirectory '{documentsPath}'"
                subprocess.Popen(["powershell", "-Command", command], shell=True)
                ui.message("Aurora Windows Optimizer is running!")
            except Exception as e:
                ui.message(f"Error when executing Aurora: {str(e)}")
        else:
            ui.message(f"Executable not found: {exePath}")

    # Atalho para o NVDA
    __gestures = {
        "kb:NVDA+SHIFT+A": "runAurora"
    }
