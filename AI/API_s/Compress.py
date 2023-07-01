import numpy as np
from scipy.io import wavfile

# Load the raw audio file
sample_rate, audio_data = wavfile.read('C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/AI/API_s/Deeper.wav')

# Set the desired sample rate for downsampling
desired_sample_rate = 16000

# Perform downsampling
downsampled_audio_data = audio_data[::int(sample_rate / desired_sample_rate)]

# Save the downsampled audio as a new raw file
wavfile.write('C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/AI/API_s/Deeper_downsampled.wav', desired_sample_rate, downsampled_audio_data)
