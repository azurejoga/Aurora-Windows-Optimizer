## Installation Methods

You can see the [changelog here](https://github.com/azurejoga/Aurora-Windows-Optimizer/blob/aurora/changelog.md)

To install Aurora, Windows Optimizer, there are 6 installation methods.


### download em Microsoft store
You can officially download Aurora from the Microsoft store.
[here](https://apps.microsoft.com/detail/xp8m0w4jc5jhg9?hl=ko-KR&gl=KR)


### download, winget. Windows Package Manager
Download aurora officially on winget using the command below.

```winget
winget install azurejoga.aurorawindowsoptimizer
```


### Download in PowerShell

#### 1. Download from PowerShell Gallery

To install, open PowerShell and paste or type the following commands:

```powershell
Install-Script -Name aurora
Aurora
```

The Aurora installer will start, where you must choose a directory and click install.

#### 2. Install with One Command

Open PowerShell and paste or type the following command:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted -Force; Invoke-Expression (Invoke-WebRequest -Uri "https://github.com/azurejoga/Aurora-Windows-Optimizer/raw/aurora/installer.ps1" -UseBasicParsing).Content
```

### Download from Chocolatey

```powershell
choco install aurora-windows-optimizer --version=13.0.0
```

Follow the on-screen instructions, choose the folder, and click install.

### Download the ZIP

Start your journey to a more powerful and efficient PC. Download Aurora for Windows 11 and Windows 10 now:

- **SHA-256: ZIP VERSION**501f7524a07ad50509f26a2d6ef6db185083ec5c2d1af97b57c3c4a5a2e74305

[Download Aurora, Windows Optimizer, ZIP version](https://github.com/azurejoga/Aurora-Windows-Optimizer/releases/download/aurora16/aurora-windows-optimizer.zip)