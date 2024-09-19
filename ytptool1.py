import moviepy.editor as mp
import yt_dlp
from pytube import YouTube

def download_video(url, output_path='downloaded_video.mp4'):
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def edit_video(input_path, output_path='edited_video.mp4'):
    # Load video
    clip = mp.VideoFileClip(input_path)

    # Example edits: cut the first 10 seconds and add a text overlay
    edited_clip = clip.subclip(10, clip.duration)
    txt_clip = mp.TextClip("YTP Chaos", fontsize=70, color='white')
    txt_clip = txt_clip.set_position('center').set_duration(edited_clip.duration)

    final_clip = mp.CompositeVideoClip([edited_clip, txt_clip])
    final_clip.write_videofile(output_path, codec='libx264')

def main():
    youtube_url = input("Enter the YouTube video URL: ")
    download_video(youtube_url)
    edit_video('downloaded_video.mp4')

if __name__ == "__main__":
    main()
