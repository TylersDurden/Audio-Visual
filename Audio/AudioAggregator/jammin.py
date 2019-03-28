import os, sys, utility
import numpy as np
from scipy.io import wavfile


def load_audio_data(song):
    sample_rate, raw_data = wavfile.read(song.split('.')[0] + '.wav')
    audio_data = np.array(raw_data)
    n_samples = audio_data.shape[0]
    song_length = float(n_samples) / sample_rate
    audio_info = {'sample_rate': sample_rate,
                  'n_samples': n_samples,
                  'seconds': song_length,
                  'data': audio_data}
    return audio_info


def convert_and_move(song):
    song_name = song.split('/')[len(song.split('/')) - 1]
    os.system('cp ' + song + ' $PWD;')
    os.system('ffmpeg -loglevel quiet -i ' + song_name + ' ' + song_name.split('.')[0] + '.wav')
    os.system('rm ' + song_name)
    return song_name.split('.')[0] + '.wav'


def get_mp3_data(song):
    data = load_audio_data(convert_and_move(song))
    os.system('rm ' + list(song.split('/')).pop().split('.')[0] + '.wav')
    return data


def main():

    if '-mp3' in sys.argv:
        if str(sys.argv[2]) not in utility.find_mp3(verbose=False):
            print "That song doesn't Exist"
            exit(0)
        music = get_mp3_data(str(sys.argv[2]))
        for property in music:
            if property != 'data':
                print '\033[1m\33[34m' + property + ' : ' + str(music[property]) + '\033[0m'


if __name__ == '__main__':
    main()
