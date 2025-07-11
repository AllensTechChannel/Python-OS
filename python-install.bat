ECHO OFF
CLS
:MENU
ECHO.
ECHO ...............................................
ECHO PRESS 1 to install python or 2 to EXIT.
ECHO ...............................................
ECHO.
ECHO 1 - Install Python 3.13.3 amd64
ECHO 2 - EXIT
ECHO.

SET /P M=Type 1 or 2 then press ENTER:
IF %M%==1 GOTO INSTALL
IF %M%==2 GOTO EXIT 
:INSTALL
Echo Attempting to install Python 
start https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe
C:
cd C:/users/%username%/downloads
timeout /t 10 /nobreak
Start python-3.13.3-amd64.exe
exit
GOTO MENU
:EXIT
exit
GOTO MENU



