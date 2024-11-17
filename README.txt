# 📂 **Offline Malware Simulation - "Calculator with Monitoring and Persistence"**

This repository contains a simulation of a calculator application with hidden, offline file-monitoring malware capabilities. This is designed purely for educational purposes to demonstrate basic malware functions like persistence, file monitoring, and registry modification. The project is isolated and runs only on the local machine, without any network or remote components.

---

## 🗂️ **Project Contents:**

1. **`Calc.py`**:
   - The main calculator application, which runs **`startup.exe`** on launch to initiate hidden monitoring.

2. **`startup.py`**:
   - Launches and registers hidden executables (**`malware1.exe`** and **`malware2.exe`**) in the Windows startup registry to ensure they run on system reboot.

3. **`malware1.py`**:
   - Monitors specific folders on the **C drive** for any new or modified files, copying them to a folder named **"New Files C Drive"**.

4. **`malware2.py`**:
   - Monitors additional drives (e.g., **D, E, F, G, H**) for new or modified files, copying them to a folder named **"New Files For All Drives Except C"**.

5. **`setup.py`**:
   - Used to convert Python scripts into executables with **`py2exe`**, creating `.exe` files that minimize detection by Windows Defender.

---

## 📝 **Project Overview:**

This example application is a basic calculator that secretly performs the following operations when launched:

- **File Monitoring on Specific Drives**: Tracks new or modified files in user folders on the C drive and other specified drives.
- **Persistence Through Registry Modification**: Registers hidden malware executables in the Windows registry to ensure they start automatically when the system reboots.
- **Offline File Storage**: Copies monitored files to directories on the C drive for local storage instead of transmitting over a network.

> ⚠️ **Warning**: This project is strictly for educational use. Unauthorized use, distribution, or modification of this code is illegal and unethical. The code operates offline to prevent network-based data transfer, making it suitable for isolated, controlled environments only.

---

## 🛠️ **Program Details:**

### 1. **Calculator Application (`Calc.py`)**
   - A graphical calculator created with Python's **`tkinter`** library.
   - Provides basic calculator functions. On launch, it initiates **`startup.exe`** to start background monitoring processes.

### 2. **C Drive Monitoring Program (`malware1.py`)**
   - Monitors user folders (e.g., Desktop, Downloads) on the C drive.
   - Copies detected files to the **"New Files C Drive"** folder.
   - Excludes system directories like **`AppData`** to avoid permission errors.

### 3. **Other Drives Monitoring Program (`malware2.py`)**
   - Monitors drives (e.g., D, E, F, G, H) for new or modified files.
   - Copies detected files to **"New Files For All Drives Except C"**.
   - Runs as a separate process to prevent conflicts.

### 4. **Startup Program (`startup.py`)**
   - Registers **`malware1.exe`** and **`malware2.exe`** in the Windows registry.
   - **Registry Path**:
     ```
     Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
     ```

### 5. **Executable Conversion Script (`setup.py`)**
   - Converts Python scripts to `.exe` using **`py2exe`**.

---

## 🚀 **Getting Started:**

1. **Download and Extract**:
   - Unzip **`Calculator.zip`** to access executable files.

2. **Run the Calculator**:
   - Launch **`Calc.exe`** to open the calculator and start monitoring.

3. **File Monitoring**:
   - Background processes will track specified directories and copy new/modified files to C drive folders.

---

## 🔧 **Requirements:**

- **Python 3.7+**
- **watchdog** (for monitoring file events)
  ```bash
  pip install watchdog
  ```
- **py2exe** (for converting scripts to executables)
  ```bash
  pip install py2exe
  ```

---

## 📂 **Monitored Directories:**

1. **C Drive Monitoring**:
   - **`malware1.exe`** monitors user folders like Desktop, Documents, and Downloads.

2. **Additional Drives Monitoring**:
   - **`malware2.exe`** monitors drives other than C (e.g., D, E, F).

---

## ❌ **Stopping the Malware Programs:**

1. **Remove from Windows Registry**:
   - Open **Registry Editor** (`regedit`).
   - Navigate to:
     ```
     Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
     ```
   - Delete entries for **`malware1`** and **`malware2`**.

2. **End Background Processes**:
   - Open **Task Manager** and end processes for **`malware1.exe`** and **`malware2.exe`**.

---

## ⚠️ **Limitations and Considerations:**

- **Offline Only**:
  - No network transmission; local file copying only.
- **Storage Limitations**:
  - Continuous copying may consume disk space on the C drive.
- **Bypassing Windows Defender**:
  - **`py2exe`** is used to reduce detection.

---

## 💡 **Educational Purposes Only:**

This code is intended solely for educational purposes to understand malware persistence techniques and file monitoring. Unauthorized use, distribution, or modification of this code is illegal and unethical. Use responsibly in controlled environments.

---

