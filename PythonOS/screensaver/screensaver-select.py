import os
import time

def play_sound(filename):
    print(f"Playing sound: {filename}")  # Placeholder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("\nMenu:")
    print("1. DVD Screensaver")
    print("2. Mystify Screensaver")
    print("3. Exit")

def launch_screensaver(screensaver):
    clear()
    original_dir = os.getcwd()
    try:
        os.chdir("screensaver/mystify")
        bat_path = "install-pygame.bat"
        print("Looking for:", bat_path)
        if os.path.exists(bat_path):
            os.startfile(bat_path)
        else:
            print(f"{bat_path} not found.")
    finally:
        os.chdir(original_dir)
    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")
    clear()
def launch_screensaver(dvd):
    clear()
    original_dir = os.getcwd()
    try:
        
        os.chdir("screensaver/dvd")
        bat_path = "install-pygame.bat"
        print("Looking for:", bat_path)
        if os.path.exists(bat_path):
            os.startfile(bat_path)
        else:
            print(f"{bat_path} not found.")
    finally:
        os.chdir(original_dir)
    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")
    clear()

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip().lower()
        original_dir = os.getcwd()
        if choice == "1" or choice == "dvd":
            launch_screensaver('dvd')
        elif choice == "2" or choice == "mystify":
            launch_screensaver('mystify')
        elif choice == "3" or choice == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid choice or unimplemented feature. Please try again.")
            
            play_sound('error-beep.wav')
            time.sleep(1)
            clear()

if __name__ == "__main__":
    main()
