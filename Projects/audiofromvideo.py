from moviepy.editor import VideoFileClip
import subprocess

def extract_audio(video_path, audio_path):
    # Use FFmpeg to extract audio from the video and save it as a WAV file
    subprocess.call(['ffmpeg', '-i', video_path, '-vn', '-ac', '1', '-acodec', 'pcm_s16le', '-ar', '16000', audio_path])

# Specify the paths for the input video and output audio file
video_path = 'C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/Projects/Toko.mp4'
audio_path = 'C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/Projects/Fukawa.wav'

# Extract audio from the video
extract_audio(video_path, audio_path)

