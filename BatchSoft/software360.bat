@echo off
goto start
:START
echo Software360 All-in-1 
echo (c) GamerSoftware Corporation™ and Okmeque1 Corporation™. All rights reserved.
echo Program version: 0.88-alpha. If action returns to main menu, that means the option is not implemented.
echo [1] UAC Bypass.
echo [2] UAC Bypass (Encrypted).
echo [3] Make Elevated Task.
echo [4] Start PROGRAM w/flags (e.g : using --user-data-dir and --disable-certificate-errors when starting BrStd1 Browser).
echo [5] Quit program.
choice /c:12345 /m "Choose an option : "
IF ERRORLEVEL 5 GOTO END
IF ERRORLEVEL 4 GOTO BRSTD1
IF ERRORLEVEL 3 GOTO SETADMIN
IF ERRORLEVEL 2 GOTO UACBYPASSENCRYPT
IF ERRORLEVEL 1 GOTO UACBYPASS
:UACBYPASS
set /p input="Enter FILE PATH : "
cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "%input%"
goto START
:UACBYPASSENCRYPT
REM GamerSoft24! You figure out how it works and make the %1 variable to the command on line 17.
goto START
:SETADMIN
REM See, the CMDLine works using the bypass UAC but the problem is that it opens std cmd prompt and we want admin cmd prompt
goto START
:BRSTD1
set /p BR="Enter program with or with no parameters: "
start "%BR%"
goto START
:END
