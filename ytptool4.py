import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *
import random
import os
import youtube_dl

# GUI to input the video file
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        input_label.config(text=f"Input File: {file_path}")
        process_video(file_path)

def process_video(file_path):
    try:
        # Load video file
        video = VideoFileClip(file_path)

        # Generate random effects
        clips = []
        for i in range(5):  # Split the video into 5 random clips
            start = random.uniform(0, video.duration - 2)
            end = start + random.uniform(1, 2)
            clip = video.subclip(start, end)

            # Randomly reverse the clip
            if random.choice([True, False]):
                clip = clip.fx(vfx.time_mirror)

            # Add random speedup or slowdown
            speed_factor = random.uniform(0.5, 1.5)
            clip = clip.fx(vfx.speedx, speed_factor)

            clips.append(clip)

        # Concatenate and create chaotic output
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile("output_youtube_poop.mp4", codec="libx264")
        output_label.config(text="Video Processed and Saved!")
    except Exception as e:
        output_label.config(text=f"Error: {str(e)}")

# YouTube download function
def download_video():
    url = url_entry.get()
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloaded_video.mp4',
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        input_label.config(text="YouTube Video Downloaded!")
        process_video('downloaded_video.mp4')
    except Exception as e:
        input_label.config(text=f"Error: {str(e)}")

# Create tkinter GUI
root = tk.Tk()
root.title("YouTube Poop Chaos Generator")

# File input section
file_button = tk.Button(root, text="Select Video File", command=open_file)
file_button.pack()

input_label = tk.Label(root, text="No file selected")
input_label.pack()

# YouTube download section
url_label = tk.Label(root, text="YouTube URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="Download and Process", command=download_video)
download_button.pack()

# Output label
output_label = tk.Label(root, text="")
output_label.pack()

# Start GUI
root.mainloop()
