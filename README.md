# media.py
Images are grids of numbers. Using FFMpeg we can convert a video 
into a number of still images. Creating a VideoEntity object with 
this information you can manipulate the images and replay them. 

### Slow-Mo
* Scale the number of frames in the video by a factor N, and
  copy each frame N times. When splicing the result together, and
  playing back at the original frame rate, the result is a slower
  video effect. 
