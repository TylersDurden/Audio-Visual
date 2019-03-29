import matplotlib.pyplot as plt
import numpy as np
import utils
from threading import Thread


sounds = utils.find_wavs(verbose=True)
songs = utils.find_mp3s(verbose=True)
t = 4   # 4 Is a good test bleep
# Using a single track for testing on at a time
#test_sound = utils.load_wav(sounds[0])
#audio = test_sound['data']


test_song_short = utils.load_mp3(songs[9])
test_song_audio = test_song_short['data']
print '\033[1m'+test_song_short['name']+'\033[0m'
print test_song_audio.shape

print test_song_short['name'] + '\033[1m\033[34m LOADED\033[0m'
listen = Thread(target=utils.play_wav, args=(test_song_short['name'],))
