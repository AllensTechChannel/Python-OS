import tkinter as tk
from tkinter import messagebox
import sys
import os
import time
import subprocess
import winsound

# === Get base directory for media sounds ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def play_sound(filename):
    path = os.path.join(BASE_DIR, 'media', filename)
    if os.path.exists(path):
        winsound.PlaySound(path, winsound.SND_FILENAME)
    else:
        print(f"[Missing sound file: {path}]")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def clock():
    try:
        while True:
            clear()
            print(time.strftime("Date: %A, %d %B %Y"))
            print(time.strftime("Time: %H:%M:%S"))
            print("\nPress Ctrl+C to return to the menu.")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReturning to menu...")
        time.sleep(1)

def show_menu():
    print("\nMenu:")
    print("1. Updates")
    print("2. Command Line Interface (CLI)")
    print("3. Exit")
    print("4. Restart")
    print("5. View Clock")
    print("6. Games")
    print("7. Screensaver")
    print("8. Programs")
    print("9. About")

OPTION_MAP = {
    "1": "updates", "updates": "updates", "u": "updates",
    "2": "cli", "cli": "cli", "cmd": "cli",
    "3": "exit", "quit": "exit", "q": "exit",
    "4": "restart", "reboot": "restart", "r": "restart",
    "5": "clock", "view clock": "clock", "c": "clock",
    "6": "games", "play": "games", "g": "games",
    "7": "screensaver", "start screensaver": "screensaver",
    "8": "programs", "p": "programs",
    "9": "about", "winver": "about"
}

def show_error(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(title, message)
    root.destroy()

def main():
    os.chdir(BASE_DIR)
    clear()
    play_sound('desktop-logon.wav')

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip().lower()
        action = OPTION_MAP.get(choice)

        if action == "updates":
            clear()
            print("Opening Updates...\n")
            print("Python OS 4.13 Updates")
            print("\nUpdates:")
            print("1. Added a Paint Program (PyPaint)")
            print("2. Added an About Box")
            print("3. Added a SYSTEM folder for future projects")
            print("4. Added a new logon sound")

            print("\nBUGS:")
            print("1. The logon screen can get messed up sometimes")
            print("2. The ball in Pong can go through the paddle")
            play_sound('error-beep.wav')
            input("\nPress Enter to return to the menu...")
            clear()

        elif action == "cli":
            clear()
            print("Opening CMD.py...")
            if os.path.exists("CMD.py"):
                subprocess.run([sys.executable, "CMD.py"])
            else:
                show_error("File Not Found", "CMD.py was not found in the current directory.")
            play_sound('error-beep.wav')
            input("\nPress Enter to return to the menu...")
            clear()

        elif action == "exit":
            root = tk.Tk()
            root.withdraw()
            if messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?"):
                root.destroy()
                print("Exiting...")
                break
            else:
                root.destroy()
                clear()

        elif action == "about":
            clear()
            original_dir = os.getcwd()
            try:
                os.chdir(os.path.join(BASE_DIR, "SYSTEM"))
                if os.path.exists("About.py"):
                    subprocess.run([sys.executable, "About.py"])
                else:
                    show_error("File Not Found", "About.py not found in SYSTEM folder.")
            finally:
                os.chdir(original_dir)

            play_sound('error-beep.wav')
            input("\nPress Enter to return to the menu...")
            clear()

        elif action == "restart":
            root = tk.Tk()
            root.withdraw()
            if messagebox.askyesno("Restart Confirmation", "Are you sure you want to restart?"):
                root.destroy()
                print("Restarting...")
                time.sleep(1)
                clear()
                if os.path.exists("Boot.py"):
                    subprocess.run([sys.executable, "Boot.py"])
                else:
                    show_error("File Not Found", "Boot.py was not found.")
                play_sound('error-beep.wav')
                break
            else:
                root.destroy()
                clear()

        elif action == "clock":
            clock()

        elif action == "games":
            clear()
            game_script = os.path.abspath(os.path.join("..", "games", "game-select.py"))
            print("Looking for:", game_script)
            if os.path.exists(game_script):
                subprocess.run([sys.executable, game_script])
            else:
                show_error("File Not Found", f"{game_script} was not found.")
            play_sound('error-beep.wav')
            input("\nPress Enter to return to the menu...")
            clear()

        elif action == "screensaver":
            clear()
            screensaver_script = os.path.abspath(os.path.join("screensaver", "screensaver-select.py"))
            print("Looking for:", screensaver_script)
            if os.path.exists(screensaver_script):
                subprocess.run([sys.executable, screensaver_script])
            else:
                show_error("File Not Found", f"{screensaver_script} was not found.")
            play_sound('error-beep.wav')
            input("\nPress Enter to return to the menu...")
            clear()

        elif action == "programs":
            clear()
            program_script = os.path.abspath("program-select.py")
            print("Looking for:", program_script)
            if os.path.exists(program_script):
                subprocess.run([sys.executable, program_script])
            else:
                show_error("File Not Found", f"{program_script} was not found.")
            play_sound('error-beep.wav')
            input("\nPress Enter to return to the menu...")
            clear()

if __name__ == "__main__":
    main()
