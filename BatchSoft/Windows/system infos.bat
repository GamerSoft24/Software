@echo off
color a
echo System Informations:
echo.
echo Running whoami...
whoami
echo.
echo Running systeminfo...
systeminfo
echo.
echo Running ipconfig...
ipconfig
echo.
echo Listing directories of C:...
dir
echo.
echo Displaying user information...
net user
echo.
echo Listing currently running tasks...
tasklist
pause
