from tkinter import *
import random



root = Tk()
root.title("ギャンブルの天才に俺はなる")
root.attributes("-zoomed", "1")

def move():
    start = Label(text="start pushed")
    start.pack()

exit_button = Button(text="exit", width=10, height=3 ,command=root.quit)

exit_button.pack()

start_button = Button(text="start", width=50, height=10, command=move)

start_button.pack()


root.mainloop();
