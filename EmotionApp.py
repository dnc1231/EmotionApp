from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import os
import time
from espeak import espeak
import tkinter as tk

global file
file='/home/pi/Pictures/frames/gif_'

def update(ind, frames):
    if (ind < len(frames)):
        frame = frames[ind]
        ind += 1
        label.configure(image=frame)
        root.after(5, update, ind, frames)
    else:
        root.mainloop()
        return;

##h
def joyEmotion():
    root.update()
    global nextEmotion
    nextEmotion = 'h'
    global currentEmotion
    if (currentEmotion == nextEmotion):
        return;
    else:
##        print sound
##        if (sound):
##            espeak.synth("hello")
        frames = [PhotoImage(file='/home/pi/Pictures/frames/gif_{}2{}{}.gif'.format(currentEmotion, nextEmotion, i)) for i in range(34)]
        currentEmotion = nextEmotion
        root.after(0, update, 0, frames)

##s
def sadnessEmotion():
    root.update()
    global nextEmotion
    nextEmotion = 's'
    global currentEmotion
    if (currentEmotion == nextEmotion):
        return;
    else:
        frames = [PhotoImage(file='/home/pi/Pictures/frames/gif_{}2{}{}.gif'.format(currentEmotion, nextEmotion, i)) for i in range(34)]
        currentEmotion = nextEmotion
        root.after(0, update, 0, frames)

##f
def fearEmotion():
    root.update()
    global nextEmotion
    nextEmotion = 'f'
    global currentEmotion
    if (currentEmotion == nextEmotion):
        return;
    else:
        frames = [PhotoImage(file='/home/pi/Pictures/frames/gif_{}2{}{}.gif'.format(currentEmotion, nextEmotion, i)) for i in range(34)]
        currentEmotion = nextEmotion
        root.after(0, update, 0, frames)

##c
def surpriseEmotion():
    root.update()
    global nextEmotion
    nextEmotion = 'c'
    global currentEmotion
    if (currentEmotion == nextEmotion):
        return;
    else:
        frames = [PhotoImage(file='/home/pi/Pictures/frames/gif_{}2{}{}.gif'.format(currentEmotion, nextEmotion, i)) for i in range(34)]
        currentEmotion = nextEmotion
        root.after(0, update, 0, frames)

##n
def neutralEmotion():
    root.update()
    global nextEmotion
    nextEmotion = 'n'
    global currentEmotion
    if (currentEmotion == nextEmotion):
        return;
    else:
        frames = [PhotoImage(file='/home/pi/Pictures/frames/gif_{}2{}{}.gif'.format(currentEmotion, nextEmotion, i)) for i in range(34)]
        currentEmotion = nextEmotion
        root.after(0, update, 0, frames)


##d
def disgustEmotion():
    root.update()
    global nextEmotion
    nextEmotion = 'd'
    global currentEmotion
    if (currentEmotion == nextEmotion):
        return;
    else:
        frames = [PhotoImage(file='/home/pi/Pictures/frames/gif_{}2{}{}.gif'.format(currentEmotion, nextEmotion, i)) for i in range(34)]
        currentEmotion = nextEmotion
        root.after(0, update, 0, frames)

##a
def angerEmotion():
    root.update()
    global nextEmotion
    nextEmotion = 'a'
    global currentEmotion
    if (currentEmotion == nextEmotion):
        return;
    else:
        frames = [PhotoImage(file='/home/pi/Pictures/frames/gif_{}2{}{}.gif'.format(currentEmotion, nextEmotion, i)) for i in range(34)]
        currentEmotion = nextEmotion
        root.after(0, update, 0, frames)

def helpCommand():
    filewin = Toplevel(root)
    filewin.maxsize(320,60)
    text = Text(filewin)
    text.insert(INSERT, "Select an emotion from the Emotions Menu to display the corresponding facial animation.\n\nSelect the 'X' to exit the program.")
    text.pack()

root = Tk()
root.title("ADAM Therapeutic Robot")

##sound = tk.BooleanVar()
##sound.set(True)

menubar = Menu(root)
emotionMenu = Menu(menubar, tearoff=0)
emotionMenu.add_command(label="Joy", command=joyEmotion)
emotionMenu.add_command(label="Sadness", command=sadnessEmotion)
emotionMenu.add_command(label="Fear", command=fearEmotion)
emotionMenu.add_command(label="Surprise", command=surpriseEmotion)
emotionMenu.add_command(label="Disgust", command=disgustEmotion)
emotionMenu.add_command(label="Anger", command=angerEmotion)
emotionMenu.add_command(label="Resting Face", command=neutralEmotion)

emotionMenu.add_separator()
##emotionMenu.add_checkbutton(label="Sound", onvalue=True, offvalue=False, variable=sound)
emotionMenu.add_command(label="Help", command=helpCommand)
menubar.add_cascade(label="Emotions", menu=emotionMenu)
root.config(menu=menubar)

global currentEmotion
currentEmotion = 'n'
global nextEmotion
nextEmotion = 'n'

h2n = [PhotoImage(file='/home/pi/Pictures/frames/gif_h2n{0}.gif'.format(i)) for i in range(34)]

label = Label(root)
label.pack()
root.after(0, update, 0, h2n)

root.mainloop()





