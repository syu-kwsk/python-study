from tkinter import *
import random
from PIL import Image



root = Tk()
root.title("ギャンブルの天才に俺はなる")
root.geometry("1000x800")
# root.attributes("-zoomed", "1")


top_page = Frame(root)
game_page = Frame(root)
genius_img = PhotoImage(file='genius.png').subsample(4)

   
def move():
    top_page.destroy()
    gen_game_page()

def show_message(message, frame, x=1, y=0):
    message = Label(frame, text=message).grid(row=x, column=y)
    
"""toppageのフレーム"""
def gen_top_page():
    
    exit_button = Button(top_page, text="exit", width=10, height=3 ,command=root.quit)
    start_button = Button(top_page, text="start", width=50, height=10, command=move)
    
    top_page.pack()
    exit_button.pack()
    start_button.pack()

def gen_game_page():
    exit_button = Button(game_page, text="exit_intro", width=10, height=3 ,command=root.quit)
    genius = Label(game_page, image=genius_img)
    text = "お前が天才かどうか調べてやる"
    show_message(text, game_page, 2)
    
    game_page.grid()
    exit_button.grid(row=1)
    genius.grid(row=2, column=2)


    
gen_top_page();


root.mainloop();
