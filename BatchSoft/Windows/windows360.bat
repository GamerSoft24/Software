@echo off
goto START
:START
cls
Title
color a
echo Windows360 All-In-One Program:
echo Program version: 0.97-foxtrot. 
echo (c) GamerSoftware Corporation and Okmeque1 Corporation. All rights reserved.
echo If action returns to main menu, that means the option is not implemented.
echo [1] System Infomations.
echo [2] Website Pinger.
echo [3] Quit program.
choice /c:1234 /m "Choose an option: "
IF ERRORLEVEL 3 GOTO QUIT
IF ERRORLEVEL 2 GOTO WEBPING
IF ERRORLEVEL 1 GOTO SYSTEMINFOS
:SYSTEMINFOS
cls
Title System Informations
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
goto START
:WEBPING
cls
Title Website Pinger
color a
echo Website Pinger:
set input=
set /p input= Enter your website to ping here: 
if %input%==goto A if NOT B
echo Processing your request...
ping %input%
goto START
:QUIT
exit /b