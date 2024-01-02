import tkinter as tk
import os
import sys
import subprocess

class Calc:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.entry = tk.Entry(root, width=20, font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'AC', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button_text in buttons:
            tk.Button(root, text=button_text, width=5, height=2,
                      command=lambda text=button_text: self.click(text)).grid(row=row_val, column=col_val)
            col_val += 1

            if col_val > 3:
                col_val = 0
                row_val += 1

    def click(self, text):
        if text == 'AC':
            self.entry.delete(0, tk.END)
        elif text == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            new_text = self.entry.get() + text
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, new_text)


def run_exe(program_name):
    # Get the path to the directory where the script or executable is located
    script_path = get_current_directory()

    # Assuming the executable is in the same directory as the script or the compiled executable
    exe_path = os.path.join(script_path, f'{program_name}.exe')

    # Check if the executable file exists
    if os.path.isfile(exe_path):
        try:
            # Run the executable using subprocess.Popen
            subprocess.Popen([exe_path])
        except Exception as e:
            return
    else:
        return


# Get the path to the directory where the script or executable is located
def get_current_directory():
    if getattr(sys, 'frozen', False):
        # The application is frozen (compiled to exe)
        return os.path.dirname(sys.executable)
    else:
        # The script is running in a normal Python environment
        return os.path.dirname(os.path.realpath(__file__))


if __name__ == '__main__':
    current_directory = get_current_directory()
    run_exe('startup')
    root = tk.Tk()
    run = Calc(root)
    root.mainloop()
