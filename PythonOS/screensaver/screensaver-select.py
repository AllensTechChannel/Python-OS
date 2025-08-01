import os
import time
import subprocess
# Utility function to simulate sound playing
def play_sound(filename):
    print(f"Playing sound: {filename}")  # Placeholder for actual sound playback

# Clear terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display main menu
def show_menu():
    print("\nMenu:")
    print("1. DVD Screensaver")
    print("2. Mystify Screensaver")
    print("3. Exit")

# Launch DVD Screensaver
def launch_dvd_screensaver():
    clear()
    original_dir = os.getcwd()
    try:
        os.chdir("screensaver/dvd")
        bat_path = "install-pygame.bat"
        print("Looking for:", bat_path)
        if os.path.exists(bat_path):
            try:
                subprocess.run(bat_path, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Batch file exited with error: {e}")
            except OSError as e:
                print(f"OS error launching {bat_path}: {e}")
        else:
            print(f"{bat_path} not found.")
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")
    clear()
# Launch Mystify Screensaver
def launch_mystify_screensaver():
    clear()
    original_dir = os.getcwd()
    try:
        os.chdir("screensaver/mystify")
        bat_path = "install-pygame.bat"
        print("Looking for:", bat_path)
        if os.path.exists(bat_path):
            try:
                subprocess.run(bat_path, shell=True, check=True)
            except subprocess.CalledProcessError as e:

                print(f"Error launching {bat_path}: {e}")
        else:
            print(f"{bat_path} not found.")
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")
    clear()

# Main program loop
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1" or choice == "dvd":
            launch_dvd_screensaver()
        elif choice == "2" or choice == "mystify":
            launch_mystify_screensaver()
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
