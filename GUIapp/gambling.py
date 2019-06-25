from tkinter import *
import tkinter.ttk as ttk
import random
from PIL import Image


root = Tk()
root.title("GUIAPP tkinter")
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


body_frame = ttk.Frame()


game_frame = ttk.Frame(body_frame)
intro_frame = ttk.Frame(body_frame)
top_frame =  ttk.Frame(body_frame)


## top ##

title_label = ttk.Label(top_frame, text="GUIAPP", font=(u'ＭＳ ゴシック', '100')).grid(column=0, row=0)
start_btn = Button(top_frame, text="play start!",font=("",20), bg='#1056ff', command=lambda: intro_frame.tkraise()).grid(column=0, row=1)
top_frame.grid(column=0, row=0, sticky="news")

top_frame.columnconfigure(0, weight=1)
top_frame.rowconfigure(0, weight=1)
top_frame.rowconfigure(1, weight=1)

top_frame.master.columnconfigure(0, weight=1)
top_frame.master.rowconfigure(0, weight=1)
## topend ##


## intro ##

# image #

image_frame = ttk.Frame(intro_frame)
genius_img = PhotoImage(file='genius.png').subsample(2)    
image = ttk.Label(image_frame, image=genius_img).grid(column=0, row=0)


image_frame.grid_propagate(False)
image_frame.grid(column=0, row=1, sticky="news")
image_frame.columnconfigure(0, weight=1)
image_frame.rowconfigure(0, weight=1)

image_frame.master.columnconfigure(0, weight=1)
image_frame.master.rowconfigure(0, weight=1)

# image end #

# message #

message_frame = ttk.Frame(intro_frame)

skip_btn = ttk.Button(message_frame, text='skip', command=lambda: game_frame.tkraise()).grid(column=1, row=0, sticky="news")

text_frame = ttk.Frame(message_frame, relief="sunken")
text_label = ttk.Label(text_frame, text="intro_message").grid(column=0, row = 0)

text_frame.grid(column=0, row=0, sticky="news")
text_frame.columnconfigure(0, weight=1)
text_frame.rowconfigure(0, weight=1)




message_frame.grid(column=0, row=0, sticky="news")
message_frame.columnconfigure(0, weight=2)
message_frame.rowconfigure(0, weight=1)
message_frame.columnconfigure(1, weight=1)
message_frame.rowconfigure(0, weight=1)

message_frame.master.columnconfigure(0, weight=1)
message_frame.master.rowconfigure(0, weight=1)

# text end #


intro_frame.grid(column=0, row=0, sticky="news")

intro_frame.columnconfigure(0, weight=1)
intro_frame.rowconfigure(0, weight=2)
intro_frame.rowconfigure(1, weight=3)


intro_frame.master.columnconfigure(0, weight=1)
intro_frame.master.rowconfigure(0, weight=1)

## intro end ##


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
 |       |      |---imageFrame
 |       |      |---messageFrame
 |       |              |---nextBtn
 |       |              |---skipBtn
 |       |              |---textLabel
 |       |      
 |       |---gameFrame
 |              |---dealerFrame
 |              |---userFrame
 |              |---chooseFrame
 |              |---geniusFrame
 |              |---
 |              |---
 |              |---
 |
 |
 |---footFrame
         |---topBtn
         |---introBtn
         |---gameBtn
 
"""

