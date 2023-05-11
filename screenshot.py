import pyautogui
import tkinter as tk

def take_sc(output_path):
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(output_path)
        print("Tangkapan layar berhasil disimpan di", output_path)
    except Exception as e:
        print("Maaf! Gagal melakukan tangkapan layar:", str(e))

output_file = "D:\layar.png"

root = tk.Tk()
root.title("Tangkap Layar")
root.geometry("300x100")

screenshot_button = tk.Button(root, text="Tangkap Layar!", command=take_sc(output_file))
screenshot_button.pack(pady=30)

root.mainloop()