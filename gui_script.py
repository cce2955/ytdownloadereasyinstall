from tkinter import *
from subprocess import call
import os

def get_url_and_download_audio(event=None):
    url = url_entry.get()
    call(["python", "download_audio.py", url])
    url_entry.delete(0, 'end')  # Clear the input field

def get_url_and_download_video(event=None):
    url = url_entry.get()
    call(["python", "video_downloader.py", url])
    url_entry.delete(0, 'end')  # Clear the input field

def on_enter(e):
    e.widget['background'] = 'lightblue'

def on_leave(e):
    e.widget['background'] = 'blue'

def on_click(e):
    e.widget['relief'] = SUNKEN

def on_release_audio(e):
    e.widget['relief'] = RAISED
    get_url_and_download_audio()  # Call download function on button release

def on_release_video(e):
    e.widget['relief'] = RAISED
    get_url_and_download_video()  # Call download function on button release

root = Tk()
root.geometry("400x400")  
root.title("YouTube Downloader")
root.configure(bg="light gray")

Label(root, text="Enter YouTube URL:", font=("Arial", 14), bg="lightgrey", fg="black").pack(pady=10)

url_entry = Entry(root, font=("Arial", 14))
url_entry.pack(pady=10)
url_entry.bind('<Return>', get_url_and_download_audio)  # Bind Enter key to the audio download function

download_audio_btn = Button(root, text="Download Audio", font=("Arial", 14), bg="blue", fg="white")
download_audio_btn.pack(pady=10)
download_audio_btn.bind("<Enter>", on_enter)
download_audio_btn.bind("<Leave>", on_leave)
download_audio_btn.bind("<Button-1>", on_click)
download_audio_btn.bind("<ButtonRelease-1>", on_release_audio)

download_video_btn = Button(root, text="Download Video", font=("Arial", 14), bg="blue", fg="white")
download_video_btn.pack(pady=10)
download_video_btn.bind("<Enter>", on_enter)
download_video_btn.bind("<Leave>", on_leave)
download_video_btn.bind("<Button-1>", on_click)
download_video_btn.bind("<ButtonRelease-1>", on_release_video)

root.mainloop()
