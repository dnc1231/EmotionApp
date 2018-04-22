from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import os
import time

def update(ind, frames):
    if (ind < len(frames)):
        frame = frames[ind]
        ind += 1
        label.configure(image=frame)
        root.after(5, update, ind, frames)
    else:
        root.mainloop()
        return;

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

##h
def joyEmotion():
    root.update()
    global nextEmotion
    nextEmotion = 'h'
    global currentEmotion
    if (currentEmotion == nextEmotion):
        return;
    else:
        if (currentEmotion == 's'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/frames/gif_s2h{0}.gif'.format(i)) for i in range(34)]
            #frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_s2h.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'n'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_n2h.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'c'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_c2h.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'f'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_f2h.gif',format = 'gif -index %i' %(i)) for i in range(34)]
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
        if (currentEmotion == 'h'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_h2s.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'n'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_n2s.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'c'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_c2s.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'f'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_f2s.gif',format = 'gif -index %i' %(i)) for i in range(34)]
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
        if (currentEmotion == 's'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_s2f.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'n'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_n2f.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'c'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_c2f.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'h'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_h2f.gif',format = 'gif -index %i' %(i)) for i in range(34)]
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
        if (currentEmotion == 's'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_s2c.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'n'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_n2c.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'h'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_h2c.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'f'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_f2c.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        currentEmotion = nextEmotion
        root.after(0, update, 0, frames)

def neutralEmotion():
    root.update()
    global nextEmotion
    nextEmotion = 'n'
    global currentEmotion
    if (currentEmotion == nextEmotion):
        return;
    else:
        if (currentEmotion == 's'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_s2n.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'c'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_c2n.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'h'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_h2n.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        elif (currentEmotion == 'f'):
            frames = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_f2n.gif',format = 'gif -index %i' %(i)) for i in range(34)]
        currentEmotion = nextEmotion
        root.after(0, update, 0, frames)


##d
def disgustEmotion():
    return;

##a
def angerEmotion():
    return;

##e
def anticipationEmotion():
    return;

def helpCommand():
    filewin = Toplevel(root)
    filewin.maxsize(320,60)
    text = Text(filewin)
    text.insert(INSERT, "Select an emotion from the Emotions Menu to display the corresponding facial animation.\n\nSelect the 'X' to exit the program.")
    text.pack()

root = Tk()
root.title("ADAM Therapeutic Robot")
menubar = Menu(root)
emotionMenu = Menu(menubar, tearoff=0)
emotionMenu.add_command(label="Joy", command=joyEmotion)
emotionMenu.add_command(label="Sadness", command=sadnessEmotion)
emotionMenu.add_command(label="Fear", command=fearEmotion)
emotionMenu.add_command(label="Surprise", command=surpriseEmotion)
emotionMenu.add_command(label="Disgust", command=donothing)
emotionMenu.add_command(label="Anger", command=donothing)
emotionMenu.add_command(label="Anticipation", command=donothing)
emotionMenu.add_command(label="Resting Face", command=neutralEmotion)

emotionMenu.add_separator()
emotionMenu.add_command(label="Help", command=helpCommand)
menubar.add_cascade(label="Emotions", menu=emotionMenu)
root.config(menu=menubar)

global currentEmotion
currentEmotion = 'n'
global nextEmotion
nextEmotion = 'n'

h2n = [PhotoImage(file='/home/pi/Pictures/Emotion Gifs/1 sec gifs/gif_h2n.gif',format = 'gif -index %i' %(i)) for i in range(34)]

label = Label(root)
label.pack()
root.after(0, update, 0, h2n)

root.mainloop()





