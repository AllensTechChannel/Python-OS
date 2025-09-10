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
        if os.path.exists("pythonplayer.py"):
            subprocess.run([sys.executable, "pythonplayer.py"])
        else:
            show_message("File Not Found", "pythonplayer.py not found.")
        time.sleep(1)
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")

def launch_internet_explorer(original_dir):
    clear()
    try:
        os.chdir(os.path.join("..", "Programs", "Internet Explorer"))
        if os.path.exists("Internet-Explorer.py"):
            subprocess.run([sys.executable, "Internet-Explorer.py"])
        else:
            show_message("File Not Found", "Internet-Explorer.py not found.")
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

def launch_clock(original_dir):
    clear()
    try:
        os.chdir(os.path.join("..", "Programs", "clock"))
        if os.path.exists("clock.py"):
            subprocess.run([sys.executable, "clock.py"])
        else:
            show_message("File Not Found", "Clock.py not found.")
        time.sleep(1)
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")
def launch_alarm(original_dir):
    clear()
    try:
        os.chdir(os.path.join("..", "Programs", "alarm"))
        if os.path.exists("alarm.py"):
            subprocess.run([sys.executable, "alarm.py"])
        else:
            show_message("File Not Found", "alarm.py not found.")
        time.sleep(1)
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")   

   

def launch_paint(original_dir):
    clear()
    try:
        os.chdir(os.path.join("..", "Programs", "PyPaint"))
        if os.path.exists("pypaint.py"):
            subprocess.run([sys.executable, "pypaint.py"])
        else:
            show_message("File Not Found", "pypaint.py not found.")
        time.sleep(1)
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")
def launch_FilePilot(original_dir):
    clear()
    try:
        os.chdir(os.path.join("..", "Programs", "FilePilot", "src"))
        if os.path.exists("main.py"):
            subprocess.run([sys.executable, "main.py"])
        else:
            show_message("File Not Found", "main.py not found.")
        time.sleep(1)
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")
def launch_System_Programs(original_dir):
    clear()
    try:
        os.chdir(os.path.join("..", "Programs", "System Programs"))
        if os.path.exists("Program-select.py"):
            subprocess.run([sys.executable, "Program-select.py"])
        else:
            show_message("File Not Found", "Program-select.py not found.")
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
    print("4. System Programs")
    print("5. Clock")
    print("6. Digital Alarm Clock")
    print("7. FilePilot (File Explorer)")
    print("8. PythonPaint")
    print("9. Exit")

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
        elif choice == "5":
            launch_clock(original_dir)
        elif choice  == "6":
            launch_alarm(original_dir)
        elif choice == "7": 
            launch_FilePilot(original_dir)
        elif choice == "8":
            launch_paint(original_dir)
        elif choice in ("9", "exit"):
            print("Exiting...")
            break
        else:
            show_message("Invalid Choice", "Invalid choice or unimplemented feature.")
            play_sound('error-beep.wav')
            time.sleep(1)

if __name__ == "__main__":
    main()
