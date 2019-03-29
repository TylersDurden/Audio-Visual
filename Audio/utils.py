from scipy.io import wavfile
import numpy as np
import time
import os


def swap(file_name, destroy):
    data = []
    for line in open(file_name, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(file_name)
    return data


def load_wav(file_name):
    song = {}
    sample_rate, raw_data = wavfile.read(file_name)
    song['name'] = file_name.split('.')[0]
    song['sample_rate'] = sample_rate
    song['data'] = np.array(raw_data)
    return song


def load_mp3(file_name):
    name = file_name.split('.')[0].split('/')[len(file_name.split('.')[0].split('/'))-1]+'.wav'
    os.system('ffmpeg -i '+file_name+' ' +name)     # TODO: maybe make output invisible and clear after?
    song = {}
    try:
        sample_rate, raw_data = wavfile.read(name)
        song['name'] = name
        song['sample_rate'] = sample_rate
        song['data'] = np.array(raw_data)
    except ValueError:
        print "\033[1m\033[31m< Couldn't load song data >\033[0m"
    #os.system('rm '+name)
    return song


def find_wavs(verbose):
    locate = 'locate .wav >> command.txt'
    os.system(locate)
    songs = swap('command.txt', True)
    if verbose:
        print str(len(songs)) + ' WAVs Found'
    return songs


def find_mp3s(verbose):
    locate = 'locate *.mp3 >> command.txt'
    os.system(locate)
    songs = swap('command.txt', True)
    if verbose:
        print str(len(songs)) + ' MP3s Found'
    return songs


def play_wav(song):
    os.system('paplay '+song)


def thread_test(timeout):
    while True:
        print "Running?"
        time.sleep(timeout)