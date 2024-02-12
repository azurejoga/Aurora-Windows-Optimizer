# zip file URL
$zipUrl = "https://github.com/azurejoga/Aurora-Windows-Optimizer/raw/aurora/vc-packages.zip"

# Name of the zip file and extraction directory# Name of the zip file and extraction directory
$zipFileName = "vc-packages.zip"
$extractedDirectoryName = "vc-packages"

# Full path to the zip file
$zipPath = Join-Path -Path $PSScriptRoot -ChildPath $zipFileName

# Download the zip file
Invoke-WebRequest -Uri $zipUrl -OutFile $zipPath

# Extract the contents of the zip
Expand-Archive -Path $zipPath -DestinationPath $PSScriptRoot -Force

# Run install-all.bat as administrator
$batFilePath = Join-Path -Path $PSScriptRoot -ChildPath "$extractedDirectoryName\install_all.bat"
Start-Process -FilePath $batFilePath -Verb RunAs -Wait

# Wait for bat execution to complete# Wait for bat execution to complete
Write-Host "Aguardando a conclusão da execução do install-all.bat..."
Start-Sleep -Seconds 30  # Você pode ajustar o tempo de espera conforme necessário

# Remove zip file and extracted directory
Remove-Item -Path $zipPath -Force
Remove-Item -Path (Join-Path -Path $PSScriptRoot -ChildPath $extractedDirectoryName) -Recurse -Force

Write-Host "Script completed successfully."
