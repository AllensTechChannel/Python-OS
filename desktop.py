import os
import time
import subprocess

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

# Map multiple inputs to single commands
OPTION_MAP = {
    "1": "updates", "updates": "updates", "u": "updates",
    "2": "cli", "cli": "cli", "cmd": "cli",
    "3": "exit", "quit": "exit", "q": "exit",
    "4": "restart", "reboot": "restart", "r": "restart",
    "5": "clock", "view clock": "clock", "c": "clock"
}

clear()

while True:
    print("\nMenu:")
    print("1. Updates")
    print("2. Command Line Interface (CLI)")
    print("3. Exit")
    print("4. Restart")
    print("5. View Clock")
    

    choice = input("Enter your choice: ").strip().lower()
    action = OPTION_MAP.get(choice)

    if action == "updates":
        print("Opening Updates...")
        print("Python OS 2 updates:")
        print("1. Added a shortcut to the CLI to the desktop.")
        print("2. Added a list of users at logon.")
        print("3. Organized code with comments.")
        print("4. Added a clock")
        print("5. Added more flexibility with menues")
        print("BUGS: None known.")

    elif action == "cli":
        print("Opening CMD.py...")
        if os.path.exists("CMD.py"):
            subprocess.run(["python", "CMD.py"])
        else:
            print("CMD.py not found.")
        clear()

    elif action == "exit":
        print("Exiting...")
        break

    elif action == "restart":
        print("Restarting...")
        clear()
        if os.path.exists("Start.bat"):
            os.system("Start.bat")
        else:
            print("Start.bat not found.")

    elif action == "clock":
        clock()

    else:
        print("Invalid choice. Please try again.")
