# Aurora Otimizador do Windows

# Leia em Português
[Leia em Português](https://github.com/azurejoga/Aurora-Windows-Optimizer/blob/aurora/readme-pt-br.md)


# leer em español
[Leer em español](https://github.com/azurejoga/Aurora-Windows-Optimizer/blob/aurora/readme_es.md)


# Leia em inglês
[README en english](https://github.com/azurejoga/Aurora-Windows-Optimizer/blob/aurora/readme.md)


# Aurora: Windows Optimizer™ transformando seu PC em uma máquina poderosa! 



**Aurora™** é o melhor otimizador do Windows, uma ferramenta incrivelmente poderosa que melhora o desempenho do seu PC! ✨

Agradecimentos especiais a [edu-mx](https://github.com/edu-mx) pela colaboração no desenvolvimento. 🙌


### Aviso para usuários com 8 GB ou mais de RAM
Se o seu PC tiver 8 GB ou mais de RAM, o impacto no desempenho e na otimização poderá ser mínimo. No entanto, se você priorizar a privacidade, ainda poderá usar vários comandos disponíveis


## Por que escolher Aurora? 🤔

Se você deseja **otimizar seu PC para desempenho máximo** ou simplesmente **eliminar recursos indesejados do Windows**, Aurora é a resposta. Este otimizador inovador oferece:


## aurora, o otimizador do Windows é seguro?
Sim, o Aurora Windows Optimizer é seguro e você mesmo pode verificar com algumas ferramentas.
1. Vírus total  [veja e verifique o aurora no virus total](https://www.virustotal.com/gui/file/8a2a97b1ee70674a5d7571d4c8985de3fa8270ad5532517a4dc3f502dbef1aab?nocache=1)
2. Verifique com chaves GPG. Assinei minhas chaves gpg para garantir que o executável seja legítimo.
3. nunca baixe de sites que não sejam chocolatey ou github e sempre verifique os hashes para comparação, se o hash do zip ou do executável não for o mesmo, não confie, e não instale ou execute.

### 🌄 Recursos poderosos:

- **Adicione seus próprios comandos**: tenha controle total e personalize o Aurora com seus próprios comandos.
- **Atualizações Simplificadas**: Fique atualizado com o toque de um botão, diretamente do aplicativo.
- **Otimização sem complicações**: diga adeus aos fóruns obscuros e sites cheios de anúncios.
- **Comunidade de Colaboradores**: Participe de uma comunidade vibrante e compartilhe seus comandos personalizados.
- **Código aberto**: contribua com o projeto e veja suas alterações ganharem vida no repositório aberto.
- **Capacidade de editar, remover ou adicionar seus próprios comandos conforme desejar; a personalização é sua! 😱**
- **Mova para o topo, final da lista ou até mesmo classifique os comandos em ordem alfabética! ✌**
- **Crie um ponto de restauração dentro do próprio Aurora e melhore seu PC sem medo! 👏**
- **Remova aplicativos nativos inúteis que vêm pré-instalados no seu PC! Cansado de bloatware? Nós estamos aqui para ajudar! 🐱‍🎁**
- **Instale aplicativos úteis através do Aurora, Windows Optimizer**
- **Os aplicativos listados são:**
1. NVDA, instale o NVDA: Leitor de tela para cegos.
2. instale todos os pacotes VC++ de tempo de execução visual.
3. instale todo o framework .net de 1.0 a 8.0
4. Instale o tão necessário java8 JDK!
5. Instale o winrar ou, se preferir, o 7zip.
6. habilite o directplay,necessário para rodar alguns jogos que requerem este componente/recurso.
7. desative o Windows Defender ou desative a telemetria, a escolha é sua!
8. Instale o VS code: para desenvolvedores!
9. Faça login automaticamente no Windows sem precisar digitar sua senha!
10. Instale um menu Iniciar clássico ou gerenciador de tarefas, melhor que o do Windows 10! É ainda melhor! com visual clássico!
11. habilite ou desabilite o firewall, a escolha é sua!
12. Limpe o cache DNS, otimize seu windows com mais de 67 comandos e muito mais!
13. desabilite completamente o windows update, totalmente!
14. receba notificações de quando um comando foi concluido com sucesso ou aconteceu algum erro.
15. a mensagem de boas vindas agora não aparece mais depois da primeira execução
Nossa lista de recursos que o Aurora oferece será atualizada à medida que introduzimos novos recursos!

### 🌟 O futuro é incrível:

Estamos empenhados em adicionar mais recursos incríveis ao Aurora. Conte com novos idiomas, personalização avançada do registro do Windows e muito mais. Além disso, o Aurora é totalmente acessível para usuários com deficiência visual. 🌌

## Como usar o Aurora? 🚀

Começar a otimizar seu PC com Aurora é fácil:

1. Abra o aplicativo como administrador para obter melhor desempenho.
2. Ignore a mensagem de boas-vindas se você já tiver definido um ponto de restauração.
3. Escolha entre uma variedade de comandos de otimização ou crie o seu próprio. Pressione Enter em um comando e espere que ele seja executado. Se o programa parar de responder, é normal, não é um bug e o script será executado normalmente devido ao uso de um método de execução externo
4. Edite, mova e remova comandos de acordo com sua preferência.

# É altamente recomendável criar um ponto de restauração antes de fazer alterações para que você possa desfazê-las se necessário.

# Não nos responsabilizamos por nada que aconteça com seu PC; Use por sua conta e risco!

## Reporte bugs e colabore 🐞😻

Se você encontrar algum problema ou tiver sugestões de melhorias, crie um *Issue*. A colaboração é essencial para valorizar Aurora e torná-la ainda mais incrível.

## métodos de instalação
Você pode ver o [log de alterações aqui](https://github.com/azurejoga/Aurora-Windows-Optimizer/blob/aurora/changelog.md)


Para instalar o Aurora, Windows Optimizer
Existem 4 métodos de instalação.


## baixe no powershell
Existem duas maneiras para baixar o aurora via powershell
1. [na galeria do powershell](https://www.powershellgallery.com/packages/aurora/15.0)
* para instalar faça o seguinte
* abra o powershell e cole ou / digite o comando
```
Install-Script -Name aurora
```
* depois, digite 
```
aurora
```
O instalador do aurora irá iniciar e você deve escolher um dieretório  e clicar em install

2. Instale com um comando
* abra o powershell e cole ou / digite o seguinte comando
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted -Force; Invoke-Expression (Invoke-WebRequest -Uri "https://github.com/azurejoga/Aurora-Windows-Optimizer/raw/aurora/installer.ps1" -UseBasicParsing).Content
```

## baixe do chocolatey.

```
choco install aurora-windows-optimizer --version=13.0.0
```

Siga as instruções na tela, escolha a pasta e clique em instalar


## baixe o zip abaixo

Comece sua jornada para um PC mais potente e eficiente. Baixe Aurora para Windows 11 e Windows 10 agora:


- **SHA-256: ZIP VERSION** 8a2a97b1ee70674a5d7571d4c8985de3fa8270ad5532517a4dc3f502dbef1aab


[Baixar Aurora, Windows Optimizer, versão ZIP](https://github.com/azurejoga/Aurora-Windows-Optimizer/releases/download/aurora16/aurora-windows-optimizer.zip)


# Obrigado por escolher o Aurora para elevar o desempenho do seu PC a níveis sem precedentes! 💪✨

# Licenciado sob a licença MIT