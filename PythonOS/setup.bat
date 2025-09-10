@echo off

start "" python-install.bat


pause

py -m  pip install Pillow ttkbootstrap screen-brightness-control keyboard psutil playsound Webview
C:\Users\%username%\AppData\Local\Programs\Python\Python313\python.exe -m pip install --upgrade pip
cls
boot.py
pause