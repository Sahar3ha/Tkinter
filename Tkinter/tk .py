from tkinter import *

root= Tk()

e1=Entry(root)
e1.pack()

def clickaction():
    textoutput=e1.get()
    l1=Label(root,text=textoutput)
    l1.pack()

b1=Button(root, text="CLICK ME", command=clickaction)
b1.pack()

root.mainloop()