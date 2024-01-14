import wx
import subprocess
import pickle
import webbrowser
import ctypes
import os
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if not is_admin():
    run_as_admin()
    sys.exit()

# Comando PowerShell para habilitar a execução de scripts
powershell_command = "Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force"

# Executa o comando PowerShell
subprocess.run(["powershell", "-Command", powershell_command], shell=True, check=True)

# Constants for the Windows API to create a restore point
SMGR_CREATE = 0x100
SMGR_CONFIRM = 0x200
SMGR_AUTO = 0x400
SMGR_NOCHANGE = 0x800
SMGR_NORESTORE = 0x1000
SMGR_NOTSUPPORTED = 0x2000
SMGR_LOCK = 0x4000
SMGR_UNLOCK = 0x8000
SMGR_NOSMPAGEFILE = 0x10000

class WelcomeDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        super(WelcomeDialog, self).__init__(parent, id, title)

        panel = wx.Panel(self)

        # Welcome text in the dialog box
        welcome_text = wx.StaticText(panel, -1, "Hi, we're glad you want to try our program!")
        disclaimer_text = wx.StaticText(panel, -1, "Remember that all changes are made by you and we are not responsible for any issues.")
        restore_text = wx.StaticText(panel, -1, "Before doing anything, create a restore point on your PC to avoid any problems.")

        # "Ok, I want to continue" button in the dialog box
        ok_button = wx.Button(panel, label="Okay, I want to continue")
        ok_button.Bind(wx.EVT_BUTTON, self.on_ok)

        # Dialog box layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(welcome_text, 0, wx.ALL, 10)
        sizer.Add(disclaimer_text, 0, wx.ALL, 10)
        sizer.Add(restore_text, 0, wx.ALL, 10)
        sizer.Add(ok_button, 0, wx.CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        super(MyFrame, self).__init__(parent, id, title, size=(400, 300))

        panel = wx.Panel(self)

        # Empty list
        self.lista_de_comandos = wx.ListCtrl(panel, -1, style=wx.LC_REPORT)
        self.lista_de_comandos.InsertColumn(0, "Name", width=100)
        self.lista_de_comandos.InsertColumn(1, "Description", width=150)
        self.lista_de_comandos.InsertColumn(2, "Command", width=200)
        self.lista_de_comandos.InsertColumn(3, "Type", width=100)

        # Create the "Add Commands" menu
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        add_command_item = file_menu.Append(wx.ID_ANY, "Add Commands", "Add a new command")
        self.Bind(wx.EVT_MENU, self.on_add_command, add_command_item)
        menu_bar.Append(file_menu, "Commands")

        # Create the "Tools" menu and add items
        tools_menu = wx.Menu()
        open_github_repo_item = tools_menu.Append(wx.ID_ANY, "Open the repository on GitHub", "Open the repository on GitHub")
        download_latest_github_item = tools_menu.Append(wx.ID_ANY, "Download Latest Version from GitHub", "Download Latest Version from GitHub")
        create_restore_point_item = tools_menu.Append(wx.ID_ANY, "Create Restore Point", "Create a system restore point")
        sort_commands_item = tools_menu.Append(wx.ID_ANY, "Sort Commands", "Sort commands alphabetically")
        check_updates_item = tools_menu.Append(wx.ID_ANY, "Check updates", "Check for updates and close Aurora")
        self.Bind(wx.EVT_MENU, self.open_github_repo, open_github_repo_item)
        self.Bind(wx.EVT_MENU, self.download_latest_github, download_latest_github_item)
        self.Bind(wx.EVT_MENU, self.create_system_restore_point, create_restore_point_item)
        self.Bind(wx.EVT_MENU, self.sort_commands, sort_commands_item)
        self.Bind(wx.EVT_MENU, self.check_updates, check_updates_item)
        menu_bar.Append(tools_menu, "Tools")
        self.SetMenuBar(menu_bar)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lista_de_comandos, 1, wx.EXPAND | wx.ALL, 10)
        panel.SetSizer(sizer)

        # Bind for Enter or Space key in the command list
        self.lista_de_comandos.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_execute_command)

        # Bind the EVT_CONTEXT_MENU event
        self.lista_de_comandos.Bind(wx.EVT_CONTEXT_MENU, self.on_context_menu)

        # Load commands from the file
        self.commands = load_commands()

        # Populate the command list
        for command in self.commands:
            self.add_command_to_list(command)

    def on_execute_command(self, event):
        # Get the selected command in the list
        selected_item = self.lista_de_comandos.GetFirstSelected()
        if selected_item >= 0:
            cmd = self.lista_de_comandos.GetItemText(selected_item, col=2)
            type = self.lista_de_comandos.GetItemText(selected_item, col=3)
            # Execute the command
            self.run_command(cmd, type)

    def on_add_command(self, event):
        # Open the dialog to add commands
        dlg = AddCommandDialog(self, -1, "Add Commands")
        result = dlg.ShowModal()
        if result == wx.ID_OK:
            name = dlg.name_text.GetValue()
            desc = dlg.desc_text.GetValue()
            cmd = dlg.cmd_text.GetValue()
            type = dlg.type_combo.GetValue()

            # Add the command to the list
            command = {"name": name, "desc": desc, "cmd": cmd, "type": type}
            self.commands.append(command)
            self.add_command_to_list(command)
            # Save the commands to the file
            save_commands(self.commands)

        dlg.Destroy()

    def add_command_to_list(self, command):
        index = self.lista_de_comandos.InsertItem(self.lista_de_comandos.GetItemCount(), command["name"])
        self.lista_de_comandos.SetItem(index, 1, command["desc"])
        self.lista_de_comandos.SetItem(index, 2, command["cmd"])
        self.lista_de_comandos.SetItem(index, 3, command["type"])

    def run_command(self, command, type):
        try:
            if "CMD" in type.upper():
                # Execute the CMD command and capture the output
                result = subprocess.run(["cmd", "/c", command], shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            elif "POWERSHELL" in type.upper():
                # Execute the PowerShell command and capture the output
                result = subprocess.run(["powershell", "-Command", command], shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            else:
                print("Unsupported command type:", type)
                return

            # Display the output in a dialog box
            output_dialog = OutputDialog(self, -1, "Command Result", result.stdout)
            output_dialog.ShowModal()

        except subprocess.CalledProcessError as e:
            # If an error occurs while executing the command, display the error output in a dialog box
            output_dialog = OutputDialog(self, -1, "Error Executing Command", e.stderr)
            output_dialog.ShowModal()
        except Exception as e:
            print("Error executing command:", e)

    def open_github_repo(self, event):
        # GitHub repo URL
        github_url = "https://github.com/azurejoga/Aurora-Windows-Optimizer"
        webbrowser.open(github_url)

    def download_latest_github(self, event):
        # URL to download the latest version from GitHub
        download_url = "https://github.com/azurejoga/Aurora-Windows-Optimizer/releases"
        webbrowser.open(download_url)

    def create_system_restore_point(self, event):
        # Open a dialog to enter the description for the restore point
        description = wx.GetTextFromUser("Enter a description for the restore point:", "Create Restore Point")
        if description:
            create_system_restore_point(description)

    def sort_commands(self, event):
        # Sort the commands in alphabetical order
        self.lista_de_comandos.DeleteAllItems()
        self.commands.sort(key=lambda x: x["name"])
        for command in self.commands:
            self.add_command_to_list(command)

    def create_context_menu(self):
        menu = wx.Menu()

        edit_item = wx.MenuItem(menu, wx.ID_ANY, "edit")
        self.Bind(wx.EVT_MENU, self.on_edit_command, edit_item)
        menu.Append(edit_item)

        remove_item = wx.MenuItem(menu, wx.ID_ANY, "Remove command")
        self.Bind(wx.EVT_MENU, self.on_remove_command, remove_item)
        menu.Append(remove_item)

        move_to_top_item = wx.MenuItem(menu, wx.ID_ANY, "Move to Top")
        self.Bind(wx.EVT_MENU, self.move_command_to_top, move_to_top_item)
        menu.Append(move_to_top_item)

        move_to_bottom_item = wx.MenuItem(menu, wx.ID_ANY, "Move to End")
        self.Bind(wx.EVT_MENU, self.move_command_to_bottom, move_to_bottom_item)
        menu.Append(move_to_bottom_item)

        return menu

    def on_context_menu(self, event):
        selected_item = self.lista_de_comandos.GetFirstSelected()
        if selected_item >= 0:
            menu = self.create_context_menu()
            self.PopupMenu(menu)
            menu.Destroy()

    def on_edit_command(self, event):
        selected_item = self.lista_de_comandos.GetFirstSelected()
        if selected_item >= 0:
            # Get details of the selected command
            name = self.lista_de_comandos.GetItemText(selected_item, col=0)
            desc = self.lista_de_comandos.GetItemText(selected_item, col=1)
            cmd = self.lista_de_comandos.GetItemText(selected_item, col=2)
            type = self.lista_de_comandos.GetItemText(selected_item, col=3)

            # Use the same dialog box for editing
            dlg = AddCommandDialog(self, -1, "Edit Command")
            dlg.name_text.SetValue(name)
            dlg.desc_text.SetValue(desc)
            dlg.cmd_text.SetValue(cmd)
            dlg.type_combo.SetValue(type)

            result = dlg.ShowModal()
            if result == wx.ID_OK:
                # Update the details of the command in the list
                updated_name = dlg.name_text.GetValue()
                updated_desc = dlg.desc_text.GetValue()
                updated_cmd = dlg.cmd_text.GetValue()
                updated_type = dlg.type_combo.GetValue()

                self.lista_de_comandos.SetItem(selected_item, 0, updated_name)
                self.lista_de_comandos.SetItem(selected_item, 1, updated_desc)
                self.lista_de_comandos.SetItem(selected_item, 2, updated_cmd)
                self.lista_de_comandos.SetItem(selected_item, 3, updated_type)

                # Update the details of the command in the list of commands
                self.commands[selected_item]["name"] = updated_name
                self.commands[selected_item]["desc"] = updated_desc
                self.commands[selected_item]["cmd"] = updated_cmd
                self.commands[selected_item]["type"] = updated_type

                # Save the changes to the file
                save_commands(self.commands)

            dlg.Destroy()

    def on_remove_command(self, event):
        selected_item = self.lista_de_comandos.GetFirstSelected()
        if selected_item >= 0:
            # Remove the command from the list and from the display
            del self.commands[selected_item]
            self.lista_de_comandos.DeleteItem(selected_item)
            # Save the changes to the file
            save_commands(self.commands)

    def check_updates(self, event):
        subprocess.run(["update.exe"], shell=True)



    def move_command_to_top(self, event):
        selected_item = self.lista_de_comandos.GetFirstSelected()
        if selected_item > 0:
            # Move the command to the top of the list
            self.commands.insert(0, self.commands.pop(selected_item))
            self.lista_de_comandos.DeleteAllItems()
            for command in self.commands:
                self.add_command_to_list(command)
            self.lista_de_comandos.Select(0)

    def move_command_to_bottom(self, event):
        selected_item = self.lista_de_comandos.GetFirstSelected()
        if selected_item >= 0 and selected_item < len(self.commands) - 1:
            # Move the command to the end of the list
            self.commands.append(self.commands.pop(selected_item))
            self.lista_de_comandos.DeleteAllItems()
            for command in self.commands:
                self.add_command_to_list(command)
            self.lista_de_comandos.Select(len(self.commands) - 1)

class AddCommandDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        super(AddCommandDialog, self).__init__(parent, id, title)

        panel = wx.Panel(self)

        # Add elements for entering name, description, command, and command type
        name_label = wx.StaticText(panel, -1, "Name:")
        self.name_text = wx.TextCtrl(panel, -1, "")

        desc_label = wx.StaticText(panel, -1, "Description:")
        self.desc_text = wx.TextCtrl(panel, -1, "")

        cmd_label = wx.StaticText(panel, -1, "Command:")
        self.cmd_text = wx.TextCtrl(panel, -1, "", style=wx.TE_MULTILINE)  # Allows multiple lines

        type_label = wx.StaticText(panel, -1, "Command type")
        self.type_combo = wx.ComboBox(panel, -1, choices=["CMD", "Powershell"], style=wx.CB_READONLY)

        # "Ok" and "Cancel" buttons
        ok_button = wx.Button(panel, label="Ok")
        ok_button.Bind(wx.EVT_BUTTON, self.on_ok)

        cancel_button = wx.Button(panel, label="Cancel")
        cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)

        # Layout of the dialog box
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(name_label, 0, wx.ALL, 10)
        sizer.Add(self.name_text, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(desc_label, 0, wx.ALL, 10)
        sizer.Add(self.desc_text, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(cmd_label, 0, wx.ALL, 10)
        sizer.Add(self.cmd_text, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(type_label, 0, wx.ALL, 10)
        sizer.Add(self.type_combo, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(ok_button, 0, wx.CENTER | wx.ALL, 10)
        sizer.Add(cancel_button, 0, wx.CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)

class OutputDialog(wx.Dialog):
    def __init__(self, parent, id, title, output):
        super(OutputDialog, self).__init__(parent, id, title, size=(400, 300))

        panel = wx.Panel(self)

        # Command output text
        if output:
            output_text = wx.TextCtrl(panel, -1, value=output.strip(), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.VSCROLL)
        else:
            output_text = wx.TextCtrl(panel, -1, value='The command was executed successfully!', style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.VSCROLL)

        # "Close" button
        close_button = wx.Button(panel, label="close")
        close_button.Bind(wx.EVT_BUTTON, self.on_close)

        # Layout of the dialog
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(output_text, 1, wx.EXPAND | wx.ALL, 10)
        sizer.Add(close_button, 0, wx.CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)

    def on_close(self, event):
        self.EndModal(wx.ID_OK)

def save_commands(commands):
    try:
        with open("commands", "wb") as file:
            pickle.dump(commands, file)
    except Exception as e:
        print("Erro ao salvar comandos:", e)

def load_commands():
    try:
        with open("commands", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        print("Erro ao carregar comandos:", e)
        return []

def create_system_restore_point(description):
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "powershell.exe", "Checkpoint-Computer -Description '{}'".format(description), "", 1)
        wx.MessageBox("Restore point created successfully!", "Restoration point", wx.OK | wx.ICON_INFORMATION)
    except Exception as e:
        wx.MessageBox("Error creating restore point:\n" + str(e), "Erro de Ponto de Restauração", wx.OK | wx.ICON_ERROR)

app = wx.App()

# Display the initial dialog box
dlg = WelcomeDialog(None, -1, "Welcome to Aurora")
result = dlg.ShowModal()
dlg.Destroy()

if result == wx.ID_OK:
    frame = MyFrame(None, -1, "Aurora, windows optimizer™")
    frame.Show()

app.MainLoop()
