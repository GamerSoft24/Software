@echo off
Title Website Pinger
color a
echo Website Pinger:
set input=
set /p input= Enter your website to ping here: 
if %input%==goto A if NOT B
echo Processing your request...
ping %input%
echo.
pause