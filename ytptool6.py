import moviepy.editor as mp
import os
import random
from youtube_dl import YoutubeDL

class YTPTennisParser:
    def __init__(self):
        self.rounds = []
    
    def add_round(self, player_name, video_file):
        """ Add a round to the tennis match """
        round_data = {
            'player': player_name,
            'video': video_file
        }
        self.rounds.append(round_data)

    def show_match(self):
        """ Display the tennis match rounds """
        for i, r in enumerate(self.rounds):
            print(f"Round {i+1}: Player {r['player']} - Video: {r['video']}")

    def get_last_video(self):
        """ Return the last video of the match for editing """
        return self.rounds[-1]['video'] if self.rounds else None

class YTPTennis:
    def __init__(self):
        self.parser = YTPTennisParser()
    
    def download_video(self, url, output_file):
        """ Download video from YouTube using youtube_dl """
        ydl_opts = {
            'format': 'best',
            'outtmpl': output_file
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    
    def apply_random_effects(self, input_file, output_file):
        """ Apply random effects to a video using moviepy """
        video = mp.VideoFileClip(input_file)
        effects = [self.reverse_video, self.fade_in_out]
        effect = random.choice(effects)
        edited_video = effect(video)
        edited_video.write_videofile(output_file, codec='libx264')
    
    def reverse_video(self, video_clip):
        """ Reverse a video """
        return video_clip.fx(mp.vfx.time_mirror)
    
    def fade_in_out(self, video_clip):
        """ Apply fade-in and fade-out effect """
        return video_clip.fadein(1).fadeout(1)
    
    def add_round(self, player_name, video_file):
        """ Add a new round to the YTP tennis game """
        self.parser.add_round(player_name, video_file)
    
    def play_tennis(self, player_name, video_url=None, video_file=None):
        """ Play a round of YTP Tennis """
        if video_url:
            print(f"Downloading video from {video_url}...")
            download_file = f"{player_name}_round.mp4"
            self.download_video(video_url, download_file)
            video_file = download_file
        
        # If it's not the first round, take the last video and apply effects
        if len(self.parser.rounds) > 0:
            last_video = self.parser.get_last_video()
            output_file = f"{player_name}_edited.mp4"
            self.apply_random_effects(last_video, output_file)
            video_file = output_file
        
        self.add_round(player_name, video_file)
    
    def show_match(self):
        """ Display the match rounds """
        self.parser.show_match()

# Example Usage:
# yt_tennis = YTPTennis()
# yt_tennis.play_tennis("Player1", video_url="https://www.youtube.com/watch?v=example")
# yt_tennis.play_tennis("Player2")
# yt_tennis.show_match()
