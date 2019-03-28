import jammin, utility, time, numpy as np


def create_mp3_lib(verbose):
    mp3_data = {}
    for tune in song_lib['MP3']:
        mp3_data[tune] = jammin.get_mp3_data(tune)
        if verbose:
            print list(tune.split('/')).pop() + ' Loaded into \033[1m\033[35mGroovis\033[0m'

    total_seconds = 0
    lengths = []
    for song in mp3_data.keys():
        print '\033[1m' + list(song.split('/')).pop() + ' =  ' + \
              str(mp3_data[song]['seconds']) + 's\033[0m'
        total_seconds += mp3_data[song]['seconds']
        lengths.append(mp3_data[song]['seconds'])
    minima = np.array(lengths).min()

    for song in mp3_data.keys():
        if mp3_data[song]['seconds'] == minima:
            print "shortest song is " + song

    hms = utility.sec_to_h_m_s(total_seconds)
    if verbose:
        print '------------------------------------\n' + str(hms[0]) + 'h:' + str(hms[1]) + 'm of MP3 Data Loaded'
        print '\033[1m\033[36m' + str(time.time() - t0) + 's Elapsed\033[0m'
    return mp3_data


t0 = time.time()
mp3s = utility.find_all_of_type('mp3', False)
wavs = utility.find_all_of_type('wav', False)
song_lib = {'MP3': mp3s, 'WAV': wavs}
mp3_data = create_mp3_lib(True)

shortest_song = mp3_data.keys().pop(len(mp3_data.keys())-2)
test_song_data = mp3_data[shortest_song]
# utility.reveal_dict(mp3_data, 'Song Library')