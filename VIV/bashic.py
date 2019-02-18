import matplotlib.pyplot as plt, matplotlib.animation as animation
import os


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def render_color(image_data, frame_rate):
    f = plt.figure()
    film = []
    for frame in image_data:
        film.append([plt.imshow(frame)])
    a = animation.ArtistAnimation(f, film, frame_rate, blit=True, repeat_delay=900)
    plt.show()


def render_bw(image_data, frame_rate):
    f = plt.figure()
    film = []
    for frame in image_data:
        film.append([plt.imshow(frame, 'gray')])
    a = animation.ArtistAnimation(f, film, frame_rate, blit=True, repeat_delay=900)
    plt.show()
