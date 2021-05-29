@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="DESKTOP-KIEDSJK" (taskkill /f /pid 13396)
if /i "%LOCALHOST%"=="DESKTOP-KIEDSJK" (taskkill /f /pid 8520)

del /F cleanup-ansys-DESKTOP-KIEDSJK-8520.bat
