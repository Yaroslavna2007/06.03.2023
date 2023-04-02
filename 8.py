from tkinter import *

w = Tk()
w.title('W')
w.geometry('600x600')

e = Spinbox(w, from_= 1,to = 100 )
e.grid(column=1,row=1)

w.mainloop()