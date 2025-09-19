@echo off

start "" python-install.bat


pause

py -m  pip install Pillow 
py -m  pip install ttkbootstrap 
py -m  pip install screen-brightness-control 
py -m  pip install keyboard 
py -m  pip install psutil 

py -m  pip install Webview
C:\Users\%username%\AppData\Local\Programs\Python\Python313\python.exe -m pip install --upgrade pip

py -m pip install playsound==1.2.2
cls
boot.py

pause
