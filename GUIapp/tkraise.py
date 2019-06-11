from tkinter import *


root = Tk()

def changepage(frame):
    frame.tkraise()


root.title("try tkraise()")
root.geometry("1000x600")

top = Frame(root)
label1 = Label(top, text="this is top")
button1 = Button(top, text="change page", command=lambda : changepage(game)) 
label1.grid()
button1.grid()
top.grid(row=0, column=0)




game = Frame(root)
label2 = Label(game, text="this is game")
button2 = Button(game, text="change page", command=lambda : changepage(top)) 
label2.grid()
button2.grid()
game.grid(row=0, column=0)

top.tkraise()


root.mainloop()
