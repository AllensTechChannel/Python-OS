@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION

:: Move to Downloads folder
cd /d "%USERPROFILE%\Downloads"

:: Confirm installation
powershell -Command "Add-Type -AssemblyName System.Windows.Forms; if ([System.Windows.Forms.MessageBox]::Show('Are you sure you want to install Python 3. ', 'Setup', 'YesNo') -ne 'Yes') { exit 1 }"
IF ERRORLEVEL 1 (
    ECHO User cancelled the operation.
    TIMEOUT /T 2 >NUL
    EXIT /B
)

:: Notify download
powershell -Command "Add-Type -AssemblyName System.Windows.Forms; if ([System.Windows.Forms.MessageBox]::Show('Setup will now download PythonOS. This might take up to 3 minute depending on your network connection.', 'Setup', 'OKCancel') -ne 'OK') { exit 1 }"
IF ERRORLEVEL 1 (
    
    TIMEOUT /T 2 >NUL
    EXIT /B
)

:: Download PythonOS ZIP (make sure version matches your target)
powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.13.7/python-3.13.7-amd64.exe' -OutFile 'Python.exe'"
TIMEOUT /T 2 >NUL
CLS
 call Python.exe
powershell -Command "Add-Type -AssemblyName System.Windows.Forms; if ([System.Windows.Forms.MessageBox]::Show('Press OK to close setup. ', 'Setup', 'ok') -ne 'Yes') { exit 1 }"
IF ERRORLEVEL 1 (
    ECHO User cancelled the operation.
    TIMEOUT /T 2 >NUL
    EXIT /B
)
