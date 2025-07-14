import time
import os
import hashlib
import threading

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
                os.system("desktop.py")
            except Exception as e:
                print("desktop.py not found.")

        elif action == "restart":
            print("Restarting...")
            clear_screen()
            try:
                os.system("Boot.py")
            except Exception as e:
                print("Error executing boot.py:", e)

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

def display_login_screen_with_clock():
    stop_clock = threading.Event()
    login_data = {}

    def show_clock():
        while not stop_clock.is_set():
            clear_screen()
            print("==== Python OS Logon Screen ====")
            print("List of users:\n1. User\n2. Administrator")
            print(f"Time: {time.strftime('%H:%M:%S')}")
            if "lockout_time" in login_data:
                remaining = login_data["lockout_time"] - time.time()
                if remaining > 0:
                    print(f"\nToo many attempts. Locked out for {int(remaining)} seconds.\n")
            else:
                print("(Press ENTER after entering each field)\n")
            time.sleep(1)

    while True:
        stop_clock.clear()
        clock_thread = threading.Thread(target=show_clock)
        clock_thread.start()

        if "lockout_time" in login_data:
            # If locked out, wait here
            while time.time() < login_data["lockout_time"]:
                time.sleep(1)
            del login_data["lockout_time"]
            continue  # Refresh login screen

        try:
            username = input("Username: ")
            password = input("Password: ")
        finally:
            stop_clock.set()
            clock_thread.join()

        yield username, password, login_data

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

# Lockout and login loop
MAX_ATTEMPTS = 3
LOCKOUT_SECONDS = 10
attempts = 0

login_generator = display_login_screen_with_clock()

for username, password, login_data in login_generator:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username in users and users[username]["password"] == hashed_password:
        clear_screen()
        print("Access granted!")
        print(users[username]["message"])
        menu()
        break
    else:
        attempts += 1
        print("Access denied. Invalid username or password.")
        print("Password Hint: The username is the same as the password")

        if attempts >= MAX_ATTEMPTS:
            print(f"\nToo many failed attempts. Locking out for {LOCKOUT_SECONDS} seconds.")
            login_data["lockout_time"] = time.time() + LOCKOUT_SECONDS
            attempts = 0  # reset after lockout
        time.sleep(2)  # short pause before reattempt
