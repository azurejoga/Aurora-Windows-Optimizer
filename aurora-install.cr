# Função para executar comandos com privilégios de administrador
def run_as_admin(command : String)
  # Constrói o comando completo para ser executado com o PowerShell
  ps_command = "powershell.exe -NoProfile -ExecutionPolicy Bypass -Command \"#{command}\""

  # Executa o comando com privilégios de administrador
  system(ps_command)
end

# Comando para instalar o script Aurora no PowerShell
install_command = "Install-Script -Name aurora"

# Comando para executar o script Aurora após a instalação
execute_command = "aurora"

# Instala o script Aurora
run_as_admin(install_command)

# Aguarda um momento para garantir que a instalação seja concluída antes de executar o script
sleep 1

# Executa o script Aurora com permissões elevadas
run_as_admin(execute_command)
