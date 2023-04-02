from tkinter.ttk import Progressbar
from tkinter import *

w = Tk()
w.title('W')
w.geometry('600x600')

e = Progressbar(w,length=154)
e.grid(column=1,row=1)
e['value'] = 50

w.mainloop()