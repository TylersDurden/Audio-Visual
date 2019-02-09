import matplotlib.pyplot as plt
import numpy as np, scipy.ndimage as ndi
import time, media, bashic


def time_evolving_exposure_inversion(data, frame_rate, label, depth):
    t0 = time.time()
    reel = []

    for frame in data:
        # maxima = np.array(frame).max()
        # minima = np.array(frame).min()
        # average = np.array(frame).mean()
        reel.append(explore(frame[:,:,2]))

    print '\033[1m\033[34m Finished Simulating ' + str(len(data)*depth) +\
          "Frames ["+str(time.time()-t0)+'s]\033[0m'
    bashic.render_bw(reel, 17)


def expose(image, filter_name):
    f0 = [[1,1,1,1,1],
          [1,0,0,0,1],
          [1,0,1,0,1],
          [1,0,0,0,1],
          [1,1,1,1,1]]
    filters = {'spread':f0}
    filt = filters[filter_name]
    dims = np.array(image).shape
    imat = np.array(image).flatten()
    # f, ax = plt.subplots(1, 2)
    # ax[0].imshow(np.array(image), 'gray_r')
    ii = 0
    for cell in ndi.convolve(image,f0).flatten():
        if cell > 3*imat[ii]:
            imat[ii] -= 10
        ii += 1
    return imat.reshape(dims)


def explore(image):
    dims = np.array(image).shape
    data = np.array(image).flatten()
    average = np.array(image).mean()
    ii = 0
    for cell in image.flatten():
        if cell > average:
            data[ii] -= 3
        if cell < average:
            data[ii] += 3
        ii += 1

    # ax[1].imshow(data.reshape(dims), 'gray_r')
    # plt.show()
    return data.reshape(dims)