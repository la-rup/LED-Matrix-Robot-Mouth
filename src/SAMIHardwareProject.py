import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from serial import Serial
import time
import os
import winsound
from collections import deque

# Ask user for WAV file path
wav_path = input("Enter WAV file path: ").strip()
if not os.path.isfile(wav_path):
    print("File not found. Please check path and try again.")
    exit()

# Get sampling rate and audio data from wav file
sample_rate, audio_data = wavfile.read(wav_path)

# Setting boundaries
frame_size = 1024
freq_range = (40, 600)
threshold = 10000
smooth_win = 5
volume_his = deque(maxlen = smooth_win)

# Convert wav audio from stereo to mono
if audio_data.ndim > 1:
    audio_data = np.mean(audio_data, axis=1)


# Start playing sound
winsound.PlaySound(wav_path, winsound.SND_ASYNC)

# Setting up serial connection to Arduino
arduino = Serial(port='COM5', baudrate=9600, timeout=0.1)
time.sleep(2)

for i in range(0, len(audio_data) - frame_size, frame_size):
    # Processing audio w/FFT
    frame = audio_data[i:i + frame_size]
    fft_done = fft(frame)
    freqs = fftfreq(frame_size, 1 / sample_rate)

    # Getting magnitudes and filtering for freqs > 0
    mags = np.abs(fft_done)
    pos_freqs = freqs > 0
    freq_band = pos_freqs & (freqs >= freq_range[0]) & (freqs <= freq_range[1])
    volume = np.mean(mags[freq_band])
    volume_his.append(volume)

    # Applying moving avg filter to smooth noise
    smooth_vol = np.mean(volume_his)
    print(f"Volume: {smooth_vol:.1f}")

    if smooth_vol > threshold:
        arduino.write(b"text:-\n")
    else:
        arduino.write(b"clear\n")

    time.sleep(frame_size / sample_rate)

arduino.write(b"clear\n")
arduino.close()