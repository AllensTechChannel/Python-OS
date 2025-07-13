import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    while True:
        clear()
        print("Python CLI Clock")
        print("================")
        print(time.strftime("Date: %A, %d %B %Y"))
        print(time.strftime("Time: %H:%M:%S"))
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")