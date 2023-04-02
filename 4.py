from tkinter import *
from tkinter.ttk import Checkbutton
w = Tk()
w.title('W')
w.geometry('600x600')

chk_state = BooleanVar()
chk_state.set(False)
e = Checkbutton(w,text = 'выбрать', var = chk_state)
e.grid(column=0,row=0)

w.mainloop()
