from tkinter import *
import tkinter.ttk as ttk
import random
from PIL import Image


root = Tk()
root.title("ギャンブルの天才に俺はなる")
root.geometry("1000x800")
#root.attributes("-zoomed", "1")


### head ###

head_frame = ttk.Frame()
ttk.Button(head_frame, text='exit', command=lambda: root.quit()).grid(column=0, row=0, sticky="news")
head_frame.columnconfigure(0, weight=1)
head_frame.rowconfigure(0, weight=1)


head_frame.grid(column=0, row=0, sticky="news")
head_frame.master.columnconfigure(0, weight=1)
head_frame.master.rowconfigure(0, weight=2)

### headend ###



### body ###

#genius_img = PhotoImage(file='genius.png').subsample(4)    

def setButton(from_frame, to_frame ,name):
    ttk.Button(from_frame, text=name, command=lambda: to_frame.tkraise()).grid(column=0, row=0, sticky="news")


body_frame = ttk.Frame()

top_frame =  ttk.Frame(body_frame)
intro_frame = ttk.Frame(body_frame)
game_frame = ttk.Frame(body_frame)

setButton(top_frame, intro_frame, "to intro")
setButton(intro_frame, game_frame, "to game")
setButton(game_frame, top_frame, "to top")


game_frame.grid(column=0, row=0, sticky="news")
intro_frame.grid(column=0, row=0, sticky="news")
top_frame.grid(column=0, row=0, sticky="news")

top_frame.columnconfigure(0, weight=1)
top_frame.columnconfigure(1, weight=1)
top_frame.rowconfigure(0, weight=1)
intro_frame.columnconfigure(0, weight=1)
intro_frame.columnconfigure(1, weight=1)
intro_frame.rowconfigure(0, weight=1)
game_frame.columnconfigure(0, weight=1)
game_frame.columnconfigure(1, weight=1)
game_frame.rowconfigure(0, weight=1)

top_frame.master.columnconfigure(0, weight=1)
top_frame.master.rowconfigure(0, weight=1)
intro_frame.master.columnconfigure(0, weight=1)
intro_frame.master.rowconfigure(0, weight=1)
game_frame.master.columnconfigure(0, weight=1)
game_frame.master.rowconfigure(0, weight=1)




body_frame.grid(column=0, row=1, sticky="news")
body_frame.master.columnconfigure(0, weight=1)
body_frame.master.rowconfigure(1, weight=500)

### bodyend ###

### foot ###

foot_frame = ttk.Frame()
ttk.Button(foot_frame, text='presents by syu-kwsk').grid(column=0, row=0, sticky="news")
foot_frame.columnconfigure(0, weight=1)
foot_frame.rowconfigure(0, weight=1)


foot_frame.grid(column=0, row=2, sticky="news")
foot_frame.master.columnconfigure(0, weight=1)
foot_frame.master.rowconfigure(0, weight=1)

###footend###


root.mainloop();


"""
MODEL

root 
 |---headFrame---exitBtn
 | 
 |---bodyFrame
 |       |---topFrame
 |       |      |---startBtn
 |       |
 |       |---introFrame
 |       |---gameFrame
 |
 |
 |---footFrame---byBtn
 
"""

