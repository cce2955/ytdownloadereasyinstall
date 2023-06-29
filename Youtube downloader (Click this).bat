@echo off
setlocal EnableDelayedExpansion

REM Check if Chocolatey is installed
choco -v >nul 2>&1
if %errorlevel% neq 0 (
    echo Chocolatey is not installed. Installing Chocolatey...
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
)

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python...
    choco install python -y
)

REM Check if FFmpeg is installed
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo FFmpeg is not installed. Installing FFmpeg...
    choco install ffmpeg -y
)

REM Create and activate virtual environment
echo Creating and activating virtual environment...
python -m venv .venv
call .venv\Scripts\activate

REM Install yt-dlp
echo Installing yt-dlp...
pip install yt-dlp

REM Run Python script with GUI
echo Running the GUI...
python gui_script.py

REM Deactivate virtual environment
echo Deactivating virtual environment...
call .venv\Scripts\deactivate
