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
set /p filepath_uac="Enter file path: "
cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "%filepath_uac%"
echo.
goto START
:CHROMELAUNCHER
cls
echo Please be aware that this program (BRSTD1) will fail if you moved Chrome to an other location or if it's not in its default location.
set /p username_session="Enter your username (can be found with the command 'whoami' in the Windows Command Prompt (cmd.exe)): "
set /p version_chrome="Enter Chrome version to open (any number from 1-current release) e.g. 86, 120, 121,...: "
start "" "C:\Progra~2\Google\Chrome\Application\chrome.exe" --user-data-dir="C:\Users\%username_session%\AppData\Local\Google\Chrome\User Data" --disable-infobars  --no-sandbox  --ignore-certificate-errors --disable-logging --no-default-browser-check --disable-component-update --disable-background-networking --allow-outdated-plugins --cipher-suite-blacklist=0xcc14,0xe013 --ignore-certificate-errors --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%version_chrome%.0.0.0 Safari/537.36"
echo.
goto start
:STARTCMD
start
goto END
:END
exit /b
