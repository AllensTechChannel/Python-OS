import os
import sys
import time
import subprocess
import ctypes

# Show a Windows message box
def show_message(title, text, style=0x10):  # 0x10 = MB_ICONERROR
    ctypes.windll.user32.MessageBoxW(0, text, title, style)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_sound(filename):
    path = os.path.join(os.getcwd(), 'media', filename)
    if os.path.exists(path):
        import winsound
        winsound.PlaySound(path, winsound.SND_FILENAME)
    else:
        show_message("Missing File", f"Sound file not found:\n{path}")

def launch_pythonplayer(original_dir):
    clear()
    try:
        os.chdir(os.path.join("..", "Programs", "pythonplayer"))
        bat_path = "playsound-install.bat"
        if os.path.exists(bat_path):
            try:
                os.startfile(bat_path)
            except OSError as e:
                show_message("Launch Error", str(e))
        else:
            show_message("File Not Found", f"{bat_path} not found.")
        time.sleep(1)
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")

def launch_internet_explorer(original_dir):
    clear()
    try:
        os.chdir(os.path.join("..", "Programs", "Internet Explorer"))
        bat_path = "Webview-install.bat"
        if os.path.exists(bat_path):
            try:
                os.startfile(bat_path)
            except OSError as e:
                show_message("Launch Error", str(e))
        else:
            show_message("File Not Found", f"{bat_path} not found.")
        time.sleep(1)
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")

def launch_txtpad(original_dir):
    clear()
    try:
        os.chdir(os.path.join("..", "Programs", "txtpad"))
        if os.path.exists("txtpad.py"):
            subprocess.run([sys.executable, "txtpad.py"])
        else:
            show_message("File Not Found", "txtpad.py not found.")
        time.sleep(1)
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...") 

def launch_Computer_Monitor(original_dir):
    clear()
    try:
        os.chdir(os.path.join("..", "Programs", "Computer-Monitor"))
        if os.path.exists("Computer-Monitor.py"):
            subprocess.run([sys.executable, "Computer-Monitor.py"])
        else:
            show_message("File Not Found", "Computer-Monitor.py not found.")
        time.sleep(1)
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")     

def show_menu():
    print("\nMenu:")
    print("1. PythonPlayer (Media Player)")
    print("2. Internet Explorer")
    print("3. txtpad (Text Editor)")
    print("4. Computer Monitor")
    print("5. Exit")

def main():
    original_dir = os.getcwd()
    while True:
        clear()
        show_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            launch_pythonplayer(original_dir)
        elif choice == "2":
            launch_internet_explorer(original_dir)
        elif choice == "3":
            launch_txtpad(original_dir)   
        elif choice == "4":
            launch_Computer_Monitor(original_dir)
        elif choice in ("5", "exit"):
            print("Exiting...")
            break
        else:
            show_message("Invalid Choice", "Invalid choice or unimplemented feature.")
            play_sound('error-beep.wav')
            time.sleep(1)

if __name__ == "__main__":
    main()
