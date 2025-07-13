
import os

clear_screen()
def python_cmd():
    print("Python OS [1.0](c) The Python Software Foundation. All rights reserved.")
    print("Type 'help' for a list of commands. Type 'exit' to quit.\n")

    while True:
        command = input(f"{os.getcwd()}> ").strip().lower()
        if command == "exit":
            print("Exiting CMD...")
            break
        elif command == "help":
            print("""
Available commands:
  help       - Show this help message
  exit       - Exit the CMD
  clear      - Clear the screen
  ls / dir   - List files in current directory
  cd [dir]   - Change directory
  pwd        - Print current directory
  echo [msg] - Print a message
""")
        elif command in ["ls", "dir"]:
            for item in os.listdir():
                print(item)
        elif command.startswith("cd "):
            path = command[3:].strip()
            try:
                os.chdir(path)
                print(f"Changed directory to: {os.getcwd()}")
            except FileNotFoundError:
                print("Directory not found.")
        elif command == "pwd":
            print(os.getcwd())
        elif command.startswith("echo "):
            print(command[5:].strip())
        elif command == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print(f"Unknown command: {command}. Type 'help' for a list of commands.")

# Run the CMD interface
if __name__ == "__main__":
    python_cmd()
