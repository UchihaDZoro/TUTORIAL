Offline Malware Simulation - "Calculator with Monitoring and Persistence"

This repository contains a simulation of a calculator application with hidden, offline file-monitoring malware capabilities. This is designed purely for educational purposes to demonstrate basic malware functions like persistence, file monitoring, and registry modification. The project is isolated and runs only on the local machine, without any network or remote components.

---

Project Contents:

1. Calc.py:
   - The main calculator application, which runs `startup.exe` on launch to initiate hidden monitoring.

2. startup.py:
   - Launches and registers hidden executables (`malware1.exe` and `malware2.exe`) in the Windows startup registry to ensure they run on system reboot.

3. malware1.py:
   - Monitors specific folders on the C drive for any new or modified files, copying them to a "New Files C Drive" directory.

4. malware2.py:
   - Monitors additional drives (e.g., D, E, F, G, H) for new or modified files, copying them to a separate folder named "New Files For All Drives Except C."

5. setup.py:
   - Used to convert the Python scripts into executables with `py2exe`, creating `.exe` files that avoid detection by Windows Defender.

---

Project Overview:

This example application is a basic calculator that secretly performs the following operations when launched:

1. File Monitoring on Specific Drives:
   - Tracks new or modified files in user folders on the C drive and other specified drives.

2. Persistence Through Registry Modification:
   - Registers hidden malware executables in the Windows registry to ensure they start automatically when the system reboots.

3. Offline File Storage:
   - Copies monitored files to directories on the C drive for local storage instead of transmitting over a network.

Warning:
This project is strictly for educational use. Unauthorized use, distribution, or modification of this code is illegal and unethical. This code operates offline to prevent network-based data transfer, making it suitable for isolated, controlled environments only.

---

Program Details:

1. Calculator Application (Calc.py):
   - A graphical calculator created with Python's `tkinter` library.
   - Basic calculator functions with buttons and an entry field.
   - When launched, it initiates `startup.exe` to start the malware processes in the background.

2. C Drive Monitoring Program (malware1.py):
   - Monitors user folders (e.g., Desktop, Downloads) on the C drive for new or modified files.
   - Runs in the background and copies detected files to the folder "New Files C Drive."
   - Excludes system directories like `AppData` and `Roaming`.

3. Other Drives Monitoring Program (malware2.py):
   - Monitors drives (e.g., D, E, F, G, H) for new or modified files.
   - Runs as a separate process to avoid conflicts and copies files to "New Files For All Drives Except C."

4. Startup Program (startup.py):
   - Registers `malware1.exe` and `malware2.exe` in the Windows registry.
   - Registry Path: 
     Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run

5. Executable Conversion Script (setup.py):
   - Converts Python scripts into `.exe` files using `py2exe`.

---

Getting Started:

1. Download and Extract the ZIP File:
   - Unzip `Calculator.zip` to access the executable files.

2. Run the Calculator:
   - Launch `Calc.exe` to open the calculator application and start the background monitoring processes.

3. File Monitoring:
   - The malware executables will track specified directories and copy new or modified files into designated folders on the C drive.

---

Requirements:

- Python 3.7+
- watchdog (for monitoring file events)
  Install with: `pip install watchdog`
- py2exe (used for conversion in `setup.py`)
  Install with: `pip install py2exe`

---

Monitored Directories:

1. C Drive Monitoring:
   - `malware1.exe` monitors user folders like Desktop, Documents, and Downloads.

2. Additional Drives Monitoring:
   - `malware2.exe` monitors drives other than C (e.g., D, E, F) and copies detected files to a folder on the C drive.

---

Stopping the Malware Programs:

1. Remove from Windows Registry:
   - Open Registry Editor by typing `regedit` in the Windows search bar.
   - Navigate to: Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
   - Delete entries for `malware1` and `malware2`.

2. End Background Processes:
   - Open Task Manager, locate `malware1.exe` and `malware2.exe` under Background processes, and end these processes.

---

Limitations and Considerations:

1. Offline Only:
   - The project copies files locally without transmitting them to a remote server.

2. Storage Limitations:
   - Continuous file copying can consume disk space on the C drive.

3. Bypassing Windows Defender:
   - `py2exe` is used to minimize detection. Other methods may trigger Windows Defender alerts.

---

Educational Purposes Only:

This code is provided solely for educational purposes to understand malware persistence techniques and directory monitoring. Unauthorized use or distribution of malware is illegal and unethical. Always exercise caution and use responsibly in controlled, isolated environments.

---

License:

This project is licensed for educational use only. Redistribution, modification, or deployment of this code for malicious purposes is strictly prohibited and subject to legal penalties.

