### Changelog, Aurora Windows Optimizer V10.0
12/28/2023 16:16


# Português

### Código fonte atualizado
O código fonte foi atualizado para uma nova versão polida!

### Atualização de Idioma
O aplicativo e o instalador agora estão configurados em inglês, com apenas um script permanecendo em português (`aurora-pt-br.ps1`).

Esse script de otimização com mais de 67 comandos otimiza PCs com menos de 8GB RAM ou melhora a privacidade e desinstala bloatwares inúteis  do seu PC, garantindo a confiabilidade. PS: caso você seja um usuário com um pc +8GB ram, use o Aurora windows optimizer apenas para os 2 últimos fins acima.

### Normas de Segurança
Devido às normas de segurança, implementamos o uso de chaves GPG.

Para verificar a autenticidade do programa, siga estes passos:
1. Baixe o [GPG para seu sistema operacional](https://gnupg.org/download/).
2. Após a instalação, importe minha chave GPG pública para o seu PC. Você pode usar:

    ```powershell
    cd "caminho\para\Aurora-Windows-Optimizer"
    gpg --import pub-aurora.asc
    ```

3. Para verificar a autenticidade, use o comando:

    ```powershell
    gpg --verify "aurora-windows-optimizer.exe.gpg" "aurora-windows-optimizer.exe"
    ```

   Se aparecer:

   ```
   gpg: Good signature from "azurejoga <azurejoga@gmail.com>" [unknown]
   ```

   Significa que funcionou e o programa está autenticado e seguro!

4. Se aparecer uma mensagem semelhante a esta:

   ```
   gpg: AVISO: Esta chave não está certificada com uma assinatura confiável!
   gpg: Não há indicação de que a assinatura pertence ao dono.
   ```

   Certifique sua própria chave com o seguinte comando:

   ```powershell
   gpg --lsign-key A40B864FB19D5549096B348EA1CB01C59968F33F
   ```

   Mais uma norma de segurança foi implementada em nosso aplicativo para garantir confiabilidade!

### Aviso para Usuários com 8GB ou Mais de RAM
Se o seu PC tiver 8GB ou mais de RAM, o impacto no desempenho e otimização pode ser mínimo. No entanto, se você priorizar a privacidade, ainda pode usar vários comandos disponíveis.

# Aurora, agora disponível no chocolatey como um aplicativo de pacote!

Aurora, Windows Optimizer, agora pode ser instalado via Chocolatey. Use os seguintes comandos:

* Para instalar 
```PowerShell
choco install aurora
```

* Para desinstalar 
```PowerShell
choco uninstall aurora
Se você quiser ajudar no desenvolvimento, abra um pull request ou um issue!
Ficarei feliz em ajudar a contribuir também.


# English
### Sourcecode
Sourcecode is updated
### Language Update
The application and installer now default to English, with only one script remaining in Portuguese (`aurora-pt-br.ps1`).

This optimization script with 67+ commands optimizes PCs with less than 8GB RAM or improves privacy and uninstalls useless bloattware from your PC, ensuring reliability. PS: if you are a user with a PC +8GB ram, use Aurora windows optimizer only for the last 2 purposes above.

### Safety Rules
Due to security standards, we have implemented the use of GPG keys.

To verify the authenticity of the program, follow these steps:
1. Download [GPG for your operating system](https://gnupg.org/download/).
2. After installation, import my public GPG key to your PC. You can use:

    ```powershell
    cd "path\to\Aurora-Windows-Optimizer"
    gpg --import pub-aurora.asc
    ```

3. To check authenticity, use the command:

    ```powershell
    gpg --verify "aurora-windows-optimizer.exe.gpg" "aurora-windows-optimizer.exe"
    ```

   If you see:

   ```
   gpg: Good signature from "azurejoga <azurejoga@gmail.com>" [unknown]
   ```

   It means it worked, and the program is authenticated and secure!

4. If a similar message appears:

   ```
   gpg: WARNING: This key is not certified with a trusted signature!
   gpg: There is no indication that the signature belongs to the owner.
   ```

   Certify your own key with the following command:

   ```powershell
   gpg --lsign-key A40B864FB19D5549096B348EA1CB01C59968F33F
   ```

   Another security standard has been implemented in our application to ensure reliability!

### Warning for Users with 8GB or More RAM
If your PC has 8GB or more RAM, the performance and optimization impact may be minimal. However, if you prioritize privacy, you can still use various available commands.

### Aurora, now available on chocolatey as a package app!

Aurora, Windows Optimizer, can now be installed via Chocolatey. Use the following commands:

To install (English and Portuguese):
```PowerShell
choco install aurora
```

To uninstall (English and Portuguese):
```PowerShell
choco uninstall aurora
If you want to help develop, open a pull request or an issue!
I'll be happy to help contribute too.
