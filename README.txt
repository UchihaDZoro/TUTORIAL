# Offline Malware Simulation - "Calculator with Monitoring and Persistence"

This repository contains a simulation of a calculator application with hidden, offline file-monitoring malware capabilities. This is designed purely for educational purposes to demonstrate basic malware functions like persistence, file monitoring, and registry modification. The project is isolated and runs only on the local machine, without any network or remote components.

---

## 📂 Project Contents

### Files and Directories

- **`Calc.py`**: The main calculator application, which runs `startup.exe` on launch to initiate hidden monitoring.
- **`startup.py`**: Launches and registers hidden executables (`malware1.exe` and `malware2.exe`) in the Windows startup registry to ensure they run on system reboot.
- **`malware1.py`**: Monitors specific folders on the C drive for any new or modified files, copying them to a "New Files C Drive" directory.
- **`malware2.py`**: Monitors additional drives (e.g., D, E, F, G, H) for new or modified files, copying them to a separate folder named "New Files For All Drives Except C."
- **`setup.py`**: Used to convert the Python scripts into executables with `py2exe`, creating `.exe` files that avoid detection by Windows Defender.

---

## 📝 Project Overview

This example application is a basic calculator that secretly performs the following operations when launched:

1. **File Monitoring on Specific Drives**: Tracks new or modified files in user folders on the C drive and other specified drives.
2. **Persistence Through Registry Modification**: Registers hidden malware executables in the Windows registry so they start automatically when the system reboots.
3. **Offline File Storage**: Copies monitored files to directories on the C drive for local storage instead of transmitting over a network.

> ⚠️ **Warning**: This project is strictly for educational use. Unauthorized use, distribution, or modification of this code is illegal and unethical. This code operates offline to prevent network-based data transfer, making it suitable for isolated, controlled environments only.

---

## 🛠️ Program Details

### 1. Calculator Application (`Calc.py`)
- **Description**: A graphical calculator created with Python's `tkinter` library.
- **Functionality**: Basic calculator functions with buttons and an entry field. When launched, it also initiates `startup.exe` to start the malware processes in the background.

### 2. C Drive Monitoring Program (`malware1.py`)
- **Description**: Monitors user folders (e.g., Desktop, Downloads) on the C drive for new or modified files.
- **Execution**: Runs in the background, detects file events, and copies detected files to the folder `"New Files C Drive"` on the C drive.
- **Excluded Folders**: Ignores system directories like `AppData` and `Roaming` to avoid permission errors.

### 3. Other Drives Monitoring Program (`malware2.py`)
- **Description**: Monitors additional drives (e.g., D, E, F, G, H) for new or modified files.
- **Execution**: Runs in the background, copying files to `"New Files For all Drives Except C"` on the C drive.
- **Separated Execution**: Runs as a separate process from `malware1.py` to avoid conflicts.

### 4. Startup Program (`startup.py`)
- **Description**: Registers `malware1.exe` and `malware2.exe` in the Windows registry to ensure they execute on startup.
- **Registry Path**:
  ```
  Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
  ```
- **Execution**: Ensures persistence by adding registry entries for malware startup.

### 5. Executable Conversion Script (`setup.py`)
- **Description**: Converts Python scripts into `.exe` files using `py2exe`, minimizing detection by Windows Defender.

---

## 🚀 Getting Started

1. **Download and Extract the ZIP File**: Unzip `Calculator.zip` to access the executable files.
2. **Run the Calculator**: Launch `Calc.exe` to open the calculator application and start the background monitoring processes.
3. **File Monitoring**: The malware executables will track specified directories and copy new or modified files into designated folders on the C drive.

---

## 🔧 Requirements

Ensure the following are installed in your environment:

- **Python 3.7+**
- **watchdog** (for monitoring file events)
  ```bash
  pip install watchdog
  ```
- **py2exe** (used for conversion in `setup.py`)
  ```bash
  pip install py2exe
  ```

---

## 📂 Monitored Directories

1. **C Drive Monitoring**: `malware1.exe` monitors selected user folders on the C drive, like Desktop, Documents, and Downloads.
2. **Additional Drives Monitoring**: `malware2.exe` monitors drives other than C (e.g., D, E, F, etc.) for any new or modified files, copying them into a dedicated C drive folder.

---

## ❌ Stopping the Malware Programs

To stop these programs and remove them from startup:

1. **Remove from Windows Registry**:
   - Open **Registry Editor** by typing `regedit` in the Windows search bar.
   - Navigate to:
     ```
     Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
     ```
   - Delete the entries for `malware1` and `malware2`.

2. **End Background Processes**:
   - Open **Task Manager** and locate `malware1.exe` and `malware2.exe` under Background processes.
   - End these processes to halt file monitoring.

---

## ⚠️ Limitations and Considerations

- **Offline Only**: The project copies files locally without transmitting them to a remote server, making it suitable for offline educational purposes.
- **Storage Limitations**: Continuous file copying may consume significant disk space on the C drive, so monitor storage usage.
- **Bypassing Windows Defender**: `py2exe` was chosen to minimize detection. Other methods (e.g., `pyinstaller`, `pyarmor`) triggered Windows Defender.

---

## 💡 Educational Purposes Only

This code is provided solely for educational purposes to understand malware persistence techniques and directory monitoring. Unauthorized use or distribution of malware is illegal and unethical. Always exercise caution and use responsibly in controlled, isolated environments.

---

## 📄 License

This project is licensed for **educational use only**. Redistribution, modification, or deployment of this code for malicious purposes is strictly prohibited and subject to legal penalties.

---
```

### Explanation:

1. **Structured Format**: Follows the requested format with clear sections: Project Contents, Overview, Program Details, Getting Started, Requirements, Monitored Directories, Stopping the Programs, Limitations, Educational Use Notice, and License.
2. **Security Notice**: Emphasizes that the project is for educational use only.
3. **Technical Details**: Includes steps for stopping the malware and details on registry modification.
4. **Requirements**: Lists necessary packages and commands for installation.
5. **Execution Instructions**: Provides clear steps on how to run and manage the malware simulation.

Feel free to customize it with any additional project-specific information or links.
