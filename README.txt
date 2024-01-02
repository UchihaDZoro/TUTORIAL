It is an application designed as a calculator, but it contains malicious features that actively monitor your system and transmit any new files to a remote server. The malware is designed to opreate offline and coping files locally instead of uploading them to a remote server. When the user extracts the contents, it reveals a directory containing the calculator app and several concealed programs, including few hidden ones "startup.exe," "malware1.exe," and "malware2.exe". 

given exe are hidden and won't be visible with normal setting. I choose not to rename the exe for ease of understanding,
raw .py files for all 4 exe are uploaded so you can check the code. and a final malware uploaded in a zip file name Calculator, to run it you'll have to run Calc.exe.

Upon launching the calculator, it triggers the "startup.exe" application, which, in turn, adds the malware (malware1.exe, malware2.exe) to the startup registry and also launch it in background. The malware is divided into two distinct programs one for the C drive(malware1.exe) and another for other drives(malware2.exe), which keeps it from running into errors and allowing it to monitor them for new files created by the user and not the system. Attempts to consolidate the malware into a single executable using if-else conditions pose a challenge, as Python, being an interpreter, processes code line by line, resulting in a loop and monitors either C drive or other.

For demonstration purposes, instead of uploading files to a remote server, the malware is configured to operates offline and copy files to a newly created directories on the C drive. Notably, the malware has limitations, such as selectively monitoring specified directories on the C drive, including ['Desktop', 'Downloads', 'Music', 'Pictures', 'Videos', 'OneDrive', 'Favorites', 'Documents'] because of permission errors, system files, etc. On other drives, it monitors all directories.

for bypassing windows defender I've used py2exe for converting it to exe. I've also tried other compiler and obfuscator like pyarmor, pyinstaller and nuitka but they were detected as threat by windows defender. I've also uploaded python script i used with py2exe named setup.py, and also uploaded a zip file name failed exe it contains exe converted by pyinstaller 

It's important to emphasize that this example is kept offline for educational purposes and don't use it for malicious activities, eliminating concerns about data being uploaded to a remote server. However, be cautious, as if it is kept running it can still occupy a significant amount of space on your computer as the files are copied to C drive.

!!TO STOP THE MALWARE!!
Go to registory editor and go to following path(startup registory) and delete malware1.exe and mawalre2.exe. 
if no done properly malware will automatically run when ever system is booted

Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run

Go to task manager and background process and stop malware1.exe and mawalre2.exe
