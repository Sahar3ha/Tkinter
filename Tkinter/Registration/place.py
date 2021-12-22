from tkinter import *

root = Tk()
root.geometry("600x400")

a=Label(root, text="First name").place(x=30,y=50)
e1=Entry(root).place(x=100,y=50)
b=Label(root, text="Last name").place(x=30,y=90)
e2=Entry(root).place(x=100,y=90)
c=Label(root, text="Email").place(x=30,y=160)
e3=Entry(root).place(x=100,y=160)
d=Label(root, text="Password").place(x=30,y=190)
e4=Entry(root).place(x=100,y=190)

e=Button(root, text="Login").place(x=240,y=250)
f=Button(root, text="Cancel").place(x=290,y=250)
root.mainloop()