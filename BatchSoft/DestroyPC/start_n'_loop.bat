@echo off
color c
title Start n' Loop
echo Start n' Loop PC Crasher:
echo (c) Okmeque1 Corporation. Open-source.
echo WARNING! THIS WILL COMPLETELY NUKE YOUR COMPUTER.
echo Do you want do proceed?
echo [1] Yes
echo [2] No
choice /c:12 /m "Choose an option: "
IF ERRORLEVEL 2 GOTO QUIT
IF ERRORLEVEL 1 GOTO NUKE
:NUKE
start "" %~dp0\start_n'_loop.bat
goto NUKE
:QUIT
exit /b
