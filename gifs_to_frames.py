from tkinter import *
import os

root = Tk()
files = os.listdir('/home/pi/Pictures/ResizedGIFs')
print(files)
file_prefixes = [f.split(".")[0] for f in files]

for f in file_prefixes:
    print(f)
    print()
    frames = [PhotoImage(file='/home/pi/Pictures/ResizedGIFs/{}.gif'.format(f) \
                         ,format = 'gif -index %i' %(i)) for i in range(34)]
    for i in range(34):
        frame = frames[i]
        frame.write('/home/pi/Pictures/frames/{0}{1}.gif'.format(f, i))

print('\n\ndone')


