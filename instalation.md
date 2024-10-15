## Installation Methods

You can see the [changelog here](https://github.com/azurejoga/Aurora-Windows-Optimizer/blob/aurora/changelog.md).

To install Aurora, Windows Optimizer, there are several methods available:

### Microsoft Store
You can officially download Aurora from the Microsoft Store [here](https://apps.microsoft.com/detail/xp8m0w4jc5jhg9?hl=ko-KR&gl=KR).

### Winget (Windows Package Manager)
Install Aurora using Winget with the following command:

```winget
winget install azurejoga.aurorawindowsoptimizer
```

### PowerShell

#### 1. PowerShell Gallery
Open PowerShell and run the following commands:

```powershell
Install-Script -Name aurora
Aurora
```

#### 2. One Command Installation
Run this command in PowerShell to download and install Aurora:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted -Force; Invoke-Expression (Invoke-WebRequest -Uri "https://github.com/azurejoga/Aurora-Windows-Optimizer/raw/aurora/installer.ps1" -UseBasicParsing).Content
```

### Chocolatey
Install Aurora using Chocolatey:

```powershell
choco install aurora-windows-optimizer --version=13.0.0
```

### ZIP Download
Get Aurora for Windows 10 and 11 by downloading the ZIP version:

- **SHA-256:** `5123e47574eaabae4b621eed575d11d6b6269a9a3fc8f8ee9924bae84a69c8f0`

[Download Aurora, ZIP version](https://github.com/azurejoga/Aurora-Windows-Optimizer/releases/download/aurora18/aurora-windows-optimizer.zip)

### NVDA Addon
Aurora is also available as an NVDA Addon for improved accessibility. Download the latest version (v18.0 or higher):

[Download NVDA Addon](https://github.com/azurejoga/Aurora-Windows-Optimizer/releases)

* hotkey: NVDA + SHIFT + A to activate aurora!

---

## Updating Aurora

To update Aurora, open the program and press **ALT** or go to the **Tools** menu, then select **Check for Updates**. A new installer will launch, and you will need to select the directory where Aurora is installed. Common installation directories include:

- Microsoft Store: Documents
- Documents: Where the NVDA Addon may be found (under `Documents).
- Chocolatey: Chocolatey’s default directory.
- Winget: Winget’s installation directory.

Note that the NVDA Addon is usually located in the `Documents` folder, but other installations depend on the user-defined directories.

After selecting the correct path, follow the on-screen instructions to complete the update.
