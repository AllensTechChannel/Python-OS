import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()
while True:
        print("\nMenu:")
        print("1. Updates")
        print("2. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("Opening Updates...")
            print("Python OS 1.1 updates: 1. Bugs relating to file path  BUGS: 1. No known bugs")





        elif choice == '2':
            print("Exiting...")
            clear_screen()
            break
        else:
            print("Invalid choice. Please try again.")
