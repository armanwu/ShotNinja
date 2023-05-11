import pyautogui

def take_sc(output_path):
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(output_path)
        print("Screenshot saved successfully in", output_path)
    except Exception as e:
        print("Sorry! Failed to take screenshot:", str(e))

output_file = "C:\screenshot.png"
take_sc(output_file)