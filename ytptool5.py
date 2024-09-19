import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *
import random
from pytube import YouTube

# Function to add random effects for YTP style
def ytpify_clip(clip):
    # Apply a random transformation
    effects = [
        lambda c: c.fx(vfx.invert_colors),
        lambda c: c.fx(vfx.lum_contrast, lum=50, contrast=2),
        lambda c: c.fx(vfx.mirror_x),
        lambda c: c.fx(vfx.time_mirror),
        lambda c: c.speedx(random.uniform(0.5, 2)),  # random speed change
    ]
    effect = random.choice(effects)
    return effect(clip)

# Function to load video and apply YTP-style effects
def process_video(file_path):
    video = VideoFileClip(file_path)
    # Cut video into smaller random pieces and apply effects
    clips = []
    duration = video.duration
    for _ in range(10):  # Choose 10 random clips
        start = random.uniform(0, duration - 1)
        end = start + random.uniform(1, 3)
        subclip = video.subclip(start, end)
        subclip = ytpify_clip(subclip)
        clips.append(subclip)
    
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("output_ytp.mp4")

# Function to download video from YouTube
def download_youtube_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension="mp4").first()
    stream.download(filename="downloaded_video.mp4")
    process_video("downloaded_video.mp4")

# GUI for selecting video or YouTube link
def upload_file():
    file_path = filedialog.askopenfilename()
    process_video(file_path)

def download_video():
    url = url_entry.get()
    download_youtube_video(url)

# Create a simple Tkinter GUI
root = tk.Tk()
root.title("YouTube Poop Generator")

tk.Label(root, text="YTP Generator").pack()

# Upload video from file
upload_button = tk.Button(root, text="Upload Video File", command=upload_file)
upload_button.pack()

# Download and process YouTube video
tk.Label(root, text="Or enter YouTube URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="Download & Process Video", command=download_video)
download_button.pack()

root.mainloop()
