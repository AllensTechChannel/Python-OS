@echo off

start "" python-install.bat


pause

py -m pip install psutil
py -m pip install keyboard
py -m pip install screen-brightness-control
py -m pip install requests
C:\Users\%username%\AppData\Local\Programs\Python\Python313\python.exe -m pip install --upgrade pip
boot.py
pause