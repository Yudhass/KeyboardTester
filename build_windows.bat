@echo off
setlocal
title Keyboard Tester - Build Script

echo =========================================
echo    Keyboard Tester - Build Script
echo =========================================
echo.

REM ================================
REM Check Python
REM ================================
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python tidak ditemukan.
    pause
    exit /b 1
)

echo [OK] Python ditemukan
python --version
echo.

REM ================================
REM Check file utama
REM ================================
if not exist "keyboard.py" (
    echo [ERROR] File keyboard.py tidak ditemukan!
    echo Pastikan file berada di folder yang sama dengan build.bat
    pause
    exit /b 1
)

if not exist "keyboard_icon.ico" (
    echo [WARNING] Icon tidak ditemukan, generating...
    python generate_icon.py
)

echo [OK] File keyboard.py ditemukan
echo.

REM ================================
REM Install / update pip
REM ================================
python -m pip install --upgrade pip >nul 2>&1

REM ================================
REM Install requirements jika ada
REM ================================
if exist "requirements.txt" (
    echo Installing dependencies...
    python -m pip install -r requirements.txt
)

REM ================================
REM Install PyInstaller jika belum ada
REM ================================
python -m pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing PyInstaller...
    python -m pip install pyinstaller
)

echo.
echo Membersihkan build sebelumnya...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist KeyboardTester.spec del /q KeyboardTester.spec
echo.

REM ================================
REM Build EXE
REM ================================
echo Building executable...
echo.

python -m PyInstaller ^
--onefile ^
--windowed ^
--clean ^
--noconfirm ^
--icon=keyboard_icon.ico ^
--name KeyboardTester ^
keyboard.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Build gagal!
    pause
    exit /b 1
)

echo.
echo =========================================
echo           BUILD BERHASIL
echo =========================================
echo.
echo File exe ada di:
echo   .\dist\KeyboardTester.exe
echo.
pause
endlocal
