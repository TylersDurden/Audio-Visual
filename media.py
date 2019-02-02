import matplotlib.pyplot as plt
import os, sys, bashic, vidivarium


def video2images(original_video, frame_rate):
    name = original_video.split('.')[0]
    os.system('mkdir '+name)
    cmd = 'p=$PWD;cd '+name+'; ffmpeg -i $p/Video/' + original_video + ' ' + name + \
          '%d.png -vf fps=' + str(frame_rate)
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

    def show(self):
        """
        Render Image data
        :return:
        """
        if len(self.dimensions) > 2:
            bashic.render_color(self.data, self.frame_rate)
        else:
            bashic.render_bw(self.data, self.frame_rate)

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
        self.show()


def main():
    # Convert a video to a bunch of images
    if '-demo' in sys.argv:
        test = 'tre.mp4'
        name = video2images(test, 25)
        image_data = find_files(name)

        # Virtualizing the image data for recreating video, but with effects
        video = VideoEntity(test, image_data, 25, True)

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


if __name__ == '__main__':
    main()
