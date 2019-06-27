from tkinter import *
import tkinter.ttk as ttk
import random
from PIL import Image


root = Tk()
root.title("GUIAPP tkinter")
root.geometry("1000x800")
root.attributes("-zoomed", "1")

tramp_img = [PhotoImage(file='asset/s1.png').subsample(4)
             ,PhotoImage(file='asset/s2.png').subsample(4)
             ,PhotoImage(file='asset/s3.png').subsample(4)
             ,PhotoImage(file='asset/s4.png').subsample(4)
             ,PhotoImage(file='asset/s5.png').subsample(4)
             ,PhotoImage(file='asset/s6.png').subsample(4)             
]

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
genius_img = PhotoImage(file='asset/genius.png').subsample(2)    
image = ttk.Label(image_frame, image=genius_img).grid(column=0, row=0)


image_frame.grid_propagate(False)
image_frame.grid(column=0, row=1, sticky="news")
image_frame.columnconfigure(0, weight=1)
image_frame.rowconfigure(0, weight=1)

image_frame.master.columnconfigure(0, weight=1)
image_frame.master.rowconfigure(0, weight=1)

# image end #

# message #

texts = ["なにしにきたんや？"
         ,"まさか、ギャンブルの\n天才と思とるんか？"
         ,"やめとけ。お前は天才ちゃう"
         ,"試してみるか？"
         ,"じゃあ、ブラックジャックな"
         ,"どーせ、負けるやろし"
         ,"しゃーないから、\n俺が時々アドバイスしたるわ"
         ,"ほないくで"
]
message = StringVar()
# message.set(texts[0])

def change_message(target):
    next_message = 0
    for i in range( len(texts) ):
        if texts[i] == target.get():
            next_message = i+1
            
    if next_message >= len(texts):
        game_frame.tkraise()
    else:
        message.set(texts[next_message])   
        

message_frame = ttk.Frame(intro_frame)


text_frame = ttk.Frame(message_frame, relief="sunken")
text_label = ttk.Label(text_frame, textvariable = message, font=(u'ＭＳ ゴシック', '50')).grid(column=0, row = 0)
btn_frame = ttk.Frame(message_frame, relief="raised")
skip_btn = Button(btn_frame, text='skip',font=("",20), bg='#1056ff', command=lambda: game_frame.tkraise()).grid(column=0, row=0)
next_btn = Button(btn_frame, text='next',font=("",20), bg='#1056ff', command=lambda:change_message(message)).grid(column=0, row=1)

btn_frame.grid_propagate(False)
text_frame.grid_propagate(False)

btn_frame.grid(column=1, row=0, sticky="news")
btn_frame.columnconfigure(0, weight=1)
btn_frame.rowconfigure(0, weight=1)
btn_frame.rowconfigure(1, weight=1)

text_frame.grid(column=0, row=0, sticky="news")
text_frame.columnconfigure(0, weight=1)
text_frame.rowconfigure(0, weight=1)




message_frame.grid(column=0, row=0, sticky="news")
message_frame.columnconfigure(0, weight=5)
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


# comment #
commentgame_frame = ttk.Frame(game_frame, width=1000, height=600, borderwidth=5, relief="raised")

ttk.Button(commentgame_frame, text="close", command=lambda: normalgame_frame.tkraise()).grid(column=0, row=1)

comment_frame = ttk.Frame(commentgame_frame, width=800, height=400)
ttk.Label(comment_frame, text = "それはセンスないわ〜\n俺の言うとおりで勝てる", font=(u'ＭＳ ゴシック', '30')).grid(column=0, row=0)

comment_frame.grid_propagate(False)
comment_frame.grid(column=0, row=0)
comment_frame.columnconfigure(0, weight=1)
comment_frame.rowconfigure(0, weight=1)



commentgame_frame.grid_propagate(False)
commentgame_frame.grid(column=0, row=0)
commentgame_frame.columnconfigure(0, weight=2)
commentgame_frame.rowconfigure(0, weight=5)
commentgame_frame.rowconfigure(1, weight=1)


commentgame_frame.master.columnconfigure(0, weight=1)
commentgame_frame.master.rowconfigure(0, weight=1)

# comment #


# normal  #

normalgame_frame = ttk.Frame(game_frame)

# dealer
dealer_frame= ttk.Frame(normalgame_frame, relief="sunken")

ttk.Label(dealer_frame, text='dealer').grid(column=0, row=0)

dealer_frame.grid_propagate(False)
dealer_frame.grid(column=0, row=0, sticky="news")
dealer_frame.columnconfigure(0, weight=1)
dealer_frame.rowconfigure(0, weight=1)

# user

def gen_tramp(i):
    
    ttk.Label(user_frame, image=tramp_img[i]).grid(column=i, row=0)
    
user_frame= ttk.Frame(normalgame_frame, relief="sunken")


user_frame.grid_propagate(False)
user_frame.grid(column=0, row=2, sticky="news")
user_frame.columnconfigure(0, weight=1)
user_frame.rowconfigure(0, weight=1)


#choose
choose_frame = ttk.Frame(normalgame_frame, relief="sunken")

hit_btn = Button(choose_frame, text=" hit ",font=("",100), bg='#ff0000', fg="#ffffff", width=5).grid(column=0, row=0)
stand_btn = Button(choose_frame, text="stand",font=("",100), bg='#0000ff', fg="#ffffff", width=5).grid(column=1, row=0)

choose_frame.grid_propagate(False)
choose_frame.grid(column=0, row=1, sticky="news")
choose_frame.columnconfigure(0, weight=1)
choose_frame.columnconfigure(1, weight=1)
choose_frame.rowconfigure(0, weight=1)


#money
money_frame = ttk.Frame(normalgame_frame, relief="sunken")

ttk.Label(money_frame, text='money').grid(column=0, row=0)

money_frame.grid_propagate(False)
money_frame.grid(column=1, row=0, sticky="news")
money_frame.columnconfigure(0, weight=1)
money_frame.rowconfigure(0, weight=1)

# stock
stock_frame= ttk.Frame(normalgame_frame, relief="sunken")

ttk.Label(stock_frame, text='stock').grid(column=0, row=0)

stock_frame.grid_propagate(False)
stock_frame.grid(column=1, row=1, sticky="news")
stock_frame.columnconfigure(0, weight=1)
stock_frame.rowconfigure(0, weight=1)

# genius
genius_frame= ttk.Frame(normalgame_frame, relief="sunken")

ttk.Button(genius_frame, text='genius', command=lambda: commentgame_frame.tkraise()).grid(column=0, row=0)

genius_frame.grid_propagate(False)
genius_frame.grid(column=1, row=2, sticky="news")
genius_frame.columnconfigure(0, weight=1)
genius_frame.rowconfigure(0, weight=1)


normalgame_frame.grid(column=0, row=0, sticky="news")
normalgame_frame.columnconfigure(0, weight=2)
normalgame_frame.columnconfigure(1, weight=1)
normalgame_frame.rowconfigure(0, weight=1)
normalgame_frame.rowconfigure(1, weight=1)
normalgame_frame.rowconfigure(2, weight=1)


normalgame_frame.master.columnconfigure(0, weight=1)
normalgame_frame.master.rowconfigure(0, weight=1)


# normalgame end #




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
 |       |              |---buttonFrame
 |       |              |       |---skipBtn
 |       |              |       |---nextBtn
 |       |              |
 |       |              |---texrFrame
 |       |                      |---textLabel
 |       |
 |       |      
 |       |---gameFrame
 |              |---commentgameFrame
 |              |        |---commentFrame
 |              |        |       |---commentLabel
 |              |        |
 |              |        |---closeBtn
 |              |
 |              |
 |              |---normalgameFrame
 |                       |---dealerFrame
 |                       |---userFrame
 |                       |---chooseFrame
 |                       |---geniusFrame
 |                       |---moneyFrame
 |                       |---stockFrame
 |
 |
 |
 |---footFrame
         |---topBtn
         |---introBtn
         |---gameBtn
 
"""

