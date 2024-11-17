# 📂 **Trojnanize Calc - "File monitoring malware"**

This repository contains a trojanized calculator application with hidden, offline file-monitoring malware capabilities. This is designed purely for educational purposes to demonstrate basic malware functions like persistence, file monitoring, and registry modification. The project is isolated and runs only on the local machine, without any network or remote components.

---

## 📝 **Application Overview:**

This application is designed as a simple calculator but contains hidden malicious features that actively monitor your system for new files. These files are copied to a new directory on the **C drive**. The malware operates offline, copying files locally instead of uploading them to a remote server. When users extract the contents, they find a directory containing the calculator app and several concealed programs, including hidden executables: **`startup.exe`**, **`malware1.exe`**, and **`malware2.exe`**.

- **Hidden Executables**: These files are hidden by default and will not be visible with normal settings. I chose not to rename the `.exe` files for ease of understanding.
- **Source Code Availability**: The raw `.py` files for all 4 executables are uploaded, so you can check the code. Additionally, a final malware package is uploaded in a ZIP file named **`Calculator.zip`**. To run the malware, download and unzip the file, then launch **`Calc.exe`**.

### **Malware Execution Flow:**

1. **Calculator Launch**:
   - Upon launching **`Calc.exe`**, it triggers **`startup.exe`**, which adds **`malware1.exe`** and **`malware2.exe`** to the Windows startup registry and starts them in the background.

2. **Separation of Monitoring Programs**:
   - The malware is divided into two distinct programs:
     - **`malware1.exe`**: Monitors the **C drive**, specifically user directories like Desktop, Downloads, etc.
     - **`malware2.exe`**: Monitors additional drives (e.g., D, E, F).
   - **Why Separate?**: Combining both into a single executable using if-else conditions was problematic due to Python's line-by-line interpretation, causing conflicts. Hence, they are split to run independently, reducing errors and improving efficiency.

3. **Offline File Storage**:
   - For demonstration purposes, the malware is configured to operate offline. Instead of uploading files to a server, it copies detected files to newly created directories on the C drive.

### **Limitations**:

- **Storage Hazard**: Since files are copied locally to the C drive, there is a risk of significant storage consumption over time.
- **Selective Monitoring**: The malware monitors specific user folders (e.g., `Desktop`, `Downloads`, `Documents`) to avoid permission issues with system files.

### **Bypassing Windows Defender**:

- **Executable Conversion**: The malware was converted to `.exe` files using **`py2exe`**. Other methods like **`pyarmor`**, **`pyinstaller`**, and **`nuitka`** and many more were also used but they proved to be unsuccessful by triggering Windows Defender alerts.
- **Setup Script**: The Python script used for conversion (`setup.py`) is also included. A failed compilation attempt using **`pyinstaller`** is provided in a ZIP file named **`Failed Exe.zip`** for reference.

> ⚠️ **Important**: This project is for educational purposes only. Unauthorized use, distribution, or modification of this code is illegal and unethical. It operates offline to prevent data transmission but can still occupy disk space if left running and act as a Disk Bomb causing the system to slow down, malfunction, or crash due to insufficient disk space.

---

## 🚀 **Getting Started**:

1. **Download and Extract**:
   - Unzip **`Calculator.zip`** to access the executable files.

2. **Run the Calculator**:
   - Launch **`Calc.exe`** to open the calculator and start the hidden monitoring processes.

3. **File Monitoring**:
   - **`malware1.exe`** and **`malware2.exe`** will start in the background, monitoring specified directories and copying files to new folders on the C drive.

---

## 🛠️ **Stopping the Malware Programs**:

1. **Remove from Windows Registry**:
   - Open **Registry Editor** (`regedit`).
   - Navigate to:
     ```
     Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
     ```
   - Delete entries for **`malware1.exe`** and **`malware2.exe`**.

2. **End Background Processes**:
   - Open **Task Manager** and end processes for **`malware1.exe`** and **`malware2.exe`**.
   - Failure to remove these entries will cause the malware to run automatically on system boot.

---

## 🔧 **Requirements**:

- **Python 3.7+**
- **watchdog** (for file monitoring):
  ```bash
  pip install watchdog
  ```
- **py2exe** (for converting scripts to executables):
  ```bash
  pip install py2exe
  ```

---

## 📂 **Monitored Directories**:

1. **C Drive Monitoring**:
   - **`malware1.exe`** monitors user folders like `Desktop`, `Documents`, `Downloads`, `Music`, `Pictures`, `Videos`, and `OneDrive`.
   - System directories like **`AppData`** are excluded to avoid permission errors.

2. **Additional Drives Monitoring**:
   - **`malware2.exe`** monitors other drives (e.g., D, E, F, etc.), copying new or modified files to a designated folder on the C drive.

---

## ⚠️ **Educational Purposes Only**:

This code is provided solely for educational purposes to understand malware persistence techniques and file monitoring. Unauthorized use or distribution is illegal and unethical. Always use this project responsibly in controlled, isolated environments.
