#!/bin/bash

# Obter a versão mais recente do release
RELEASE=$(curl -s https://api.github.com/repos/azurejoga/Aurora-Windows-Optimizer/releases/latest | jq -r '.tag_name')

# Obter a última versão da tag sem o prefixo 'v'
RELEASE_TAG=$(echo $RELEASE | sed 's/v//')

# Construir URLs para os arquivos .zip e .exe
DOWNLOAD_URL="https://github.com/azurejoga/Aurora-Windows-Optimizer/releases/download/$RELEASE_TAG/"
ZIP_FILE="aurora-windows-optimizer.zip"
EXE_FILE="aurora-install.exe"

ZIP_URL="$DOWNLOAD_URL$ZIP_FILE"
EXE_URL="$DOWNLOAD_URL$EXE_FILE"

# Exibir resultados no README.md em formato HTML
HTML_OUTPUT="README.html"

# Iniciar o conteúdo HTML
echo "<h1>Verificação de Vírus para a Versão $RELEASE</h1>" > $HTML_OUTPUT
echo "<p>Links para os arquivos:</p>" >> $HTML_OUTPUT
echo "<ul>" >> $HTML_OUTPUT
echo "<li><a href=\"$ZIP_URL\">$ZIP_FILE</a></li>" >> $HTML_OUTPUT
echo "<li><a href=\"$EXE_URL\">$EXE_FILE</a></li>" >> $HTML_OUTPUT
echo "</ul>" >> $HTML_OUTPUT

# Verificar vírus usando a API do VirusTotal
echo "Verificando $ZIP_FILE e $EXE_FILE com VirusTotal..."

# Usando a API do VirusTotal para verificar os arquivos
VT_RESULT_ZIP=$(curl -s --request POST \
  --url https://www.virustotal.com/api/v3/files \
  --header "x-apikey: $VIRUSTOTAL_API_KEY" \
  --form file=@$ZIP_URL)

VT_RESULT_EXE=$(curl -s --request POST \
  --url https://www.virustotal.com/api/v3/files \
  --header "x-apikey: $VIRUSTOTAL_API_KEY" \
  --form file=@$EXE_URL)

# Adicionar resultados ao HTML
echo "<p>Resultados da Verificação .zip:</p>" >> $HTML_OUTPUT
echo "<pre>$VT_RESULT_ZIP</pre>" >> $HTML_OUTPUT

echo "<p>Resultados da Verificação .exe:</p>" >> $HTML_OUTPUT
echo "<pre>$VT_RESULT_EXE</pre>" >> $HTML_OUTPUT

# Exibir mensagem de conclusão no HTML
echo "<p>Verificação concluída.</p>" >> $HTML_OUTPUT

# Adicionar HTML gerado ao README.md
cat $HTML_OUTPUT >> README.md

# Limpar arquivos temporários
rm $HTML_OUTPUT
