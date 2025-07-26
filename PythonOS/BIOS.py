import psutil
import platform
import time
import os
import winsound
from datetime import datetime
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
print("System Information made by Abdeladim Fadheli at https://thepythoncode.com/article/get-hardware-system-information-python (Ctrl + Click to follow)")
time.sleep(1)
print("Brightness control made by Parvat Computer Technology at https://www.youtube.com/watch?v=VMXselzxVxU (Ctrl + Click to follow)")
time.sleep(1)
print("Internet status made by geeksforgeeks at https://www.geeksforgeeks.org/python/how-to-check-whether-users-internet-is-on-or-off-using-python/ (Ctrl + Click to follow)")
time.sleep(5)
clear()
print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

# let's print CPU information
print("="*40, "CPU Info", "="*40)
# number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")

import requests

# initializing URL
url = "https://www.python.org/"
timeout = 10
try:
    # requesting URL
    request = requests.get(url, timeout=timeout)
    print("="*40, "Internet Adapter Info ", "="*40)
                      
    print("Internet adapter detected")

# catching exception
except (requests.ConnectionError,requests.Timeout) as exception:
        print("="*40, "Internet Adapter Info ", "="*40)
        print("Internet adapter is not detected")
  
import screen_brightness_control as pct


#get current brightness level
print("="*40, "Brightness ", "="*40)
print(pct.get_brightness())

level=input("Enter brightness level: ")

pct.set_brightness(level)



#print(pct.get_brightness())

winsound.PlaySound('media/startup-error-beep.wav', winsound.SND_FILENAME)
input("\nPress Enter to return to continue boot")
clear()

