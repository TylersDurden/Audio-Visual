import os, sys
import numpy as np
from scipy.io import wavfile


def load_audio_data(song):
    sample_rate, raw_data = wavfile.read(song.title)
    audio_data = np.array(raw_data)
    n_samples = audio_data.shape[0]
    song_length = float(n_samples) / sample_rate
    audio_info = {'sample_rate': sample_rate,
                  'n_samples': n_samples,
                  'seconds': song_length,
                  'data': audio_data}
    return audio_info


def convert_and_move(song):
    song_name = song.source.split('/')[len(song.source.split('/')) - 1]
    os.system('cp ' + song.source + ' $PWD;')
    os.system('ffmpeg -loglevel quiet -i ' + song_name + ' ' + song_name.split('.')[0] + '.wav')
    os.system('rm ' + song_name)
    return song_name.split('.')[0] + '.wav'


def get_mp3_data(song):
    return load_audio_data(convert_and_move(song))


def main():

    if '-mp3' in sys.argv:
        # TODO: check that song exists first
        music = get_mp3_data(sys.argv[2])
        for property in music:
            print '\033[1m' + property + ' : ' + music[property]


if __name__ == '__main__':
    main()
