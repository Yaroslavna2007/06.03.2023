from tkinter import *

window = Tk()
window.title('Yara')

lbl = Label(window,text = 'Hi', font = ('Arial Bold', 40))
lbl.grid(column = 1, row = 0 )
window.geometry('200x200')

btm = Button(window, text = 'play',bg = 'black',fg = 'white')
btm.grid(column = 0, row = 0 )

window.mainloop()
