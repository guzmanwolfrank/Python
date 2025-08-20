# Program Uninstaller

A user-friendly Python application with a tkinter GUI for safely uninstalling programs on Windows systems. This tool provides a clean interface to manage installed software using Windows' built-in uninstallation mechanisms.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- 🔍 **Smart Program Discovery** - Automatically scans Windows registry to find all installed programs
- 🔎 **Real-time Search** - Instantly filter through hundreds of installed programs
- 📊 **Detailed Information** - View program details including publisher, version, and install location
- 🛡️ **Safe Uninstallation** - Uses Windows' official uninstall commands, not file deletion
- 🎨 **Modern GUI** - Clean, intuitive interface built with tkinter
- ⚡ **Multi-threaded Loading** - Responsive UI with background program scanning
- ✅ **Confirmation Dialogs** - Prevents accidental uninstallations
- 🔄 **Auto-refresh** - Easy program list updates after installations/uninstallations

## Screenshots

### Main Interface
The main window displays all installed programs in an organized, searchable list:
- Program names with publisher and version information
- Real-time search functionality
- Clean, modern interface

### Program Information
Detailed view showing:
- Full program name and publisher
- Version information
- Installation location
- Uninstall command details

## Requirements

- **Operating System**: Windows 7/8/10/11
- **Python**: 3.7 or higher
- **Modules**: All required modules are part of Python's standard library
  - `tkinter` (GUI framework)
  - `winreg` (Windows registry access)
  - `subprocess` (Process execution)
  - `threading` (Background operations)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/program-uninstaller.git
   cd program-uninstaller
   ```

2. **Ensure Python is installed**:
   ```bash
   python --version
   ```
   
3. **Run the application**:
   ```bash
   python program_uninstaller.py
   ```

## Usage

### Getting Started

1. **Launch the Application**
   ```bash
   python program_uninstaller.py
   ```

2. **Wait for Program Loading**
   - The application will automatically scan your system for installed programs
   - This may take a few moments depending on the number of installed programs

3. **Browse or Search Programs**
   - Use the search box to quickly find specific programs
   - Browse the full list using the scroll bar

### Uninstalling Programs

1. **Select a Program**
   - Click on any program in the list to select it

2. **View Program Information** (Optional)
   - Click "Program Info" to see detailed information about the selected program

3. **Uninstall**
   - Click "Uninstall Selected"
   - Confirm the action in the dialog box
   - Follow any additional prompts that may appear

4. **Refresh List** (Optional)
   - Click "Refresh List" to update the program list after changes

### Search and Filter

- **Real-time Search**: Type in the search box to instantly filter programs
- **Search by Name**: Find programs by their display name
- **Search by Publisher**: Find programs by their publisher/company name

## How It Works

### Registry Scanning
The application scans multiple Windows registry locations:
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`
- `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall`
- `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`

### Safe Uninstallation Process
1. Retrieves the official uninstall command from Windows registry
2. Executes the program's registered uninstall command
3. Does NOT manually delete files or folders
4. Relies on the software's own uninstallation process

### Data Filtering
- Automatically filters out system components and updates
- Excludes Microsoft Visual C++ redistributables and .NET frameworks
- Hides Windows security updates and hotfixes

## Safety Features

- **Registry-based Discovery**: Only shows officially registered programs
- **Official Uninstall Commands**: Uses each program's designated uninstall method
- **Confirmation Dialogs**: Requires user confirmation before uninstalling
- **No File Deletion**: Never manually deletes program files
- **Error Handling**: Gracefully handles missing or invalid uninstall commands

## Troubleshooting

### Common Issues

**"No uninstall command found"**
- Some programs may not have proper uninstall commands registered
- Try uninstalling through Windows' "Add or Remove Programs" instead

**"Access Denied" or Permission Errors**
- Some programs require administrator privileges
- Try running the application as administrator:
  - Right-click on Command Prompt
  - Select "Run as administrator"
  - Navigate to the program folder and run: `python program_uninstaller.py`

**Program Not Listed**
- Click "Refresh List" to reload the program database
- Some portable applications may not appear as they don't register in Windows
- Microsoft Store apps are not included (use Windows Settings to manage them)

**Uninstallation Doesn't Complete**
- Some programs may show their own uninstall wizard
- Follow the prompts in the program's uninstaller
- The application simply triggers the uninstall process

### System Requirements Issues

**Windows Only**
- This application only works on Windows systems
- Registry access is Windows-specific

**Python Version**
- Ensure you're using Python 3.7 or higher
- tkinter should be included with most Python installations

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes**
4. **Test thoroughly** on different Windows versions
5. **Submit a pull request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test on multiple Windows versions if possible
- Ensure error handling for edge cases

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

**Important**: This tool interacts with your system's installed programs. While it uses safe, official uninstall methods:

- Always create system backups before making major changes
- Some uninstallations cannot be reversed
- The developers are not responsible for any data loss or system issues
- Use at your own risk

## Acknowledgments

- Built with Python's tkinter for cross-Windows compatibility
- Uses Windows Registry API for safe program discovery
- Inspired by the need for a simple, clean program management tool

## Support

If you encounter issues or have questions:

1. Check the [Issues](https://github.com/yourusername/program-uninstaller/issues) page
2. Create a new issue with:
   - Your Windows version
   - Python version
   - Steps to reproduce the problem
   - Any error messages

---

**Made with ❤️ for Windows users who want a cleaner system management experience.**