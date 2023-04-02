from tkinter import *
from tkinter import scrolledtext

w = Tk()
w.title('W')
w.geometry('600x600')

e = scrolledtext.ScrolledText(w,heigh = 12,width = 34)
e.grid(column=1, row=0)
e.insert(INSERT,'HI')
e.delete(1.0,END)
w.mainloop()
