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

OPTION_MAP = {
    "1": "updates", "updates": "updates", "u": "updates",
    "2": "cli", "cli": "cli", "cmd": "cli",
    "3": "exit", "quit": "exit", "q": "exit",
    "4": "restart", "reboot": "restart", "r": "restart",
    "5": "clock", "view clock": "clock", "c": "clock",
    "6": "games", "play": "games", "g": "games",
    "7": "screensaver", "start screensaver": "screensaver",
}

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    clear()
    play_sound('desktop-logon.wav')

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip().lower()
        action = OPTION_MAP.get(choice)

        if action == "updates":
            clear()
            print("Opening Updates...\n")
            print("Python OS 4 Updates")
            print("\nUpdates:")
            print("1. Added BIOS")
            print("2. Added Credits.md")
            print("3. Added Sound")
            print("4. Created README.txt")

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
                print("CMD.py not found.")
            play_sound('error-beep.wav')
            input("\nPress Enter to return to the menu...")
            clear()

        elif action == "exit":
            print("Exiting...")
            break

        elif action == "restart":
            print("Restarting...")
            time.sleep(1)
            clear()
            if os.path.exists("Boot.py"):
                subprocess.run([sys.executable, "Boot.py"])
            else:
                print("Boot.py not found.")
            play_sound('error-beep.wav')
            input("\nPress Enter to return to the menu...")
            clear()

        elif action == "clock":
            clock()

        elif action == "games":
            clear()
            game_script = os.path.abspath(os.path.join("..", "games", "game-select.py"))
            print("Looking for:", game_script)
            print("Current working directory:", os.getcwd())

            if os.path.exists(game_script):
                subprocess.run([sys.executable, game_script])
            else:
                print("ERROR: game-select.py not found.")
            play_sound('error-beep.wav')
            input("\nPress Enter to return to the menu...")
            clear()

        elif action == "screensaver":
         clear()
         screensaver_script = os.path.abspath(os.path.join("screensaver", "screensaver-select.py"))
         print("Looking for:", screensaver_script)
         print("Current working directory:", os.getcwd())

         if os.path.exists(screensaver_script):
             subprocess.run([sys.executable, screensaver_script])
         else:
                print("ERROR: game-select.py not found.")
         play_sound('error-beep.wav')
         input("\nPress Enter to return to the menu...")
         clear()

   

if __name__ == "__main__":
    main()

