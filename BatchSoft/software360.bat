@echo off
goto start
title Software360 AIO
:START
cls
color a
echo Software360 AIO:
echo Made by GamerSoftware Corp. and Okmeque1 Computers. (c) All rights reserved.
echo V0.86-alpha. If action returns to main menu, that means the option is not implemented.
echo [1] UAC Bypass
echo [2] Start PROGRAM w/flags (e.g : using --user-data-dir and --disable-certificate-errors when starting BrStd1 Browser)
echo [3] Goto CMD (cmd.exe).
echo [4] Use COMPATABILITY flag for browser( disabling all errors and faking user agent. Uses SUPERMIUM 118 User agent and _BrStd1(taskbar) settings.)
echo [5] Quit
choice /c:12345 /m "Choose an option : "
IF ERRORLEVEL 7 GOTO END
IF ERRORLEVEL 6 GOTO 360UDATA1
IF ERRORLEVEL 5 GOTO STARTCMD
IF ERRORLEVEL 4 GOTO BRSTD1
IF ERRORLEVEL 3 GOTO SETADMIN
IF ERRORLEVEL 2 GOTO UACBYPASSENCRYPT
IF ERRORLEVEL 1 GOTO UACBYPASS
:UACBYPASS
cls
set /p input="Enter FILE PATH : "
cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "%input%"
echo.
goto START
:UACBYPASSENCRYPT
cls
REM Gamersoft! You figure out how it works and make the %1 variable to the command on line 17.
echo.
goto START
:SETADMIN
cls
REM See, the CMDLine works using the bypass UAC but the problem is that it opens std cmd prompt and we want admin cmd prompt
echo.
goto START
:BRSTD1
cls
set /p BR="Enter program with or with no parameters. : "
echo %BR%
start "" %BR%
echo.
goto START
:360UDATA1
cls
set /p setpath="Enter BROWSER EXE path : "
set /p userdir="Enter USERDATA DIR : "
set /p crver="Enter CHROME version(any number from 1-current release) : "
start "" "%setpath%" --user-data-dir="%userdir%" --disable-infobars  --no-sandbox  --ignore-certificate-errors --disable-logging --no-default-browser-check --disable-component-update --disable-background-networking --allow-outdated-plugins --cipher-suite-blacklist=0xcc14,0xe013 --ignore-certificate-errors --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%crver%.0.0.0 Safari/537.36"
echo.
goto start
:STARTCMD
start
goto END
:END
exit /b
