from moviepy.editor import *

clip = VideoFileClip("The Super Mario Effect - Tricking Your Brain into Learning More  Mark Rober  TEDxPenn.mp4").\
    subclip(1, 15).resize(0.3)
clip.preview()
print("done")