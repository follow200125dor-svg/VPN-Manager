@echo off
title VPN Manager - Installer
echo ============================================
echo    VPN MANAGER - INSTALLER
echo ============================================
echo.

echo [1/2] Checking Python...
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Downloading 3.14.2...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.14.2/python-3.14.2-amd64.exe' -OutFile 'python.exe'"
    echo Installing Python...
    python.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    del python.exe
    echo Python installed!
) else (
    echo Python OK
)

echo.
echo [2/2] No extra libraries needed!
echo Starting VPN Manager...
start python main.py
exit
