# Check if you are running as administrator
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "Running as a non-administrator. Requesting elevation..."

    # Request elevation to administrator
    Start-Process powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$($MyInvocation.MyCommand.Path)`"" -Verb RunAs
    exit
}

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

function Show-FolderBrowserDialog {
    $folderBrowser = New-Object System.Windows.Forms.FolderBrowserDialog
    $folderBrowser.Description = "Select the installation folder for Aurora Windows Optimizer"
    
    if ($folderBrowser.ShowDialog() -eq 'OK') {
        $textBox.Text = $folderBrowser.SelectedPath
    }
}

function Install-AuroraWindowsOptimizer {
    if (-not $textBox.Text) {
        [System.Windows.Forms.MessageBox]::Show("Please select a folder before installing.", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
        return
    }

    # Set variables
    $repo = "azurejoga/Aurora-Windows-Optimizer"
    $file = "Aurora-Windows-Optimizer.zip"
    $targetDir = $textBox.Text
    $shortcutName = "Aurora Windows Optimizer"

    # Determine the latest release
    $releases = "https://api.github.com/repos/$repo/releases"
    $tag = (Invoke-WebRequest -Uri $releases -UseBasicParsing | ConvertFrom-Json)[0].tag_name

    # Download the zip file
    $download = "https://github.com/$repo/releases/download/$tag/$file"
    Invoke-WebRequest $download -OutFile $file

    # Extract the contents of the zip file
    Expand-Archive $file -DestinationPath $targetDir

    # Create a shortcut on the desktop using WScript.Shell
    $shell = New-Object -ComObject WScript.Shell
    $executablePath = Join-Path $targetDir "aurora-windows-optimizer\aurora windows optimizer.exe"
    $shortcutPath = [System.IO.Path]::Combine([System.Environment]::GetFolderPath('Desktop'), "$shortcutName.lnk")

    # Remove existing shortcut if any
    if (Test-Path $shortcutPath) {
        Remove-Item $shortcutPath -Force
    }

    # Create new shortcut
    $shortcut = $shell.CreateShortcut($shortcutPath)
    $shortcut.TargetPath = $executablePath
    $shortcut.WorkingDirectory = Join-Path $targetDir "aurora-windows-optimizer"
    $shortcut.Save()

    # Display a success message
    [System.Windows.Forms.MessageBox]::Show("The latest release of Aurora Windows Optimizer has been successfully downloaded and installed.", "Installation Complete", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
}

# Create the main window
$form = New-Object System.Windows.Forms.Form
$form.Text = "Aurora Windows Optimizer Installer"
$form.Size = New-Object System.Drawing.Size(400,150)
$form.StartPosition = "CenterScreen"

# Create a button to open the folder selector
$buttonFolder = New-Object System.Windows.Forms.Button
$buttonFolder.Location = New-Object System.Drawing.Point(50,50)
$buttonFolder.Size = New-Object System.Drawing.Size(150,30)
$buttonFolder.Text = "Browse Folder"
$buttonFolder.Add_Click({ Show-FolderBrowserDialog })

# Create a button to install
$buttonInstall = New-Object System.Windows.Forms.Button
$buttonInstall.Location = New-Object System.Drawing.Point(200,50)
$buttonInstall.Size = New-Object System.Drawing.Size(150,30)
$buttonInstall.Text = "Install"
$buttonInstall.Add_Click({
    $progressBar.Value = 0
    $form.Update()
    Install-AuroraWindowsOptimizer
    $progressBar.Value = 100
})

# Create a progress bar
$progressBar = New-Object System.Windows.Forms.ProgressBar
$progressBar.Location = New-Object System.Drawing.Point(50, 120)
$progressBar.Size = New-Object System.Drawing.Size(300, 20)
$progressBar.Style = [System.Windows.Forms.ProgressBarStyle]::Continuous

# Create a text box to display the folder path
$textBox = New-Object System.Windows.Forms.TextBox
$textBox.Location = New-Object System.Drawing.Point(50, 90)
$textBox.Size = New-Object System.Drawing.Size(300, 20)

# Add controls to the main window
$form.Controls.Add($buttonFolder)
$form.Controls.Add($buttonInstall)
$form.Controls.Add($progressBar)
$form.Controls.Add($textBox)

# Show the window
$form.ShowDialog()
