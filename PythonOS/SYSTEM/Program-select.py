import os
import sys
import subprocess
import ctypes
import time
import os

def find_project_root():
    current = os.path.abspath(os.path.dirname(__file__))
    while current != os.path.dirname(current):  # until we reach the filesystem root
        if os.path.isdir(os.path.join(current, "PythonOS")):
            return current
        current = os.path.dirname(current)
    raise FileNotFoundError("Could not find project root containing 'PythonOS' folder")

ROOT_DIR = find_project_root()
print(f"[DEBUG] Project root detected as: {ROOT_DIR}")

# --- Base Paths ---
# Find the root folder (one level up from "Programs")
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def show_message(title, text, style=0x10):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_sound(filename):
    path = os.path.join(ROOT_DIR, 'media', filename)
    if os.path.exists(path):
        import winsound
        winsound.PlaySound(path, winsound.SND_FILENAME)
    else:
        show_message("Missing File", f"Sound file not found:\n{path}")

def launch_pythonplayer():
    clear()
    monitor_path = os.path.join("System Programs","Computer-Monitor","Computer-Monitor.py")
    print(f"[DEBUG] Looking for: {monitor_path}")
    if os.path.exists(monitor_path):
        subprocess.run([sys.executable, monitor_path])
    else:
        show_message("File Not Found", f"{monitor_path} not found.")
        play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")
def launch_settings():
    clear()
    settings_path = os.path.join("settings.py")
    print(f"[DEBUG] Looking for: {settings_path}")
    if os.path.exists(settings_path):
        subprocess.run([sys.executable, settings_path])
    else:
        show_message("File Not Found", f"{settings_path} not found.")
        play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")


def show_menu():
    print("\nMenu:")
    print("1. Computer Monitor")
    print("2. Settings")
    print("3. Exit")

def main():
    while True:
        clear()
        show_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            launch_pythonplayer()
        elif choice == "2":
            launch_settings()
        elif choice in ("3", "exit"):
            print("Exiting...")
            break
        else:
            show_message("Invalid Choice", "Invalid choice or unimplemented feature.")
            play_sound('error-beep.wav')
            time.sleep(1)

if __name__ == "__main__":
    main()
