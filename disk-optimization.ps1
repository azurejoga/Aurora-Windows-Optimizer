# Start disk cleanup
Start-Process cleanmgr.exe -ArgumentList "/altoclean"

# Displays a message to the user
Write-Host "Please minimize the window and click OK in the Disk Cleanup window."

# Detects disk type (SSD or HD)
$diskType = (Get-PhysicalDisk | Select-Object -First 1).MediaType
Write-Host "disk type : $diskType"

# Enable optimization for SSD or compression for HD
if ($diskType -eq 'SSD') {
    Write-Host "Otimização do SSD ativada."
    Optimize-Volume -DriveLetter C -ReTrim -Analyze
}
elseif ($diskType -eq 'HDD') {
    Write-Host "HD Enabled Disk Compression."
    Enable-VolumeCompression -DriveLetter C
}
else {
    Write-Host "Unable to detect disk type."
}
