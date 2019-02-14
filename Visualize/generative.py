import matplotlib.pyplot as plt, matplotlib.animation as animation
import numpy as np, scipy.ndimage as ndi


class Kernel:

    seeds = list()
    n_generations = 0
    state = [[]]

    def __init__(self, seeds, ngen, dimensions):
        self.seeds = seeds
        self.n_generations = ngen
        self.state = np.zeros(dimensions)
        self.define_kernel_limits()

    def define_kernel_limits(self):
        permute = []
        frames = []
        largest = []
        random_seed = {}
        for j in range(len(self.seeds)):
            size = np.array(self.seeds[j]).shape[0]*np.array(self.seeds[j]).shape[1]
            largest.append(size)
            random_seed[size] = self.seeds[j]
        c = np.random.random_integers(0,1, random_seed[size].shape[0]*random_seed[size].shape[1]).reshape(random_seed[size].shape)
        for i in range(len(self.seeds)):
            c = random_seed[largest.pop()]
            # ksum = np.array(self.seeds[i]).sum()
            # cycle = np.random.random_integers(0, 1, self.seeds[i].shape[0]*self.seeds[i].shape[1])
            # c = cycle.reshape(self.seeds[i].shape)
            # csum = np.array(c).sum()
            permute.append(c)
            # img = ndi.convolve(self.seeds[i], c) + c
            # frames.append([plt.imshow(self.seeds[i], 'gray_r')])
            # frames.append([plt.imshow(img, 'gray_r')])
            frames.append([plt.imshow(ndi.convolve(self.seeds[i], c), 'gray')])
        f = plt.figure()
        a = animation.ArtistAnimation(f,frames,interval=200,blit=True,repeat_delay=900)
        plt.show()


def main():
    k0 = np.array([[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]])

    k1 = np.array([[1, 1, 1, 1],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [1, 1, 1, 1]])

    k2 = np.array([[1, 1, 1, 1, 1],
          [1, 0, 0, 0, 1],
          [1, 0, 0, 0, 1],
          [1, 0, 0, 0, 1],
          [1, 1, 1, 1, 1]])

    k3 = np.array([[2, 2, 2, 2],
          [2, 1, 1, 2],
          [2, 1, 1, 2],
          [2, 2, 2, 2]])

    k4 = np.array([[2, 2, 2, 2, 2],
                   [2, 1, 1, 1, 2],
                   [2, 1, 0, 1, 2],
                   [2, 1, 1, 1, 2],
                   [2, 2, 2, 2, 2]])

    k5 = np.array([[2,2,2,2,2,2],
                   [2,1,1,1,1,2],
                   [2,1,0,0,1,2],
                   [2,1,0,0,1,2],
                   [2,1,1,1,1,2],
                   [2,2,2,2,2,2]])

    k6 = np.array([[1,1,1,2,2,2],
                   [1,0,1,2,0,2],
                   [1,1,1,2,2,2],
                   [2,2,2,1,1,1],
                   [2,0,2,1,0,1],
                   [2,2,2,1,1,1]])

    k7 = np.array([[2,2,2,1,1,2,2,2],
          [2,1,1,1,1,1,1,2],
          [2,1,0,1,1,0,1,2],
          [1,1,1,2,2,1,1,1],
          [1,1,1,2,2,1,1,1],
          [2,1,0,1,1,0,1,2],
          [2,1,1,1,1,1,1,2],
          [2,2,2,1,1,2,2,2]])

    k8 = np.array([[2,2,2,2,2,2,2,2,2],
                   [2,1,1,1,2,1,1,1,2],
                   [2,1,0,1,2,1,0,1,2],
                   [2,1,1,1,2,1,1,1,2],
                   [2,2,2,2,2,2,2,2,2],
                   [2,1,1,1,2,1,1,1,2],
                   [2,1,0,1,2,1,0,1,2],
                   [2,1,1,1,2,1,1,1,2],
                   [2,2,2,2,2,2,2,2,2]])

    life_time = 100
    k = Kernel([k0, k1, k2, k3, k4, k5, k6, k7, k8],
               life_time, [250, 250])


if __name__ == '__main__':
    main()
