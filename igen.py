import matplotlib.pyplot as plt, matplotlib.animation as animation
import os, sys, scipy.ndimage as ndi, numpy as np


CARDINAL = {1: 'up', 2: 'down', 3: 'left', 4:'right', 5:'up left',
            6:'up right', 7: 'down left',8: 'down right', 9: 'self'}


def gen_zed(dims):
    width = dims[0]
    height = dims[1]

    state = np.zeros((width, height))
    depth = 10


def binarize(state):
    w_limit = np.array(state[:,:,0]).max() - np.array(state[:,:,0]).mean()/3
    b_limit = np.array(state)[:,:,0].min() + np.array(state[:,:,0]).max()/2
    print "White Err Limit: " + str(w_limit)
    print "Black Err Limit: " + str(b_limit)
    dims = np.array(state[:, :, 0]).shape
    c1 = np.array(state[:, :, 1]).flatten()
    c0 = np.array(state[:, :, 0]).flatten()

    ii = 0
    for pt in state.flatten():
        try:
            if pt > w_limit:
                c0[ii] = 1
            if pt <= b_limit:
                c0[ii] = 0
        except IndexError:
            break
        ii += 1
    # Now Color Channel 2

    ii = 0
    for pt in state.flatten():
        try:
            if pt > w_limit:
                c1[ii] = 1
            if pt <= b_limit:
                c1[ii] = 0
        except IndexError:
            break
        ii += 1
    f, ax = plt.subplots(1,3,sharey=True,sharex=True, figsize=(8,3))
    ax[0].imshow(c0.reshape(dims), 'gray')
    ax[1].imshow(c1.reshape(dims), 'gray')
    ax[2].imshow(state)
    plt.show()


def error_diffuse(state,weight):
    # Floyd-Steinberg
    # 1/16 [[0 0 7],[3 5 1]]
    err = [[0,0,7],
           [3,5,1]]
    erry = state + (ndi.convolve(state, err))/weight
    return erry


def render_BW(frames, frame_rate):
    f = plt.figure()
    reel = []
    for frame in frames:
        reel.append([plt.imshow(frame, 'gray_r')])
    a = animation.ArtistAnimation(f,reel,interval=frame_rate,blit=True,repeat_delay=900)
    plt.show()


def render_Color(frames, frame_rate):
    f = plt.figure()
    reel = []
    for frame in frames:
        reel.append([plt.imshow(frame)])
    a = animation.ArtistAnimation(f,reel,interval=frame_rate,blit=True,repeat_delay=900)
    plt.show()


def main():
    img_path = '/media/tylersdurden/CoopersDB/Images/Astronomical/andromeda.jpg'
    img_path_1 = '../TheGuardiansOfTomorrow/home.jpg'
    img_path_2 = 'Images/fruit-stand.jpg'

    test_image = np.array(plt.imread(img_path))
    # print "Shape: " + str(test_image.shape)
    # print "Min: " + str(test_image.min())
    # print "Max: " + str(test_image.max())
    # print "Avg: " + str(test_image.mean())

    # binarize(test_image)

    ch0 = error_diffuse(test_image[:, :, 0], 24)
    ch1 = error_diffuse(test_image[:, :, 1], 8)
    ch2 = error_diffuse(test_image[:, :, 2], 6)
    f, ax = plt.subplots(1,3,figsize=(8,4),sharex=True,sharey=True)
    ax[0].imshow(ch0, 'gray')
    ax[1].imshow(ch1, 'gray')
    ax[2].imshow(ch2, 'gray')
    plt.show()


if __name__ == '__main__':
    main()
