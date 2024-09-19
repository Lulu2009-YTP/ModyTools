from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip
import random

def create_ytp(video_path, output_path, text_clips):
    # Load the main video
    video = VideoFileClip(video_path)
    
    # Create a list to hold all video segments
    segments = []

    # Add the main video clip
    segments.append(video)

    # Add random text clips as a parody effect
    for text in text_clips:
        txt_clip = (TextClip(text, fontsize=70, color='white', bg_color='black')
                    .set_duration(random.uniform(1, 5))  # Random duration between 1 and 5 seconds
                    .set_position('center'))
        segments.append(txt_clip)

    # Concatenate all segments
    final_clip = concatenate_videoclips(segments)
    
    # Write the final video to a file
    final_clip.write_videofile(output_path, codec='libx264')

# Example usage
if __name__ == "__main__":
    video_path = "input_video.mp4"
    output_path = "output_ytp.mp4"
    text_clips = [
        "What if I told you...",
        "The ultimate meme!",
        "YTP Edition",
        "Subscribe now!"
    ]

    create_ytp(video_path, output_path, text_clips)
