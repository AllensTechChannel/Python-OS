import time
import os
import hashlib

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    OPTION_MAP = {
        "1": "desktop", "desktop": "desktop", "d": "desktop",
        "2": "restart", "restart": "restart", "reboot": "restart", "r": "restart",
        "3": "exit", "exit": "exit", "q": "exit", "quit": "exit",
        "4": "cmd", "cli": "cmd", "cmd": "cmd", "terminal": "cmd"
    }

    while True:
        print("\nMenu:")
        print("1. Desktop")
        print("2. Restart")
        print("3. Exit")
        print("4. CMD")

        choice = input("Enter your choice: ").strip().lower()
        action = OPTION_MAP.get(choice)

        if action == "desktop":
            print("Executing Desktop...")
            time.sleep(1)
            try:
                os.system("python desktop.py")
            except Exception as e:
                print("desktop.py not found.")

        elif action == "restart":
            print("Restarting...")
            clear_screen()
            try:
                os.system("Start.bat")
            except Exception as e:
                print("Error executing Start.bat:", e)

        elif action == "exit":
            print("Exiting...")
            break

        elif action == "cmd":
            print("Opening CMD...")
            try:
                with open("CMD.py", "r") as file:
                    code = file.read()
                    exec(code)
            except FileNotFoundError:
                print("CMD.py not found.")

        else:
            print("Invalid choice. Please try again.")

# Simulated startup
clear_screen()
print("Loading BIOS...")
time.sleep(1)
print("Loading BIOS Settings...")
time.sleep(1)
print("Booting Python OS...")
time.sleep(3)

clear_screen()
print("Python OS is loading, please wait...")
time.sleep(3)
clear_screen()

# Simulated user database
users = {
    "User": {
        "password": hashlib.sha256("User".encode()).hexdigest(),
        "message": "Welcome User, to Python OS"
    },
    "Administrator": {
        "password": hashlib.sha256("Administrator".encode()).hexdigest(),
        "message": "Welcome Administrator, to Python OS"
    }
}

# Login prompt
print("""List of users:
1. User
2. Administrator""")

username = input("Username: ")
password = input("Password: ")
hashed_password = hashlib.sha256(password.encode()).hexdigest()

if username in users and users[username]["password"] == hashed_password:
    clear_screen()
    print("Access granted!")
    print(users[username]["message"])
    menu()
else:
    print("Access denied. Invalid username or password.")
    print("Password Hint: The username is the same as the password")
    try:
        with open("Start.bat", "r") as file:
            contents = file.read()
            print("\n[Start.bat contents loaded (example)]")
    except FileNotFoundError:
        print("Start.bat file not found.")
