from tkinter import *
import time
#from PIL import ImageTk

root = Tk()
"""
start_time = time.time()

frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_s2h.gif',format = 'gif -index %i' %(i)) for i in range(34)]
end_time = time.time()
print('read from gif: {}'.format(end_time-start_time))
"""
"""
for i in range(34):
    f = frames[i]
    f.write('/home/pi/Pictures/test/{}.gif'.format(i))

print('done')
"""
start_time = time.time()
new_frames = []
for i in range(34):
    new_frames.append(PhotoImage(file='/home/pi/Pictures/Emotion Gifs/frames/gif_s2h{}.gif'.format(i)))
end_time = time.time()                      
print('read from frames: {}'.format(end_time-start_time))

frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/frames/gif_s2h{0}.gif'.format(i)) for i in range(34)]
print('done')



