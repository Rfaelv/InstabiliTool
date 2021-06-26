@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="DESKTOP-KIEDSJK" (taskkill /f /pid 6472)
if /i "%LOCALHOST%"=="DESKTOP-KIEDSJK" (taskkill /f /pid 11156)

del /F cleanup-ansys-DESKTOP-KIEDSJK-11156.bat
