from tkinter import *
from tkinter.ttk import Combobox
w = Tk()
w.title('W')
w.geometry('600x600')
e = Combobox(w)
e.grid(column=0,row=0)
e['values'] = ('не выбрано',1,2,3,4,5,6,7)
e.current(0)
w.mainloop()