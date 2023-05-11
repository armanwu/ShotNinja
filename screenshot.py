import pyautogui
import tkinter as tk
import tkinter.messagebox as messagebox
from datetime import datetime
import os

def take_ss():
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        output_dir = os.path.join(os.path.expanduser("~"), "Pictures")
        output_file = os.path.join(output_dir, f"ss_{timestamp}.png")
        screenshot = pyautogui.screenshot()
        screenshot.save(output_file)
        messagebox.showinfo("Done!", f"Screenshot saved successfully in {output_file}")
    except Exception as e:
        messagebox.showerror("Error!", "Failed to take screenshot:\n" + str(e))

root = tk.Tk()
root.title("Screenshot")
root.geometry("300x100")
root.resizable(False, False)

def button_click():
    take_ss()

ss_button = tk.Button(root, text="Take Screenshot!", command=button_click)
ss_button.pack(pady=30)

root.mainloop()