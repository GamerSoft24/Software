cls
color a
title System Informations
echo System Informations:
echo.
echo Running whoami...
whoami
pause
echo.
echo Running systeminfo...
systeminfo
pause
echo.
echo Running ipconfig...
ipconfig
pause
echo.
echo Listing directories of %~dp0\...
dir
echo.
echo Displaying user information...
net user
pause
echo.
echo Listing currently running tasks...
tasklist
pause
