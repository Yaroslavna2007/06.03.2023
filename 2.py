from tkinter import *
w = Tk()
w.title('W')
w.geometry('600x600')
lbl = Label(w,text = 'Hi' , font = ('Arial Bold', 40))
lbl.grid(column = 0,row = 0)
txt = Entry(w, width= 20) #текстовая строка
txt.grid(column = 1,row = 0)
txt.focus() # поле сразу активно для ввода

def Click():
    r = txt.get()
    lbl.configure(text = 'Hello ' + r)

btm = Button(w, text = 'play',bg = 'black',fg = 'white',command = Click)
btm.grid(column = 2, row = 0 )

w.mainloop()