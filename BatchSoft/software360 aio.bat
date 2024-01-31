@echo off
goto start
title Software360 AIO
:START
cls
color a
echo Software360 AIO:
echo Made by GamerSoftware Corp. and Okmeque1 Computers. (c) All rights reserved.
echo V1.26-beta. If action returns to main menu, that means the option is not implemented.
echo [1] UAC Bypass
echo [2] Goto CMD (cmd.exe).
echo [3] Use COMPATABILITY flag for browser( disabling all errors and faking user agent. Uses SUPERMIUM 118 User agent and _BrStd1(taskbar) settings.)
echo [4] Quit
choice /c:12345 /m "Choose an option : "
IF ERRORLEVEL 4 GOTO END
IF ERRORLEVEL 3 GOTO 360UDATA1
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
