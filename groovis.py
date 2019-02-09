import jammin, utility, time

t0 = time.time()
mp3s = utility.find_all_of_type('mp3', False)
wavs = utility.find_all_of_type('wav', False)
song_lib = {'MP3': mp3s, 'WAV': wavs}

mp3_data = {}
for tune in song_lib['MP3']:
    mp3_data[tune] = jammin.get_mp3_data(tune)
    print list(tune.split('/')).pop() + ' Loaded into \033[1m\033[35mGroovis\033[0m'

total_seconds = 0
for song in mp3_data.keys():
    print '\033[1m'+ list(song.split('/')).pop() + ' =  ' +\
          str(mp3_data[song]['seconds']) + 's\033[0m'
    total_seconds += mp3_data[song]['seconds']
print '------------------------------------\n' + str(total_seconds) + 's of MP3 Data Loaded'
print '\033[1m\033[36m' + str(time.time()-t0) + 's Elapsed\033[0m'
utility.sec_to_h_m_s(total_seconds)