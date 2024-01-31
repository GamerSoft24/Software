@echo off
goto start
:START
cls
color a
title Software360 AIO
echo Software360 AIO/All-In-One:
echo V1.26-beta. If action returns to main menu, that means the option is not implemented.
echo (c) GamerSoftware Corporation and Okmeque1 Corporation. All rights reserved.
echo [1] UAC Bypass.
echo [2] Open Windows Command Prompt (cmd.exe).
echo [3] BRSTD1 (Browser Standard 1).
echo [4] Quit program.
choice /c:1234 /m "Choose an option: "
IF ERRORLEVEL 4 GOTO END
IF ERRORLEVEL 3 GOTO CHROMELAUNCHER
IF ERRORLEVEL 2 GOTO STARTCMD
IF ERRORLEVEL 1 GOTO UACBYPASS
:UACBYPASS
cls
set /p input="Enter file path: "
cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "%input%"
echo.
goto START
:CHROMELAUNCHER
cls
set /p setpath="Enter browser path: "
set /p userdir="Enter User Data DIR: "
set /p crver="Enter Chrome version (any number from 1-current release): "
start "" "%setpath%" --user-data-dir="%userdir%" --disable-infobars  --no-sandbox  --ignore-certificate-errors --disable-logging --no-default-browser-check --disable-component-update --disable-background-networking --allow-outdated-plugins --cipher-suite-blacklist=0xcc14,0xe013 --ignore-certificate-errors --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%crver%.0.0.0 Safari/537.36"
echo.
goto start
:STARTCMD
start
goto END
:END
exit /b
