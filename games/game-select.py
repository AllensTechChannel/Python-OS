import sys
import os
import time
import subprocess
os.chdir("..") 
os.chdir("games") 
def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen appropriately
        print("\nMain Menu:")
        
        print("1. Pong")
        print("2. MineSweeper")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Opening Pong")
            time.sleep(1)
            if os.path.exists("Pong.py"):
                subprocess.run([sys.executable, "Pong.py"])
            else:
                print("Pong.py not found.")
            time.sleep(1)
        elif choice == "2":
            print("Opening MineSweeper")
            time.sleep(1)
            if os.path.exists("MineSweeper/MineSweeper/game.py"):
                subprocess.run([sys.executable, "MineSweeper/MineSweeper/game.py"])
            else:
                print("game.py not found.")
            time.sleep(1)

        

        elif choice == "3":
            print("Returning to the Desktop!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
