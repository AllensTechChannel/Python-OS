import os
import sys
import time
import subprocess
import ctypes
import subprocess
# Show a Windows message box
def show_message(title, text, style=0x10):  # 0x10 = MB_ICONERROR
    ctypes.windll.user32.MessageBoxW(0, text, title, style)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_sound(filename):
    path = os.path.join(os.getcwd(), 'media', filename)
    if os.path.exists(path):
        import winsound
        winsound.PlaySound(path, winsound.SND_FILENAME)
    else:
        show_message("Missing File", f"Sound file not found:\n{path}")

def launch_user(original_dir):
    

    bat_file_path = "User.bat"  # Use double backslashes or raw string for path

    try:
        # Use shell=True to allow the command interpreter to handle the batch file execution
        result = subprocess.run(bat_file_path, shell=True, check=True, capture_output=True, text=True)
        print("Batch file executed successfully.")
        print("Output:", result.stdout)
        print("Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing batch file: {e}")
        print("Output:", e.stdout)
        print("Errors:", e.stderr)
    except FileNotFoundError:
        print(f"Error: Batch file not found at {bat_file_path}")

def launch_user2(original_dir):
    bat_file_path = "User2.bat"  # Use double backslashes or raw string for path

    try:
        # Use shell=True to allow the command interpreter to handle the batch file execution
        result = subprocess.run(bat_file_path, shell=True, check=True, capture_output=True, text=True)
        print("Batch file executed successfully.")
        print("Output:", result.stdout)
        print("Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing batch file: {e}")
        print("Output:", e.stdout)
        print("Errors:", e.stderr)
    except FileNotFoundError:
        print(f"Error: Batch file not found at {bat_file_path}")

def launch_pwd(original_dir):
    bat_file_path = "pwd.bat"  # Use double backslashes or raw string for path

    try:
        # Use shell=True to allow the command interpreter to handle the batch file execution
        result = subprocess.run(bat_file_path, shell=True, check=True, capture_output=True, text=True)
        print("Batch file executed successfully.")
        print("Output:", result.stdout)
        print("Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing batch file: {e}")
        print("Output:", e.stdout)
        print("Errors:", e.stderr)
    except FileNotFoundError:
        print(f"Error: Batch file not found at {bat_file_path}")


def show_menu():
    print("\nMenu:")
    print("1. Change Username")
    print("2. Change Company name")
    print("3. Change Passowrd")
    print("4. Exit")
    
def main():
    original_dir = os.getcwd()
    while True:
        clear()
        show_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            launch_user(original_dir)
        
        if choice == "2":
            launch_user2(original_dir)
        if choice == "3":
            launch_pwd(original_dir)
        elif choice in ("4", "exit"):
            print("Exiting...")
            break
        else:
            show_message("Invalid Choice", "Invalid choice or unimplemented feature.")
            play_sound('error-beep.wav')
            time.sleep(1)

if __name__ == "__main__":
    main()
