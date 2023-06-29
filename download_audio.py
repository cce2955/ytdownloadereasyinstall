import sys
import os
import subprocess
import json
import glob
import time
import shutil
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1
from PIL import Image

def download_audio(url):
    """
    Function to download audio from a YouTube video given its URL.
    The URL is processed to ensure it is treated as an individual video even if copied from a playlist.
    Audio is downloaded using yt-dlp and saved to a temporary 'tmp' folder in the script's directory.
    Also downloads the video thumbnail, converts it to jpg if necessary, and embeds it into the mp3 file.
    Writes metadata to a .json file and sets it in the mp3 file.
    The completed mp3 file is moved to the 'Downloads' folder.
    """
    url = url.split('&')[0]  # Remove everything from '&' onward
    temp_directory = os.path.join(os.getcwd(), "tmp")
    output_directory = os.path.join(os.getcwd(), "Downloads")
    os.makedirs(temp_directory, exist_ok=True)  # Ensure the temporary directory exists
    os.makedirs(output_directory, exist_ok=True)  # Ensure the output directory exists

    cmd = f'yt-dlp {url} --extract-audio --audio-format mp3 --write-thumbnail --write-info-json -o "{os.path.join(temp_directory, "%(title)s.%(ext)s")}"'
    subprocess.run(cmd, shell=True)

    # Wait for a bit before accessing the file
    time.sleep(1)

    # Get the path of the thumbnail file (could be .jpg or .webp)
    glob_pattern = os.path.join(temp_directory, "*.*")
    files = glob.glob(glob_pattern)

    if not files:
        print(f"No files found matching pattern {glob_pattern}")
        return

    # Segregate files based on their extensions
    mp3_files = [file for file in files if file.endswith('.mp3')]
    thumbnail_files = [file for file in files if file.endswith('.jpg') or file.endswith('.webp')]
    json_files = [file for file in files if file.endswith('.info.json')]

    # If there's no mp3 file, or thumbnail file, or json file, then return
    if not mp3_files or not thumbnail_files or not json_files:
        print("Necessary files for processing are missing.")
        return

    # Select the first mp3 file, thumbnail file and json file (assuming there's only one of each per run)
    output_file = mp3_files[0]
    thumbnail_file = thumbnail_files[0]
    json_file = json_files[0]

    if thumbnail_file.endswith('.webp'):
        # Convert .webp thumbnail to .jpg
        img = Image.open(thumbnail_file).convert("RGB")
        img.save(output_file.replace('.mp3', '.jpg'), "jpeg")
        thumbnail_file = output_file.replace('.mp3', '.jpg')

    # Embed album art into mp3 file
    audio = MP3(output_file, ID3=ID3)
    audio.tags.add(
        APIC(
            encoding=3,
            mime='image/jpeg',
            type=3,
            desc=u'Cover',
            data=open(thumbnail_file, 'rb').read()
        )
    )

    # Set metadata in mp3 file
    with open(json_file, encoding='utf-8') as f:
        metadata = json.load(f)
    audio.tags.add(TIT2(encoding=3, text=metadata['title']))
    audio.tags.add(TPE1(encoding=3, text=metadata['uploader']))
    audio.save()


    # Move the completed file to the output directory
    shutil.move(output_file, os.path.join(output_directory, os.path.basename(output_file)))

    # Delete the temporary directory
    shutil.rmtree(temp_directory)

if __name__ == '__main__':
    download_audio(sys.argv[1])
