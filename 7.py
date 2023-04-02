from tkinter import *
from tkinter import messagebox

w = Tk()
w.title('W')
w.geometry('600x600')


def Click():
    messagebox.showinfo('w','Hi')


txt = Button(w,text= 'Hi',bg ='black',fg = 'white',command = Click)
txt.grid(column=0,row=0)

w.mainloop()