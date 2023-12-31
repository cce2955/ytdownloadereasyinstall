# YouTube Audio Downloader

YouTube Audio Downloader is a command line program that downloads audio from YouTube videos.

## Features

- Checks if Chocolatey, Python, and FFmpeg are installed, and installs them if not.
- Creates and uses a virtual environment.
- Downloads and uses yt-dlp to download the audio.
- GUI for user-friendly experience.
- Downloads audio in mp3 format.

## Installation

Clone the repository:

```bash
git clone https://github.com/cce2955/ytdownloadereasyinstall.git
cd youtube-audio-downloader
```
- Run "installer.bat", if it keeps running into an error, run "installer.bat" as Administrator.
- Once everything is installed, run "Download.bat"
- Paste your URL and click either Download Audio or Download Video
- Downloaded videos appear in the "Download" folder in the same directory

## Usage

When the GUI pops up:

1. Enter the YouTube video URL.
2. Click on the 'Download' button or press the Enter key.
3. The audio will be downloaded to a 'Downloads' folder in the script directory.
4. Enter another URL to download more audio, or close the GUI to exit the program.

## License

[MIT](https://choosealicense.com/licenses/mit/)
