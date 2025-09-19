@echo off
title Python Environment Setup
echo ====================================================
echo Installing required Python packages...
echo ====================================================
echo.

:: Upgrade pip first
py -m pip install --upgrade pip

:: Core packages
py -m pip install Pillow
py -m pip install ttkbootstrap
py -m pip install screen-brightness-control
py -m pip install keyboard
py -m pip install psutil
py -m pip install pywebview
py -m pip install playsound==1.2.2

echo.
echo ====================================================
echo All packages installed successfully!
echo Launching boot.py...
echo ====================================================
echo.

:: Run your Python program
py boot.py

pause
