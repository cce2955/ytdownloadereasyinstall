REM Create and activate virtual environment
echo Creating and activating virtual environment...
python -m venv .venv
call .venv\Scripts\activate

REM Install yt-dlp
echo Installing yt-dlp...
pip install yt-dlp
pip install Pillow
pip install glob

REM Run Python script with GUI
echo Running the GUI...
python gui_script.py

REM Deactivate virtual environment
echo Deactivating virtual environment...
call .venv\Scripts\deactivate