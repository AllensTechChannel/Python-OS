import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_sound(filename):
    path = os.path.join(os.getcwd(), 'media', filename)
    if os.path.exists(path):
        import winsound
        winsound.PlaySound(path, winsound.SND_FILENAME)
    else:
        print(f"[Missing sound file: {path}]")

def launch_pythonplayer(original_dir):
    clear()
    try:
        os.chdir("..")
        os.chdir("Programs")
        os.chdir("pythonplayer")
        bat_path = "playsound-install.bat"
        print("Looking for:", bat_path)
        if os.path.exists(bat_path):
            os.startfile(bat_path)
        else:
            print(f"{bat_path} not found.")
        time.sleep(1)
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")

def launch_internet_explorer(original_dir):
    clear()
    try:
        os.chdir("..")
        os.chdir("Programs")
        os.chdir("Internet Explorer")
        bat_path = "Webview-install.bat"
        print("Looking for:", bat_path)
        if os.path.exists(bat_path):
            os.startfile(bat_path)
        else:
            print(f"{bat_path} not found.")
        time.sleep(1)
    finally:
        os.chdir(original_dir)

    play_sound('error-beep.wav')
    input("\nPress Enter to return to the menu...")


def show_menu():
    print("\nMenu:")
    print("1. PythonPlayer (Media Player)")
    print("2. Internet Explorer")
    print("3. Exit")

def main():
    original_dir = os.getcwd()
    while True:  # ← here's your loop
        clear()
        show_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            launch_pythonplayer(original_dir)
        elif choice == "2":
            launch_internet_explorer(original_dir)
        elif choice in ("3", "exit"):
            print("Exiting...")
            break  # ← now it makes sense!
        else:
            print("Invalid choice or unimplemented feature. Please try again.")
            play_sound('error-beep.wav')
            time.sleep(1)

if __name__ == "__main__":
    main()
