@echo off
goto start
:START
echo Software360 All-in-1 
echo [1] UAC Bypass
echo [2] UAC Bypass (Encrypted)
echo [3] PLACEHOLDER
echo [4] PLACEHOLDER
choice /c:1234 /m Choose an option
IF ERRORLEVEL 1 GOTO UACBYPASS
IF ERRORLEVEL 2 GOTO UACBYPASSENCRYPT
IF ERRORLEVEL 3 GOTO PLACEHOLDER
IF ERRORLEVEL 4 GOTO PLACEHOLDER
:UACBYPASS1
rem USE SET /P TO GET PATHLINE INPUT AND SET %1 TO THE SET /P INPUT LINE
cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "%1"
:END
exit /b
