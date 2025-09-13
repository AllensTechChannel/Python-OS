import time
import os
import hashlib
import winsound
import keyboard
import tkinter as tk
from tkinter import messagebox

# === Central sound player ===
def play_sound(filename):
    path = os.path.join('media', filename)
    if os.path.exists(path):
        winsound.PlaySound(path, winsound.SND_FILENAME)
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Missing Sound", f"Sound file not found:\n{path}")
        root.destroy()

# Clear screen based on platform
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# BIOS script execution function
def enter_BIOS():
    file_path = "BIOS.py"
    if os.path.exists(file_path):
        os.system(file_path)
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("File Not Found", f"Could not find: {file_path}")
        root.destroy()

# --- Simulated startup ---
print("Loading BIOS Config...")
time.sleep(1)
print("Loading Hardware Config...")
time.sleep(1)
play_sound('startup-error-beep.wav')

print("Press 'b' to enter the BIOS or 'Esc' to continue to boot.")
while True:
    if keyboard.is_pressed('b'):
        print("Loading BIOS...")
        enter_BIOS()
        break
    elif keyboard.is_pressed('esc'):
        print("Continuing to Boot")
        break
    time.sleep(0.1)

# Menu system
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
            if os.path.exists("desktop.py"):
                os.system("desktop.py")
            else:
                root = tk.Tk(); root.withdraw()
                messagebox.showerror("File Not Found", "desktop.py not found.")
                root.destroy()
                play_sound('error-beep.wav')

        elif action == "restart":
            print("Restarting...")
            clear_screen()
            if os.path.exists("Boot.py"):
                os.system("Boot.py")
            else:
                root = tk.Tk(); root.withdraw()
                messagebox.showerror("File Not Found", "Boot.py not found.")
                root.destroy()
                play_sound('error-beep.wav')

        elif action == "exit":
            root = tk.Tk(); root.withdraw()
            if messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?"):
                root.destroy()
                print("Exiting...")
                break
            root.destroy()
            clear_screen()

        elif action == "cmd":
            print("Opening CMD...")
            if os.path.exists("CMD.py"):
                with open("CMD.py", "r") as file:
                    exec(file.read())
            else:
                root = tk.Tk(); root.withdraw()
                messagebox.showerror("File Not Found", "CMD.py not found.")
                root.destroy()
                play_sound('error-beep.wav')

        else:
            play_sound('error-beep.wav')
            print("Invalid choice. Please try again.")

# === Load owner file ===
file_path = "SYSTEM\\owner.txt"  # Replace with the actual path to your .txt file

try:
    with open(file_path, 'r') as file:
        owner = file.read().strip()
except FileNotFoundError:
    owner = "defaultuser"  # fallback if file doesn't exist

file_path = "SYSTEM\\pwd.txt"  # Replace with the actual path to your .txt file

try:
    with open(file_path, 'r') as file:
        pwd = file.read().strip()
except FileNotFoundError:
    pwd = "pwd"  # fallback if file doesn't exist
# === Users and login data ===
users = {
    owner: {
        "password": hashlib.sha256(pwd.encode()).hexdigest(),
        "message": f"Welcome {owner}, to Python OS"
    },
    "Administrator": {
        "password": hashlib.sha256("Administrator".encode()).hexdigest(),
        "message": "Welcome Administrator, to Python OS"
    }
}


# Login screen function
def display_login_screen_with_clock(login_data):
    clear_screen()
    print("==== Python OS Logon Screen ====")
    print("Default Username: user name
    print("Default Passowrd: defaultpassword")      

    if "lockout_time" in login_data:
        remaining = login_data["lockout_time"] - time.time()
        if remaining > 0:
            play_sound('error-beep.wav')
            print(f"\nToo many attempts. Locked out for {int(remaining)} seconds.\n")
            time.sleep(1)
            return None, None
        else:
            del login_data["lockout_time"]

    print("(Press ENTER after entering each field)\n")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    return username, password

# === Continue boot ===
print("Booting Python OS...")
play_sound('startup-beep.wav')
time.sleep(3)

clear_screen()
print("Python OS is loading, please wait...")
time.sleep(3)
clear_screen()

# === Login logic ===
MAX_ATTEMPTS = 3
LOCKOUT_SECONDS = 10
attempts = 0
login_data = {}

while True:
    username, password = display_login_screen_with_clock(login_data)
    if not username or not password:
        continue  # skip if locked out

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username in users and users[username]["password"] == hashed_password:
        clear_screen()
        print("Access granted!")
        print(users[username]["message"])
        menu()
        break
    else:
        attempts += 1
        play_sound('error-beep.wav')
        print("Access denied. Invalid username or password.")
        

        if attempts >= MAX_ATTEMPTS:
            play_sound('error-beep.wav')
            print(f"\nToo many failed attempts. Locking out for {LOCKOUT_SECONDS} seconds.")
            login_data["lockout_time"] = time.time() + LOCKOUT_SECONDS
            attempts = 0
        time.sleep(2)
