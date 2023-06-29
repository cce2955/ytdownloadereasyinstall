from tkinter import *
from subprocess import call
import os

def get_url_and_download(event=None):
    """
    Function to fetch the URL from the GUI and call the audio download script.
    Also clears the entry field after initiating the download.
    """
    url = url_entry.get()
    call(["python", "download_audio.py", url])
    url_entry.delete(0, 'end')  # Clear the input field

def on_enter(e):
    """Function to create hover effect on button."""
    download_btn['background'] = 'lightblue'

def on_leave(e):
    """Function to remove hover effect when mouse leaves button."""
    download_btn['background'] = 'blue'

def on_click(e):
    """Function to create click-depress effect on button."""
    download_btn['relief'] = SUNKEN

def on_release(e):
    """Function to remove click-depress effect when mouse button is released."""
    download_btn['relief'] = RAISED
    get_url_and_download()  # Call download function on button release

root = Tk()
root.geometry("400x400")  # Set window size to 400x400
root.title("YouTube Audio Downloader")  # Set the title of the window
root.configure(bg="light gray")  # Set the background color

# Create a label with custom font and color
Label(root, text="Enter YouTube URL:", font=("Arial", 14), bg="lightgrey", fg="black").pack(pady=10)

url_entry = Entry(root, font=("Arial", 14))
url_entry.pack(pady=10)
url_entry.bind('<Return>', get_url_and_download)  # Bind Enter key to the function

download_btn = Button(root, text="Download", font=("Arial", 14), bg="blue", fg="white")
download_btn.pack(pady=10)

# Bind mouse events to the button
download_btn.bind("<Enter>", on_enter)
download_btn.bind("<Leave>", on_leave)
download_btn.bind("<Button-1>", on_click)
download_btn.bind("<ButtonRelease-1>", on_release)

root.mainloop()
