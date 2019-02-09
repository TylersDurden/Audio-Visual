import os, numpy as np


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def find_mp3(verbose):
    os.system('locate *.mp3 >> mp3s.txt;clear')
    mp3s = swap('mp3s.txt', True)
    if verbose:
        print str(len(mp3s)) + " MP3s Found:"
        for tune in mp3s:
            print tune
    return mp3s


def find_WAVs(verbose):
    os.system('locate *.wav >> wavs.txt')
    wavs = swap('wavs.txt', True)
    if verbose:
        print str(len(wavs)) + " WAVs Found:"
        for tune in wavs:
            print tune
    return wavs


def find_all_of_type(type, verbose):
    os.system('locate *.'+str(type)+' >> '+str(type)+'.txt; clear')
    files = swap(str(type)+'.txt', True)
    if verbose:
        print str(len(files)) + str(type) + "s Found:"
        for f in files:
            print f
    return files


def sec_to_h_m_s(seconds):
    hms = []
    if seconds > 3600:
        hours = float(seconds)/float(3600)
        min = (float(seconds)/float(3600)-int(hours))*60
        print str(int(hours)) + " hours and " + str(int(min))+" mins"
    return [hours, min]
