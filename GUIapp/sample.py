import tkinter.messagebox as mb

ans = mb.askyesno("質問", "ラーメン好き？")
if ans == True:
    mb.showinfo("同意","おれも好き")
else:
    mb.showinfo("ま？？？","ラーメン嫌いなん")
 
