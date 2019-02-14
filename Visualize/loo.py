import resource, os, matplotlib.pyplot as plt, matplotlib.animation as animation, numpy as np
from matplotlib.animation import FFMpegWriter


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def bw_render(frames, frame_rate, save, fileNameOut):
    f = plt.figure()
    film = []
    for frame in frames:
        film.append([plt.imshow(frame, 'gray_r')])
    a = animation.ArtistAnimation(f, film, interval=frame_rate, blit=True, repeat_delay=900)
    if save:
        writer = FFMpegWriter(fps=frame_rate, metadata=dict(artist='Me'), bitrate=1800)
        a.save(fileNameOut, writer=writer)
    plt.show()


def color_render(frames, frame_rate, save, fileNameOut):
    f = plt.figure()
    film = []
    for frame in frames:
        film.append([plt.imshow(frame, 'rainbow')])
    a = animation.ArtistAnimation(f, film, interval=frame_rate, blit=True, repeat_delay=900)
    if save:
        writer = FFMpegWriter(fps=frame_rate, metadata=dict(artist='Me'), bitrate=1800)
        a.save(fileNameOut, writer=writer)
    plt.show()


def check_mem_usage():
    """
    Return the amount of RAM usage, in bytes, being consumed currently.
    :return (integer) memory:
    """
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return mem


def dump_file(path_to_file):
    os.system('hexdump -C ' + path_to_file + ' >> dump.txt')
    dump = {}
    raw_dump_data = swap('dump.txt', True)
    line_number = 1
    for line in raw_dump_data:
        word = line.split(' ')[0]
        try:
            data = line.split(word)[1].split('|')[0]
        except:
            continue
        try:
            text = line.split(' |')[1].replace('|', '')
        except IndexError:
            text = ''
            continue
        dump[line_number] = [word, data, text]
        line_number += 1
    return dump


class File2Video:
    src = ''

    def __init__(self, path_to_file):
        self.src = path_to_file
        data = dump_file(self.src)
        for line in data:
            os.system("printf '%d\n' 0x"+data[line][0]+' >> x.txt')
            x = swap('x.txt', True)


p = '../LICENSE'
File2Video(p)
