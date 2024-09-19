import moviepy.editor as mp
import random

# Load your input video
input_video_path = "input_video.mp4"
output_video_path = "ytp_output.mp4"

# Load the video clip
video = mp.VideoFileClip(input_video_path)

# Function to create chaotic effects
def apply_random_effects(clip):
    effects = []

    # Reverse clip (common in YTP)
    if random.choice([True, False]):
        clip = clip.fx(mp.vfx.time_mirror)

    # Speed up or slow down clip
    if random.choice([True, False]):
        clip = clip.fx(mp.vfx.speedx, factor=random.uniform(0.5, 2))

    # Add rotation
    if random.choice([True, False]):
        clip = clip.rotate(random.randint(0, 360))

    # Random color effect
    if random.choice([True, False]):
        clip = clip.fx(mp.vfx.colorx, random.uniform(0.5, 2))

    # Apply random subclip
    if random.choice([True, False]):
        start = random.uniform(0, clip.duration - 1)
        end = random.uniform(start, clip.duration)
        clip = clip.subclip(start, end)

    return clip

# Create segments of the video and apply random effects
clips = []
segment_duration = 3  # Segment duration in seconds
for i in range(0, int(video.duration), segment_duration):
    segment = video.subclip(i, min(i + segment_duration, video.duration))
    segment_with_effects = apply_random_effects(segment)
    clips.append(segment_with_effects)

# Concatenate all clips
final_clip = mp.concatenate_videoclips(clips)

# Write the final output
final_clip.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

print(f"YTP-style video saved to {output_video_path}")
