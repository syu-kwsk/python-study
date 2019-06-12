from tkinter import *
import tkinter.ttk as ttk 

root = Tk()
root.title("layout")
root.geometry("1500x800")

rootframe = ttk.Frame()
frame = ttk.Frame(rootframe)

ttk.Button(frame, text='dealer').grid(column=0, row=0, columnspan=2, sticky="news")
ttk.Button(frame, text='exit', command=lambda: root.quit()).grid(column=2, row=0, sticky="news")

# 2列目
ttk.Button(frame, text='hit').grid(column=0, row=1, sticky="news")
ttk.Button(frame, text='stand').grid(column=1, row=1, sticky="news")
ttk.Button(frame, text='cards').grid(column=2, row=1, sticky="news")

# 3列目
ttk.Button(frame, text='user').grid(column=0, row=2, columnspan=2, sticky="news")
ttk.Button(frame, text='genius').grid(column=2, row=2, sticky="news")

# Frame自身もトップレベルウィジェットに配置
frame.grid(column=0, row=0, sticky="news")

# 各列の引き伸ばし設定
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

# 各行の引き伸ばし設定
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

# トップレベルのウィジェットも引き伸ばしに対応させる
frame.master.columnconfigure(0, weight=1)
frame.master.rowconfigure(0, weight=1)

rootframe.grid(column=0, row=0, sticky="news")
rootframe.master.columnconfigure(0, weight=1)
rootframe.master.rowconfigure(0, weight=1)

root.mainloop()
