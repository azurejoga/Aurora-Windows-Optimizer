$versions = @{
    'net1.0'  = 'https://download.microsoft.com/download/6/d/1/6d1bdb81-5fa1-436d-9a07-9664cf007746/NETCFSetup.msi';
    'net1.1'  = 'https://download.microsoft.com/download/8/c/f/8cf55d0c-235e-4062-933c-64ffdf7e7043/dotnetfx.exe';
    'net2.0'  = 'https://download.microsoft.com/download/9/1/0/91023b56-c5ff-40f1-a1b9-239c1a744454/netfx20sp2_x64pt-BR.exe';
    'net3'    = 'https://download.microsoft.com/download/4/9/0/49001df1-af88-4a4d-b10f-2d5e3a8ea5f3/dotnetfx30SP1setup.exe';
    'net3.5'  = 'https://download.microsoft.com/download/0/6/1/061F001C-8752-4600-A198-53214C69B51F/dotnetfx35setup.exe';
    'net4'    = 'https://go.microsoft.com/fwlink/?linkid=2203305';
    'net4.7.1' = 'https://go.microsoft.com/fwlink/?LinkId=852092';
    'net4.7.2' = 'https://go.microsoft.com/fwlink/?LinkId=863262';
    'net4.8'  = 'https://go.microsoft.com/fwlink/?LinkId=2085155';
    'net5'    = 'https://download.visualstudio.microsoft.com/download/pr/14ccbee3-e812-4068-af47-1631444310d1/3b8da657b99d28f1ae754294c9a8f426/dotnet-sdk-5.0.408-win-x64.exe';
    'net6'    = 'https://download.visualstudio.microsoft.com/download/pr/83d32568-c5a2-4117-9591-437051785f41/e75171da01b1fa5c796660dc4b96beed/windowsdesktop-runtime-6.0.23-win-x64.exe';
    'net7'    = 'https://download.visualstudio.microsoft.com/download/pr/f9ea536d-8e1f-4247-88b8-e79e33fa0873/c06e39f73a3bb1ec8833bb1cde98fce3/windowsdesktop-runtime-7.0.12-win-x64.exe';
    'net8'    = 'https://download.visualstudio.microsoft.com/download/pr/9c540179-a75c-4418-94fd-3bfe580e4251/6560fb0d71bf6434a4fe17b5cfa00a45/windowsdesktop-runtime-8.0.0-rc.2.23479.10-win-x64.exe';
}

foreach ($version in $versions.Keys) {
    $url = $versions[$version]

    try {
        # Download
        $installerPath = "$env:TEMP\dotnet_${version}_installer.exe"
        Invoke-WebRequest -Uri $url -OutFile $installerPath -ErrorAction Stop
        Write-Host "Downloading .NET Framework $version..."

        # Instalação
        Start-Process -FilePath $installerPath -ArgumentList '/install', '/quiet' -Wait
        Write-Host ".NET Framework $version installed successfully."

    } catch {
        Write-Host "Error handling .NET Framework $($version): $_"
    } finally {
        # Remoção do arquivo temporário
        Remove-Item -Path $installerPath -Force
        Write-Host ".NET Framework $version temporary installer removed."
    }
}
