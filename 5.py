from tkinter import *
from tkinter.ttk import Radiobutton

w = Tk()
w.title('W')
w.geometry('600x600')

yara = IntVar()
radio1 = Radiobutton(w,text = 'один', value=1, variable = yara)
radio1.grid(column=0,row=0)

radio2 = Radiobutton(w,text = 'два', value=2, variable = yara)
radio2.grid(column=1,row=0)

radio3 = Radiobutton(w,text = 'три',value=3, variable = yara)
radio3.grid(column=2,row=0)

def Click():
    print(yara.get())

    r = yara.get()
    r = str(r)

    lbl = Label(w, text = yara.get(), font=('Arial Bold', 40))
    lbl.grid(column=3, row=0)

    lbl.configure(text = 'Hello ' + r)

btm = Button(w, text = 'play',bg = 'black',fg = 'white', command = Click)
btm.grid(column = 0, row = 1 )


w.mainloop()