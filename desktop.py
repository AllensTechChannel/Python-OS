import sys
import os
import time
import subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("\nMenu:")
    print("1. Updates")
    print("2. Command Line Interface (CLI)")
    print("3. Exit")
    print("4. Restart")
    print("5. View Clock")
    print("6. Games")

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

# Map multiple inputs to single commands
OPTION_MAP = {
    "1": "updates", "updates": "updates", "u": "updates",
    "2": "cli", "cli": "cli", "cmd": "cli",
    "3": "exit", "quit": "exit", "q": "exit",
    "4": "restart", "reboot": "restart", "r": "restart",
    "5": "clock", "view clock": "clock", "c": "clock",
    "6": "games", "play": "games", "g": "games"
}

def main():
    clear()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip().lower()
        action = OPTION_MAP.get(choice)

        if action == "updates":
            print("Opening Updates...")
            print("Python OS 3 Updates")
            print("Updates:")   
            print("1. Added games like Pong.")
            print("2. Made the automatic Python install more accessible")       
            print("BUGS:")
            print("1. The logon screen can get messed up sometimes")
            print("2. The ball in Pong can go through the paddle")
            input("\nPress Enter to return to the menu...")
            clear()

        elif action == "cli":
            print("Opening CMD.py...")
            if os.path.exists("CMD.py"):
                subprocess.run([sys.executable, "CMD.py"])
            else:
                print("CMD.py not found.")
            input("\nPress Enter to return to the menu...")
            clear()

        elif action == "exit":
            print("Exiting...")
            break

        elif action == "restart":
            print("Restarting...")
            time.sleep(1)
            clear()
            if os.path.exists("Start.bat"):
                os.system("Start.bat")
            else:
                print("Start.bat not found.")

        elif action == "clock":
            clock()

        elif action == "games":
            game_path = os.path.join("games", "game-select.py")
            if os.path.exists(game_path):
                subprocess.run([sys.executable, game_path])
            else:
                print("game-select.py not found.")
            input("\nPress Enter to return to the menu...")
            clear()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
