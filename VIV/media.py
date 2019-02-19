import matplotlib.pyplot as plt, numpy as np
import os, sys, bashic, vidivarium
import scipy.ndimage as ndi, time

def video2images(original_video, frame_rate):
    name = original_video.split('.')[0]
    os.system('mkdir '+name)
    cmd = 'p=$PWD; ffmpeg -i ../Video/' + original_video + ' ' + name + \
          '/%d.png -vf fps=' + str(frame_rate)
    os.system(cmd+'; clear')
    print '\033[1m\033[34m' + original_video+' Converted To:'+'\033[0m'
    os.system('ls '+name)
    return name


def cleanup(folder):
    cmd = 'ls '+folder+'/ | while read n; do rm '+folder+'/$n; done'
    os.system(cmd)
    os.system('rmdir '+folder)


def find_files(folder):
    os.system('ls '+folder+' >> images.txt')
    data = []
    imgs = bashic.swap('images.txt', True)
    for img in imgs:
        file_name = folder+'/'+img
        data.append(plt.imread(file_name))
    return data


class VideoEntity:
    label = ''
    n_frames = 0
    frame_rate = 0
    dimensions = []
    data = [[]]
    state = [[]]
    verbose = False

    def __init__(self, video_name, image_data, frame_rate, verbosity):
        """
        //////|_________INITIALIZE VIDEO ENTITY OBJECT________|\\\\\\
        :param video_name:
        :param image_data:
        :param frame_rate:
        :param verbosity:
        """
        self.label = video_name
        self.data = image_data
        self.n_frames = len(image_data)
        self.frame_rate = frame_rate
        self.state = image_data[0]
        self.dimensions = self.state.shape
        self.verbose = verbosity

        # If Verbose display the parameter initializations
        if self.verbose:
            print "PROCESSING " + video_name
            print "Frame Rate: " + str(self.frame_rate)
            print "Dimensions: " + str(self.dimensions)
            print "Num Frames: " + str(self.n_frames)

    def show(self, isBW, save, file_name):
        """
        Render Image data
        :return:
        """
        if not isBW and len(self.dimensions) > 2:
            bashic.render_color(self.data, self.frame_rate)
        elif isBW:
            bashic.render_bw(self.data, self.frame_rate,save, file_name)

    def slow_motion(self, N):
        """
        Copy each frame N times, and reassemble into new
        video data stream. Shown with original frame rate,
        the new film is in slow motion by a factor of N.
        :param N:
        :return:
        """
        new_data = []
        for frame in self.data:
            for i in range(N):
                new_data.append(frame)
        self.data = new_data
        self.show(False, False, '')

    @staticmethod
    def fs_error_diffusion(state, weight):
        kern = [[3,3,1],
                [5,2,3],
                [3,5,1]]

        k = [[2,2,2,2,2],
             [2,1,3,1,2],
             [2,3,5,3,2],
             [2,1,3,1,2],
             [2,2,2,2,2]]

        return(ndi.convolve(np.array(state), np.array(k)))/weight - state

    def binarize(self, extra):
        new_film = []
        for frame in self.data:
            if extra:
                next_frame = self.hollywood(frame[:,:,0]/3+frame[:,:,2]/3+frame[:,:,1]/3, 3)
                new_film.append(8*next_frame + frame[:,:,0]/3)
            else:
                filtered_frame = frame[:, :, 2] + frame[:, :, 1] / 4 + \
                                 frame[:, :, 0] / (1 + self.fs_error_diffusion(frame[:, :, 0], 12))
                new_film.append(filtered_frame)
        print new_film.pop().shape
        self.data = new_film

    def hollywood(self, state, level):
        k = [[1,1,1],[1,0,1],[1,1,1]]
        new_state = np.array(state).flatten()
        ii = 0
        for cell in ndi.convolve(state,k).flatten():
            if cell >= level:
                new_state[ii] += 2
            else:
                new_state[ii] -= 1
            ii += 1
        return new_state.reshape(state.shape)


def main():
    t0 = time.time()
    # Convert a video to a bunch of images
    if '-demo' in sys.argv:
        test = 'tre.mp4'
        name = video2images(test, 30)
        image_data = find_files(name)

        # Virtualizing the image data for recreating video, but with effects
        video = VideoEntity(test, image_data, 30, True)

        if 'slowmo' in sys.argv:
            video.slow_motion(5)

        if 'expose' in sys.argv:
            vidivarium.time_evolving_exposure_inversion(video.data,
                                                        video.frame_rate,
                                                        video.label,
                                                        depth=4)
            # frame = video.data[23]
            # vidivarium.explore(frame[:,:,1])
        print "Finished."
        # When finished clean up the whole directory of images
        cleanup(name)
        exit(0)

    elif len(sys.argv) > 1:
        video_file = sys.argv[1]
        vdata = video2images(video_file, 45)
        images = find_files(vdata)

        # Instantiate the entire video for processing
        video = VideoEntity(video_file, images, 30, True)
        if '-b' not in sys.argv:
            video.binarize(False)
            # When finished clean up the whole directory of images
            cleanup(vdata)
            print '\033[1m\033[31m[' + str(time.time() - t0) + 's Elapsed]\033[0m'
            video.show(True, True, 'special_fx_'+video_file)
            exit(0)
        else:
            video.binarize(True)
            print '\033[1m\033[31m['+str(time.time()-t0)+'s Elapsed]\033[0m'
            # When finished clean up the whole directory of images
            cleanup(vdata)
            video.show(True,True, 'light_filter_'+video_file)
            exit(0)


if __name__ == '__main__':
    main()
