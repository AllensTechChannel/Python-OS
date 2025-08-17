import time
import os
import winsound 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


time_input = input("Enter amount of seconts for timer (60 sec = 1 min): ")
def countdown(t): 

    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

    

t = time_input

countdown(int(t))
clear_screen()
print(t,"Seconds Is Up!")
winsound.PlaySound('clocksound/alarm.wav', winsound.SND_FILENAME) 