import time
import os
import hashlib
import winsound
import keyboard

# Clear screen based on platform
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# BIOS script execution function
def enter_BIOS():
    file_path = "BIOS.py"
    if os.path.exists(file_path):
        os.system(f"{file_path}")
    else:
        print(f"File '{file_path}' not found!")

# --- Simulated startup ---
print("Loading BIOS Config...")
time.sleep(1)

print("Loading Hardware Config...")
time.sleep(1)
winsound.PlaySound('media/startup-error-beep.wav', winsound.SND_FILENAME)
print("Press 'b' to enter the BIOS or 'Esc' to continue to boot .")
# Wait for user to press 'b' or 'Esc'
while True:
    if keyboard.is_pressed('b'):
        print("Loading BIOS...")
        enter_BIOS()
        break
    elif keyboard.is_pressed('esc'):
        print("Continuing to Boot")
        break
    time.sleep(0.1)  # Small delay to reduce CPU usage

# Main menu options
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

            except Exception:
                print("desktop.py not found.")
        elif action == "restart":
            print("Restarting...")
            clear_screen()
            try:
                os.system("Boot.py")
            except Exception as e:
                print(f"Error executing boot.py: {e}")
            winsound.PlaySound('media/error-beep.wav', winsound.SND_FILENAME)
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
            winsound.PlaySound('media/error-beep.wav', winsound.SND_FILENAME)
        else:
            winsound.PlaySound('media/error-beep.wav', winsound.SND_FILENAME)
            print("Invalid choice. Please try again.")

# User data with hashed passwords
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

# Display login screen with clock
def display_login_screen_with_clock():
    login_data = {}
    
    while True:
        clear_screen()
        print("==== Python OS Logon Screen ====")
        print("List of users:\n1. User\n2. Administrator")
        

        if "lockout_time" in login_data:
            remaining = login_data["lockout_time"] - time.time()
            if remaining > 0:
                winsound.PlaySound('media/error-beep.wav', winsound.SND_FILENAME)
                print(f"\nToo many attempts. Locked out for {int(remaining)} seconds.\n")
                time.sleep(1)
                continue
            else:
                print("(Press ENTER after entering each field)\n")

        username = input("Username: ")
        password = input("Password: ")

        yield username, password, login_data

# Continue boot process
print("Booting Python OS...")

winsound.PlaySound('media/startup-beep.wav', winsound.SND_FILENAME)
time.sleep(3)

clear_screen()
print("Python OS is loading, please wait...")
time.sleep(3)
clear_screen()

# Login loop
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
        winsound.PlaySound('media/error-beep.wav', winsound.SND_FILENAME)
        print("Access denied. Invalid username or password.")
        print("Password Hint: The username is the same as the password")

        if attempts >= MAX_ATTEMPTS:
            winsound.PlaySound('media/error-beep.wav', winsound.SND_FILENAME)
            print(f"\nToo many failed attempts. Locking out for {LOCKOUT_SECONDS} seconds.")
            login_data["lockout_time"] = time.time() + LOCKOUT_SECONDS
            attempts = 0
        time.sleep(2)
