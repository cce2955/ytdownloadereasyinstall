import sys
import os
import subprocess
import time
import shutil
import glob 

def download_video(url):
    """
    Function to download a video from a YouTube URL.
    The URL is processed to ensure it is treated as an individual video even if copied from a playlist.
    The video is downloaded using yt-dlp and saved to a temporary 'tmp' folder in the script's directory.
    The completed video file is moved to the 'Downloads' folder.
    """
    url = url.split('&')[0]  # Remove everything from '&' onward
    temp_directory = os.path.join(os.getcwd(), "tmp")
    output_directory = os.path.join(os.getcwd(), "Downloads")
    os.makedirs(temp_directory, exist_ok=True)  # Ensure the temporary directory exists
    os.makedirs(output_directory, exist_ok=True)  # Ensure the output directory exists

    cmd = f'yt-dlp -f best {url} -o "{os.path.join(temp_directory, "%(title)s.%(ext)s")}"'
    subprocess.run(cmd, shell=True)

    time.sleep(1)

    glob_pattern = os.path.join(temp_directory, "*.*")
    files = glob.glob(glob_pattern)

    if not files:
        print(f"No files found matching pattern {glob_pattern}")
        return

    video_files = [file for file in files if file.endswith('.mp4')]

    if not video_files:
        print("No video files for processing found.")
        return

    output_file = video_files[0]

    shutil.move(output_file, os.path.join(output_directory, os.path.basename(output_file)))
    shutil.rmtree(temp_directory)

if __name__ == '__main__':
    download_video(sys.argv[1])
