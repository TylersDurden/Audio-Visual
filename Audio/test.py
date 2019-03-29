import matplotlib.pyplot as plt
import scipy.signal as signal
from threading import Thread
import numpy as np
import utils
import os


sounds = utils.find_wavs(verbose=False)
songs = utils.find_mp3s(verbose=False)
bleep = sounds[4]   # 4 Is a good test bleep


test_song_short = utils.load_mp3(songs[12])
test_song_audio = test_song_short['data']
os.system('clear')

print test_song_short['name'] + '\033[1m\033[34m LOADED\033[0m'
listen = Thread(target=utils.play_wav, args=(test_song_short['name'],))
listen.start()
song_length_seconds = test_song_audio.shape[0]/44100
song_length_minutes = str(song_length_seconds/60)+':'+\
                      str(int((float(song_length_seconds)/60 - song_length_seconds/60)*60))

print " Song Length:" + song_length_minutes

audio_left = test_song_audio[:, 0]
audio_right = test_song_audio[:, 1]

sample = test_song_audio[0:test_song_short['sample_rate']*3, :]
# plt.plot(sample)
# plt.show()

dt = 44100
t = 0
for frame in range(song_length_seconds):
    dt = frame*dt
    dat = test_song_audio[t:dt, :]
    t += dt

os.system('rm '+test_song_short['name'])
