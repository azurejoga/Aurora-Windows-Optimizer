## aurora, windows optimizer v16.0
30/03/2024 18:49
# english
# new features
* the possibility of completely disabling Windows Defender has been re-added
* Added the ability to uninstall or reinstall Microsoft Edge and Microsoft Edge WebView
* added the possibility to enable the classic volume panel of windows 10
* the possibility of downloading malwarebytes, the best antivirus on the market, has been added
* 2 new installation methods have been added! to find out which ones, see [](https://github.com/azurejoga/Aurora-Windows-Optimizer/blob/aurora/installation.md)

# português / portuguese
# novas funcionalidades
* foi readicionado a possibilidade de desativar completamente o windows defender
* foi adicionado a possibilidade de desinstalar ou reinstalar o microsoft edge, e o microsoft edge webview
* foi adicionado a possibilidade de habilitar o painel de volume clássico do windows 10
* foi adicionado a possibilidade de baixar o malwarebytes, o melhor ante-vírus do mercado
* foi adicionado 2 novos métodos de instalação! para saber quais, consulte  [](https://github.com/azurejoga/Aurora-Windows-Optimizer/blob/aurora/instalation.md)

## aurora, windows optimizer v15.0
17/03/2024 17:00

# english
# code
1. added [vcruntime140.dll](https://www.file.net/process/vcruntime140.dll.html) and
2. vcruntime140_1.dll https://www.easeus.com/knowledge-center/what-is -vcruntime140-dll.html
 so that the user does not need to install all the VC runtime ++ packages necessary to run the aurora code.

* now aurora supports notifications, more information in the file [aurora.py](https://github.com/azurejoga/Aurora-Windows-Optimizer/blob/aurora/aurora.py)

* removed the welcome message on the second run of the program onwards.

## new functions
* added the possibility of completely disabling windows update, to protest Microsoft's obligation to try to force windows 11, according to the update
1. KB5001716 https://www.neowin.net/news/microsoft-quietly-installing -kb5001716-so-you-can-update-to-windows-11-or-newer-windows-10/
2.  and according to this https://www.techradar.com/news/not-upgraded- to-windows-10-22h2-yet-youll-soon-be-forced-to-or-switch-to-windows-11
3.  plus this https://www.tomshardware.com/software/microsoft-begins -forced-updates-to-windows-11-23h2-targets-pcs-running-21h2-and-22h2 article.

 If you don't want the latest Windows updates, disable Windows Update completely in Aurora.

* you can now receive notifications when you run a command, this means if you go to grab a coffee when you get back to your pc because you left it AFK/away, it will now look like a notification on your screen saying the command has been run or you hear a error...
* the welcome message will now only appear on the first run. This means if you see an extra file in your aurora folder, don't worry...
* Restore the changes you made to your PC! Exactly, a long-awaited feature has arrived! You can now undo the changes made by Aurora on your PC!
# important.
If you created a restore point previously, it will appear in Aurora when you click to restore.
Also, if you have never created a restore point, create it within aurora before using the scripts/commands.
Another thing, if you created a point but it doesn't appear when you click to restore, close and open aurora again.

# português / portuguese.
# código
* adicionado [vcruntime140.dll](https://www.file.net/process/vcruntime140.dll.html) e vcruntime140_1.dll https://www.easeus.com/knowledge-center/what-is -vcruntime140-dll.html para que o usuário não precise instalar todos os pacotes VC runtime ++ necessários para executar o código aurora.
* agora o aurora suporta notificações, mais informações no arquivo [aurora.py](https://github.com/azurejoga/Aurora-Windows-Optimizer/blob/aurora/aurora.py)
* removeu a mensagem de boas-vindas a partir da segunda execução do programa.

## novas funções
*adicionou a possibilidade de desativar completamente o Windows Update, para protestar contra a obrigação da Microsoft de tentar forçar o Windows 11, de acordo com a atualização  KB5001716 https://www.neowin.net/news/microsoft-quietly-installing -kb5001716-so -you-can-update-to-windows-11-or-newer-windows-10/
 e de acordo com isto https://www.techradar.com/news/not-upgraded- to-windows-10-22h2-yet-youll-soon-be-forced-to-or-switch-to-windows-11
 mais este https://www.tomshardware.com/software/microsoft-begins -forced-updates- to-windows-11-23h2-targets-pcs-running-21h2-and-22h2
 Se você não quiser as atualizações mais recentes do Windows, desative completamente o Windows Update no Aurora.

* agora você pode receber notificações ao executar um comando, isso significa que se você for tomar um café quando voltar ao seu pc porque o deixou AFK/away, agora aparecerá uma notificação na tela informando que o comando foi foi executado ou ouve um erro...

* a mensagem de boas-vindas agora aparecerá apenas na primeira execução. Isso significa que se você vir um arquivo extra na pasta aurora, não se preocupe...

* Restaure as alterações feitas no seu PC! Exatamente, chegou um recurso tão esperado! Agora você pode desfazer as alterações feitas pelo Aurora no seu PC!

# importante.
Se você criou um ponto de restauração anteriormente, ele aparecerá no Aurora quando você clicar para restaurar.
Além disso, se você nunca criou um ponto de restauração, crie-o no aurora antes de usar os scripts/comandos.
Outra coisa, se você criou um ponto mas ele não aparece quando você clica para restaurar, feche e abra o aurora novamente.

## Aurora, windows optimizer v14.0
12/02/2024 15:25

# English
# Bugs fixed.
1. Now, when you click a command in aurora, aurora will not crash.
The program stopped responding when a command was clicked.
 Previously, aurora would crash because treading was not being used to run a process or tasks in the background. then, import treading and its functions were added, see

[aurora.py for more information](https://github.com/azurejoga/Aurora-Windows-Optimizer/blob/aurora/aurora.py)

2. A critical bug has been fixed.
A bug that you couldn't run aurora if you didn't have the VC++ libraries, runtimes installed.
Now, you can go into the aurora folder, and run the install-vc-packages.ps1 script to install all VC++ runtime packages from 2003 to 2022 and then this bug has been fixed.

# New features in the application.
* Now you can install chocolatey through aurora, enjoy!

[Download the new update](https://github.com/azurejoga/Aurora-Windows-Optimizer/releases/tag/aurora14)

# português / portuguese

# Bugs corrigidos
1. Agora, quando você clica em um comando no aurora, o aurora não trava.
O programa parou de responder quando um comando foi clicado.
 Anteriormente, o aurora travava porque o treading  não estava sendo usada para executar um processo ou tarefas em segundo plano. em seguida, foram adicionadas o treading  de importação e suas funções, veja

[aurora.py para obter mais informações](https://github.com/azurejoga/Aurora-Windows-Optimizer/blob/aurora/aurora.py)

2. Um bug crítico foi corrigido.
Um bug que dizia que você não poderia executar o aurora se não tivesse as bibliotecas VC++ e os tempos de execução instalados.
Agora, você pode ir para a pasta aurora e executar o script install-vc-packages.ps1 para instalar todos os pacotes de tempo de execução VC++ de 2003 a 2022 e.
 então, esse bug foi corrigido.

# Novos recursos no aplicativo.
* Agora você pode instalar o chocolatey através do aurora, divirta-se!

[Baixe a nova atualização](https://github.com/azurejoga/Aurora-Windows-Optimizer/releases/tag/aurora14)

## Aurora, windows optimizer v13.0
02/05/2024 10:11
# english

# code changes


* Now update is a folder compiled in cx_freeze and not a onefile


* check updates has been changed with new functions.


# new things added


* added the possibility of downloading lenovo vantage, where you can change the FN key or multimedia keys. explanation in the aurora program itself, download the new update.

* added java JDK 17 and java JDK 21 to download.

* Added the possibility to re-enable the dictation or/online speech features, there are 2 methods for users to use.
1. Windows registry, will open a registry for you to accept the new changes
2. powershell method, this method is carried out using the powershell command


PS: Both methods need to restart the computer.


* Added Pot Player, a video, music player, accessible for the visually impaired.
* added steam client download most updated version

* Aurora Windows Optimizer can be installed via the Chocolatey package, see
[installation methods in readme.md](https://github.com/azurejoga/Aurora-Windows-Optimizer)
download the new installation
[here](https://github.com/azurejoga/Aurora-Windows-Optimizer/releases/tag/aurora13)


# português / portuguese.


# mudanças no código


* Agora, update é uma pasta compilada em cx_freeze e não um onefile


* check updates foi mudado com novas funções.


# novas coisas adicionadas


* adicionado a possibilidade de baixar o lenovo vantage, onde pode mudar as teclas FN key ou teclas multimedia. explicação no próprio programa aurora, baixe a nova atualização.
* adicionado java JDK 17 e java JDK 21 para baixar.
* adicionado a possibilidade de reabilitar o ditado ou / recursos de fala online, existem 2 métodos para os usuários usarem.
1. registro do windows, abrirá um registro para você aceitar as novas alterações
2. método powershell, esse método realiza-se por meio do comando powershell


PS: os 2 métodos precisam  reiniciar o computador.


* adicionado pot player, um player de vídeo, música, acessível para deficientes visuais.
* adicionado download do steam client versão mais atualizada
* aurora windows optimizer pode ser instalado por meio do pacote chocolatey, consulte
[métodos de instalação no readme.md](https://github.com/azurejoga/Aurora-Windows-Optimizer)
baixe a nova instalação
[aqui](https://github.com/azurejoga/Aurora-Windows-Optimizer/releases/tag/aurora13)


### Aurora, windows optimizer. v12.0
01/17/2024 14:55
# english
added new script with more than 50 commands for windows11 and 10! see the list below!
[Taken from optimizer script en github](https://github.com/hellzerg/optimizer)
Remember, this is not the full list of features, so you can see all the features added in this version. Please download and find out!
* Full multilingual support (24 languages ​​available)
* Improve system and network performance
* Disable unnecessary Windows services
* Disable Windows telemetry, Cortana and more
* Disable Office Telemetry (works with Office 2016 or newer)
* Stop Windows 10/11 automatic updates
* Download various useful apps quickly
* Disable CoPilot AI in Windows 11
* Uninstall UWP apps
* Clean system drive and browser profiles
* Fix common registry issues
* Ping IPs and evaluate latency
* Search IPs on SHODAN.io
* Quickly change DNS server (from a predefined list)
* Flush DNS cache
* Remove unwanted startup programs
* Edit your HOSTS file
* Identify and terminate file lock handles
* Hardware inspection tool
* Add items to the desktop right-click menu
* Define custom commands for the run dialog
* Supports silent runs using a template file

# Português / portuguese
adicionado novo script com mais de 50 comandos para windows11 e 10! veja a lista abaixo!
[Retirado de, optimizer script no github](https://github.com/hellzerg/optimizer)
Lembre-se, esta não é a lista completa de recursos. para  você poder ver todos os recursos adicionados nesta versão. Faça o download e descubra!
* Suporte multilíngue completo (24 idiomas disponíveis)
* Melhore o desempenho do sistema e da rede
* Desative serviços desnecessários do Windows
* Desative a telemetria do Windows, Cortana e muito mais
* Desative a telemetria do Office (funciona com o Office 2016 ou mais recente)
* Pare as atualizações automáticas do Windows 10/11
* Baixe vários aplicativos úteis rapidamente
* Desative o CoPilot AI no Windows 11
* Desinstalar aplicativos UWP
* Limpe a unidade do sistema e os perfis do navegador
* Corrija problemas comuns de registro
* Faça ping em IPs e avalie a latência
* Pesquise IPs em SHODAN.io
* Altere rapidamente o servidor DNS (de uma lista predefinida)
* Liberar cache DNS
* Remova programas de inicialização indesejados
* Edite seu arquivo HOSTS
* Identificar e encerrar identificadores de bloqueio de arquivo
* Ferramenta de inspeção de hardware
* Adicione itens ao menu do botão direito da área de trabalho
* Defina comandos personalizados para a caixa de diálogo de execução
* Suporta execuções silenciosas usando um arquivo de modelo

### aurora windows optimizer v11.0
01/15/2024 17:55

# english
### source code
* Added: run as administrator in the source code, to eliminate installer instructions and run, through the compilation itself, aurora windows optimizer.exe
* added: enable running powershell scripts when running aurora, so you don't have to click on the first item in the list after running the application.
* I changed the installer to my own installer created by me and now, the compilation is done by cx_freeze instead of pyinstaller, where it reported as a false positive of viruses.
# New functionalities and features
* added: installation of all .net framework from 1.0 to 8.0 for better system operation.
* Added: Completely disable Windows Defender with Defender Control deactivation utility
* Added: enable or disable the firewall however you want.
* Added: install openshell classic start menu; with a classic Windows 7 design or your choice
# português / portuguese.
### código fonte
* Adicionado: executar como administrador no código fonte, para eliminar  instruções do instalador e executar atravez da própria compilação, aurora windows optimizer.exe
* adicionado: habilitar a execução de scripts powershell ao executar o aurora, para que não precise clicar no primeiro item da lista após executar o aplicativo.
# Novas funcionalidades e recursos
* adicionado: instalação de todos os .net framework do 1.0 até o 8.0 para melhor funcionamento do sistema.
* adicionado: desative completamente o windows defender com o utilitário de desativação defender control
* Adicionado: habilite o firewall ou desabilite da forma que você quiser..
* Adicionado: instale o menu iniciar clássico openshell; com um designe clássico do windows 7 ou sua escolha
* Mudei o instalador para o meu próprio instalador criado por mim e agora, a compilação é feita pelo cx_freeze ao invés do pyinstaller, onde reportava como falso positivo de vírus.
### Aurora windows optimizer V10.0
12/28/2023 16:16

Português
=========

### Código fonte atualizado

O código fonte foi atualizado para uma nova versão polida!

### Atualização de Idioma

O aplicativo e o instalador agora estão configurados em inglês, com apenas um script permanecendo em português (`aurora-pt-br.ps1`).

Esse script de otimização com mais de 67 comandos otimiza PCs com menos de 8GB RAM ou melhora a privacidade e desinstala bloatwares inúteis do seu PC, garantindo a confiabilidade. PS: caso você seja um usuário com um pc +8GB ram, use o Aurora windows optimizer apenas para os 2 últimos fins acima.

### Normas de Segurança

Devido às normas de segurança, implementamos o uso de chaves GPG.

Para verificar a autenticidade do programa, siga estes passos:

1.  Baixe o [GPG para seu sistema operacional](https://gnupg.org/download/).
2.  Após a instalação, importe minha chave GPG pública para o seu PC. Você pode usar:
    
         cd "caminho\para\Aurora-Windows-Optimizer"
         gpg --import pub-aurora.asc
        
    
3.  Para verificar a autenticidade, use o comando:
    
         gpg --verify "aurora-windows-optimizer.exe.gpg" "aurora-windows-optimizer.exe"
        
    
    Se aparecer:
    
        gpg: Good signature from "azurejoga <azurejoga@gmail.com>" [unknown]
        
    
    Significa que funcionou e o programa está autenticado e seguro!
    
4.  Se aparecer uma mensagem semelhante a esta:
    
        gpg: AVISO: Esta chave não está certificada com uma assinatura confiável!
        gpg: Não há indicação de que a assinatura pertence ao dono.
        
    
    Certifique sua própria chave com o seguinte comando:
    
        gpg --lsign-key A40B864FB19D5549096B348EA1CB01C59968F33F
        
    
    Mais uma norma de segurança foi implementada em nosso aplicativo para garantir confiabilidade!
    

### Aviso para Usuários com 8GB ou Mais de RAM

Se o seu PC tiver 8GB ou mais de RAM, o impacto no desempenho e otimização pode ser mínimo. No entanto, se você priorizar a privacidade, ainda pode usar vários comandos disponíveis.

Aurora, agora disponível no chocolatey como um aplicativo de pacote!
====================================================================

Aurora, Windows Optimizer, agora pode ser instalado via Chocolatey. Use os seguintes comandos:

*   Para instalar
    
        choco install aurora
        
    
*   Para desinstalar
    
        choco uninstall aurora
        
    
    Se você quiser ajudar no desenvolvimento, abra um pull request ou um issue! Ficarei feliz em ajudar a contribuir também.
    

English
=======

### Sourcecode

Sourcecode is updated

### Language Update

The application and installer now default to English, with only one script remaining in Portuguese (`aurora-pt-br.ps1`).

This optimization script with 67+ commands optimizes PCs with less than 8GB RAM or improves privacy and uninstalls useless bloattware from your PC, ensuring reliability. PS: if you are a user with a PC +8GB ram, use Aurora windows optimizer only for the last 2 purposes above.

### Safety Rules

Due to security standards, we have implemented the use of GPG keys.

To verify the authenticity of the program, follow these steps:

1.  Download [GPG for your operating system](https://gnupg.org/download/).
2.  After installation, import my public GPG key to your PC. You can use:
    
         cd "path\to\Aurora-Windows-Optimizer"
         gpg --import pub-aurora.asc
        
    
3.  To check authenticity, use the command:
    
         gpg --verify "aurora-windows-optimizer.exe.gpg" "aurora-windows-optimizer.exe"
        
    
    If you see:
    
        gpg: Good signature from "azurejoga <azurejoga@gmail.com>" [unknown]
        
    
    It means it worked, and the program is authenticated and secure!
    
4.  If a similar message appears:
    
        gpg: WARNING: This key is not certified with a trusted signature!
        gpg: There is no indication that the signature belongs to the owner.
        
    
    Certify your own key with the following command:
    
        gpg --lsign-key A40B864FB19D5549096B348EA1CB01C59968F33F
        
    
    Another security standard has been implemented in our application to ensure reliability!
    

### Warning for Users with 8GB or More RAM

If your PC has 8GB or more RAM, the performance and optimization impact may be minimal. However, if you prioritize privacy, you can still use various available commands.

### Aurora, now available on chocolatey as a package app!

Aurora, Windows Optimizer, can now be installed via Chocolatey. Use the following commands:

To install (English and Portuguese):

    choco install aurora
    

To uninstall (English and Portuguese):

    choco uninstall aurora
    

If you want to help develop, open a pull request or an issue! I'll be happy to help contribute too.