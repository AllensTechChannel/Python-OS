import time
import os
import hashlib

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        print("\nMenu:")
        print("1. Desktop")
        print("2. Restart")
        print("3. Exit")
        print("4. CMD")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Executing Desktop...")
            try:
                os.system("E:/desktop.py")
            except Exception as e:
                print("desktop.py not found.")
        elif choice == '2':
            print("Restarting...")
            try:
                os.system("E:/Start.bat")
            except Exception as e:
                print("Error executing Start.bat:", e)
        elif choice == '3':
            print("Exiting...")
            break
        elif choice == '4':
            print("Opening CMD...")
            try:
                with open("E:/CMD.py", "r") as file:
                    code = file.read()
                    exec(code)
            except FileNotFoundError:
                print("CMD.py not found.")
        else:
            print("Invalid choice. Please try again.")


# Simulated startup
print("Loading BIOS...")
print("Loading BIOS Settings...")
print("Booting Python OS...")
time.sleep(5)

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
