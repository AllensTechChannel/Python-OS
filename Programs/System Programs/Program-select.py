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
        os.chdir(os.path.join("Computer-Monitor"))
        if os.path.exists("Computer-Monitor.py"):
            subprocess.run([sys.executable, "Computer-Monitor.py"])
        else:
            show_message("File Not Found", "pythonplayer.py not found.")
        time.sleep(1)
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")
def show_menu():
    print("\nMenu:")
    print("1. Computer Monitor")
    
def main():
    original_dir = os.getcwd()
    while True:
        clear()
        show_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            launch_pythonplayer(original_dir)
        
        elif choice in ("2", "exit"):
            print("Exiting...")
            break
        else:
            show_message("Invalid Choice", "Invalid choice or unimplemented feature.")
            play_sound('error-beep.wav')
            time.sleep(1)

if __name__ == "__main__":
    main()