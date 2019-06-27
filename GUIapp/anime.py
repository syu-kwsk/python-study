# codeing=utf-8
import tkinter as tk
 
#円の座標
x = 300
y = 200
 
def move():
    global x,y
    #前の円を隠す
    canvas.create_oval(x-30, y-30, x+30, y+30, fill="white", width=0)
    #右に動かす
    x = x+1
    #新しい円を描く
    canvas.create_oval(x-20, y-20, x+20, y+20, fill="red", width=0)
    #タイマーを作る
    root.after(10,move)
 
#ウィンドウを作る
root = tk.Tk()
root.geometry("600x400")
  
#Canvasを作る
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.place(x=0, y=0)
 
#タイマーを作る
root.after(10,move)
 
 
root.mainloop()
