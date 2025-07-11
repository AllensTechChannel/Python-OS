import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

def python_cmd():
    print("Python OS [1.0] (c) The Python Software Foundation. All rights reserved.")
    print("Type 'help' for a list of commands. Type 'exit' to quit.\n")

    while True:
        command = input(f"{os.getcwd()}> ").strip()

        # Exits the CLI
        if command.lower() == "exit":
            print("Exiting CMD...")
            clear_screen()
            break

        # Shows available commands
        elif command.lower() == "help":
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

        # Shows contents of current directory
        elif command.lower() in ["ls", "dir"]:
            for item in os.listdir():
                print(item)

        # Changes directory
        elif command.lower().startswith("cd "):
            path = command[3:].strip()
            try:
                os.chdir(path)
                print(f"Changed directory to: {os.getcwd()}")
            except FileNotFoundError:
                print("Directory not found.")

        # Prints current directory
        elif command.lower() == "pwd":
            print(os.getcwd())

        # Prints a message
        elif command.lower().startswith("echo "):
            print(command[5:].strip())

        # Clears the screen
        elif command.lower() == "clear":
            clear_screen()

        else:
            print(f"Unknown command: {command}. Type 'help' for a list of commands.")

# Run the CMD interface
if __name__ == "__main__":
    python_cmd()
