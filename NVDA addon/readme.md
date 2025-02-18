# NVDA Add-on Scons Template

This package contains a basic template structure for NVDA add-on development, building, distribution and localization.
For details about NVDA add-on development, please see the [NVDA Add-on Development Guide](https://github.com/nvdaaddons/DevGuide/wiki/NVDA-Add-on-Development-Guide).
The NVDA add-on development/discussion list [is here](https://nvda-addons.groups.io/g/nvda-addons)
Information specific to NV Access add-on store [can be found here](https://github.com/nvaccess/addon-datastore).

Copyright (C) 2012-2024 NVDA Add-on team contributors.

This package is distributed under the terms of the GNU General Public License, version 2 or later. Please see the file COPYING.txt for further details.

[alekssamos](https://github.com/alekssamos/) added automatic package of add-ons through Github Actions.

For details about Github Actions  please see the [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).

Copyright (C) 2022 alekssamos

## Features

This template provides the following features you can use during NVDA add-on development and packaging:

* Automatic add-on package creation, with naming and version loaded from a centralized build variables file (buildVars.py) or command-line interface.
	* See packaging section for details on using command-line switches when packaging add-ons with custom version information.
	* This process will happen automatically when receiving a pull request, and there is also the possibility of manual launch.
	* To let the workflow run automatically when pushing to main or master (development) branch, remove the comment for branches line in GitHub Actions (`.github/workflows/build_addon.yml`).
	* If you have created a tag (E.G.: `git tag v1.0 && git push --tag`), then a release will be automatically created and the add-on file will be uploaded as an asset.
	* Otherwise, with normal commits or with manual startup, you can download the artifacts from the Actions page of your repository.
* Manifest file creation using a template (manifest.ini.tpl). Build variables are replaced on this template. See below for add-on manifest specification.
* Compilation of gettext mo files before distribution, when needed.
	* To generate a gettext pot file, please run `scons pot`. An `addon-name.pot` file will be created with all gettext messages for your add-on. You need to check the `buildVars.i18nSources` variable to comply with your requirements.
* Automatic generation of manifest localization files directly from gettext po files. Please make sure buildVars.py is included in i18nFiles.
* Automatic generation of HTML documents from markdown (.md) files, to manage documentation in different languages.

In addition, this template includes configuration files for the following tools for use in add-on development and testing (see "additional tools" section for details):

* Ruff (pyproject.toml/tool.ruff sections): a Python linter written in Rust. Sections starting with tool.ruff house configuration options for Ruff.
* Configuration for VS Code. It requires NVDA's repo at the same level as the add-on folder containing your actual source files, with prepared source code (`scons source`). preparing the source code is a step in the instructions for building NVDA itself, see [The NVDA Repository](https://github.com/nvaccess/nvda) for details.
        * Place the .vscode in this repo within the addon folder, where your add-on source files (will) reside. The settings file within this folder assumes the NVDA repository is within the parent folder of this folder. If your addon folder is within the addonTemplate folder, then your NVDA repository folder needs to also be within the addonTemplate folder, or the source will not be found.
        * Open the addon folder in VS Code. This should initialize VS Code with the correct settings and provide you with code completion and other VS Code features. 
	* Press `control+shift+m` after saving a file to search for problems.
	* Use arrow and tab keys for the autocompletion feature.
	* Press `control+shift+p` to open the commands palette and search for recommended extensions to install or check if they are installed.

## Requirements

You need the following software to use this code for your NVDA add-on development and packaging:

* a Python distribution (3.11 or later is recommended). Check the [Python Website](https://www.python.org) for Windows Installers. Please note that at present, preparing the NVDA source code requires the 32-bit version of Python 3.11.
* Scons - [Website](https://www.scons.org/) - version 4.5.2 or later. You can install it via PIP.
* GNU Gettext tools, if you want to have localization support for your add-on - Recommended. Any Linux distro or cygwin have those installed. You can find windows builds [here](https://gnuwin32.sourceforge.net/downlinks/gettext.php).
* Markdown 3.3.0 or later, if you want to convert documentation files to HTML documents. You can install it via PIP.

Note, that you may not need these tools in a local build environment, if you are using [Appveyor](https://appveyor.com/) or [GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions), to build and package your add-ons.

## Usage

### To create a new NVDA add-on using this template:

1. Create an empty folder to hold the files for your add-on.
2. Copy the folder:
```
site_scons
```
and the following files, into your new empty folder:
```
buildVars.py
manifest.ini.tpl
manifest-translated.ini.tpl
sconstruct
.gitignore
.gitattributes
```
3. If you intend to use the provided GitHub workflow, also copy the folder:
```
.github
```
and file:
```
.pre-commit-config.yaml
```
4. Create an `addon` folder inside your new folder. You will put your code in the usual folders for NVDA extensions, under the `addon` folder. For instance: `globalPlugins`, `synthDrivers`, etc.
5. In the `buildVars.py` file, change variable `addon_info` with your add-on's information (name, summary, description, version, author, url, source url, license, and license URL). Also, be sure to carefully set the paths contained in the other variables in that file. If you need to use custom Markdown extensions, original add-on interface language is not English, or include custom braille translations tables, be sure to fil out markdown list, base language variable, and braille tables dictioanry, respectively.
6. Gettext translations must be placed into `addon\locale\<lang>/LC_MESSAGES\nvda.po`.

#### Add-on manifest specification

An add-on manifest generated manually or via `buildVars.py` must include the following information:

* Name (string): a unique identifier for the add-on. It must use camel case (e.g. someModule). This is also used as part of add-on store to identify the add-on uniquely.
* Summary (string): name as shown on NVDA's Add-on store.
* Description (string): a short detailed description about the add-on.
* Version (string), ideally number.number with an optional third number, denoting major.minor.patch.
* Author (string and an email address): one or more add-on author contact information in the form "name <email@address>".
* URL (string): a web address where the add-on information can be found such as add-on repository.
* docFileName (string): name of the documentation file.
* minimumNVDAVersion (year.major or year.major.minor): the earliest version of NVDA the add-on is compatible with (e.g. 2019.3). Add-ons are expected to use features introduced in this version of NVDA or declare compatibility with it.
* lastTestedNVDAVersion (year.major or year.major.minor): the latest or last tested version of NVDA the add-on is said to be compatible with (e.g. 2020.3). Add-on authors are expected to declare this value after testing add-ons with the version of NVDA specified.
* addon_updateChannel (string or None): the update channel for the add-on release.

In addition, the following information must be filled out (not used in the manifest but used elsewhere such as add-on store) in buildVars:

* sourceURL (string): repository URL for the add-on source code.
* license (string): the license of the add-on and its source code.
* licenseURL: the URL for the license file.

##### Custom add-on information

In addition to the core manifest data, custom add-on information can be specified. 

###### Braille translation tables
Information on custom braille tables must be specified in buildVars under `brailleTables` dictionary as follows:

* Table name (string key for a nested dictionary): each `brailleTables` entry is a filename for the included custom braille table placed in `brailleTables` folder inside `addon` folder. This nested dictionary should specify:
	* displayName (string): the name of the table shown to users and is translatable.
	* contracted (True/False): is this a contracted braille table (True) or uncontracted (False).
	* output (True/False): the table can be listed in output table list in NVDA's braille settings.
	* input (True/False): braille can be entered using this table and listed in input table list in NVDA's braille settings.

Note: you must fill out this dictionary if at least one custom braille table is included in the add-on. If not, leave the dictionary empty.

###### Speech symbol dictionaries
Information on custom symbol dictionaries must be specified in buildVars under `symbolDictionaries` dictionary as follows:

* Dictionary name (string key for a nested dictionary): each `symbolDictionaries` entry is a name for the included custom symbol dictionary placed in `locale\<language>` folder inside `addon` folder. The file is named `symbols-<dictionary_name>.dic`. This nested dictionary should specify:
	* displayName (string): the name of the dictionary shown to users and is translatable.
	* mandatory (True/False): Always enabled (True) or optional and visible in the GUI (False)

Note: you must fill out this dictionary if at least one custom symbol dictionary is included in the add-on. If not, leave the dictionary empty.

### To manage documentation files for your addon:

1. Copy the `readme.md` file for your add-on to the first created folder, where you copied `buildVars.py`. You can also copy `style.css` to improve the presentation of HTML documents.
2. Documentation files (named `readme.md`) must be placed into `addon\doc\<lang>/`.

### To package the add-on for distribution:

1. Open a command line, change to the folder that has the `sconstruct` file (usually the root of your add-on development folder) and run the `scons` command. The created add-on, if there were no errors, is placed in the current directory.
2. You can further customize variables in the `buildVars.py` file.
3. You can also customize version and update channel information from command line by passing the following switches when running scons:
	* version: add-on version string.
	* versionNumber: add-on version number of the form major.minor.patch (all integers)
	* channel: update channel (do not use this switch unless you know what you are doing).
	* dev: suitable for development builds, names the add-on according to current date (yyyymmdd) and sets update channel to "dev".

### Additional tools

The template includes configuration files for use with additional tools such as linters. These include:

* Ruff (pyproject.toml): a Python linter written in Rust (0.4.10 or later, can be installed with PIP).

Read the documentation for the tools you wish to use when building and developing add-ons.

Note that this template only provides a basic add-on structure and build infrastructure. You may need to adapt it for your specific needs such as using additional tools.

If you have any issues please use the NVDA addon list mentioned above.
