from tkinter import *
import tkinter.ttk as ttk
import random
from PIL import Image


root = Tk()
root.title("ギャンブルの天才に俺はなる")
root.geometry("1000x800")
root.attributes("-zoomed", "1")




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

body_frame = ttk.Frame()


game_frame = ttk.Frame(body_frame)
intro_frame = ttk.Frame(body_frame)
top_frame =  ttk.Frame(body_frame)


## top ##

title_label = ttk.Label(top_frame, text="ギャンブルの天才", compound="center", font=(u'ＭＳ ゴシック', '50')).grid(column=0, row=0, sticky="news")
start_btn = ttk.Button(top_frame, text="play start!", compound="center", padding=(5,10), command=lambda: intro_frame.tkraise()).grid(column=0, row=1)
top_frame.grid(column=0, row=0, sticky="news")

top_frame.columnconfigure(0, weight=1)
top_frame.rowconfigure(0, weight=1)
top_frame.rowconfigure(1, weight=1)

top_frame.master.columnconfigure(0, weight=1)
top_frame.master.rowconfigure(0, weight=1)
## topend ##



## intro ##

ttk.Label(intro_frame, text="this is intro").grid(column=0, row=0, sticky="news")

intro_frame.grid(column=0, row=0, sticky="news")

intro_frame.columnconfigure(0, weight=1)
intro_frame.rowconfigure(0, weight=1)

intro_frame.master.columnconfigure(0, weight=1)
intro_frame.master.rowconfigure(0, weight=1)

## intro ##



## game ##

ttk.Label(game_frame, text="this is game").grid(column=0, row=0, sticky="news")

game_frame.grid(column=0, row=0, sticky="news")

game_frame.columnconfigure(0, weight=1)
game_frame.rowconfigure(0, weight=1)

game_frame.master.columnconfigure(0, weight=1)
game_frame.master.rowconfigure(0, weight=1)

## game end ##


body_frame.grid(column=0, row=1, sticky="news")
body_frame.master.columnconfigure(0, weight=1)
body_frame.master.rowconfigure(1, weight=500)

### bodyend ###







### foot ###

foot_frame = ttk.Frame()
ttk.Button(foot_frame, text='top_frame', command=lambda: top_frame.tkraise()).grid(column=0, row=0, sticky="news")
ttk.Button(foot_frame, text='intro_frame', command=lambda: intro_frame.tkraise()).grid(column=1, row=0, sticky="news")
ttk.Button(foot_frame, text='game_frame', command=lambda: game_frame.tkraise()).grid(column=2, row=0, sticky="news")
foot_frame.columnconfigure(0, weight=1)
foot_frame.columnconfigure(1, weight=1)
foot_frame.columnconfigure(2, weight=1)
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

