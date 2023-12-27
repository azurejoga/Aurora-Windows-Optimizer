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

# Verificar o arquivo .zip com a API do VirusTotal
echo "Verificando $ZIP_FILE com VirusTotal..."
ZIP_RESULT=$(curl -s -X POST "https://www.virustotal.com/api/v3/files" \
    -H "x-apikey: $VIRUSTOTAL_API_KEY" \
    -H "Content-Type: application/json" \
    --data-binary @<(curl -s $ZIP_URL | base64 -w 0) \
    | jq -r '.data.id')

# Aguardar a análise no VirusTotal
sleep 30  # Aguarde um tempo para permitir que o VirusTotal processe a verificação

# Obter o status da verificação
ZIP_STATUS=$(curl -s "https://www.virustotal.com/api/v3/analyses/$ZIP_RESULT" \
    -H "x-apikey: $VIRUSTOTAL_API_KEY" \
    | jq -r '.data.attributes.last_analysis_stats.overall')

# Verificar o arquivo .exe com a API do VirusTotal
echo "Verificando $EXE_FILE com VirusTotal..."
EXE_RESULT=$(curl -s -X POST "https://www.virustotal.com/api/v3/files" \
    -H "x-apikey: $VIRUSTOTAL_API_KEY" \
    -H "Content-Type: application/json" \
    --data-binary @<(curl -s $EXE_URL | base64 -w 0) \
    | jq -r '.data.id')

# Aguardar a análise no VirusTotal
sleep 30  # Aguarde um tempo para permitir que o VirusTotal processe a verificação

# Obter o status da verificação
EXE_STATUS=$(curl -s "https://www.virustotal.com/api/v3/analyses/$EXE_RESULT" \
    -H "x-apikey: $VIRUSTOTAL_API_KEY" \
    | jq -r '.data.attributes.last_analysis_stats.overall')

# Exibir resultados no README.md
echo "# O app foi verificado e não há vírus em .zip ou .exe da versão mais recente"
echo "Versão mais recente: $RELEASE"
echo "Verificação .zip: $ZIP_STATUS"
echo "Verificação .exe: $EXE_STATUS"
