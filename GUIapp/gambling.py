from tkinter import *
import tkinter.ttk as ttk
import random
from PIL import Image

def setButton(from_frame, to_frame ,name):
    ttk.Button(from_frame, text='exit', command=lambda: root.quit()).grid(column=1, row=0, sticky="news")
    ttk.Button(from_frame, text=name, command=lambda: to_frame.tkraise()).grid(column=0, row=0, sticky="news")

root = Tk()
root.title("ギャンブルの天才に俺はなる")
root.geometry("2000x800")
# root.attributes("-zoomed", "1")

root_frame = ttk.Frame()
top_frame =  ttk.Frame(root_frame)
intro_frame = ttk.Frame(root_frame)
game_frame = ttk.Frame(root_frame)

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

root_frame.grid(column=0, row=0, sticky="news")
root_frame.master.columnconfigure(0, weight=1)
root_frame.master.rowconfigure(0, weight=1)

root.mainloop();


"""
#genius_img = PhotoImage(file='genius.png').subsample(4)    

def move():
    top_frame.destroy()
    gen_game_frame()

def show_message(message, frame, x=1, y=0):
    message = Label(frame, text=message).grid(row=x, column=y)
    
""""""
def gen_top_frame():
    
    exit_button = Button(top_frame, text="exit", width=10, height=3 ,command=root.quit)
    start_button = Button(top_frame, text="start", width=50, height=10, command=move)
    
    top_frame.pack()
    exit_button.pack()
    start_button.pack()

def gen_game_frame():
    exit_button = Button(game_frame, text="exit_intro", width=10, height=3 ,command=root.quit)
    genius = Label(game_frame, image=genius_img)
    text = "おる"
    show_message(text, game_frame, 2)
    
    game_frame.grid()
    exit_button.grid(row=1)
    genius.grid(row=2, column=2)


    
gen_top_frame();
"""

