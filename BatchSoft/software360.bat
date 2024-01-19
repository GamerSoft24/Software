@echo off
goto start
:START
cls
echo Software360 All-in-1 
echo (c) GamerSoftware Corporation™ and Okmeque1 Corporation™. All rights reserved.
echo Program version: 0.88-beta. If action returns to main menu, that means the option is not implemented.
echo [1] UAC Bypass.
echo [2] Make Elevated Task.
echo [3] Start PROGRAM w/flags (using --user-data-dir and --disable-certificate-errors when starting BrStd1 Browser).
echo [4] Quit program.
choice /c:12345 /m "Choose an option: "
IF ERRORLEVEL 4 GOTO END
IF ERRORLEVEL 3 GOTO BRSTD1
IF ERRORLEVEL 2 GOTO SETADMIN
IF ERRORLEVEL 1 GOTO UACBYPASS
:UACBYPASS
cls
set /p input="Enter file path: "
cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "%input%"
echo.
goto START
:UACBYPASSENCRYPT
cls
REM GamerSoft24! You figure out how it works and make the %1 variable to the command on line 17.
echo.
goto START
:SETADMIN
cls
REM See, the CMDLine works using the bypass UAC but the problem is that it opens std cmd prompt and we want admin cmd prompt
echo.
goto START
:BRSTD1
cls
set /p BR="Enter program with or with no parameters: "
start "" %BR%
echo.
goto START
:END
exit /b
