import sys
import os
import subprocess

def download_audio(url):
    """
    Function to download audio from a YouTube video given its URL.
    The URL is processed to ensure it is treated as an individual video even if copied from a playlist.
    Audio is downloaded using yt-dlp and saved to a 'Downloads' folder in the script's directory.
    """
    url = url.split('&')[0]  # Remove everything from '&' onward
    output_directory = os.path.join(os.getcwd(), "Downloads")
    os.makedirs(output_directory, exist_ok=True)  # Ensure the directory exists

    cmd = f'yt-dlp {url} --extract-audio --audio-format mp3 -o "{os.path.join(output_directory, "%(title)s.%(ext)s")}"'
        
    subprocess.run(cmd, shell=True)

if __name__ == '__main__':
    download_audio(sys.argv[1])
