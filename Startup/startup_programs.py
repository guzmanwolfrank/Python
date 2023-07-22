import winreg

# Open the "Run" key of the registry where startup programs are listed
run_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)

# Get the number of values (programs) in the "Run" key
num_values = winreg.QueryInfoKey(run_key)[1]

# Print the name and path of each program in the "Run" key
print("List of programs that run on startup:")
for i in range(num_values):
    name, value, _ = winreg.EnumValue(run_key, i)
    print(f"{name}: {value}")

# Ask the user which programs to remove from startup
to_remove = input("Enter the names of the programs to remove from startup, separated by commas: ").split(",")

# Remove the selected programs from the "Run" key
for program in to_remove:
    try:
        winreg.DeleteValue(run_key, program.strip())
        print(f"{program.strip()} has been removed from startup.")
    except FileNotFoundError:
        print(f"{program.strip()} is not in the list of programs that run on startup.")

# Close the "Run" key of the registry
winreg.CloseKey(run_key)
