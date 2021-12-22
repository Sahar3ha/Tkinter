from tkinter import *

root=Tk()

z=Label(root, text="Login",font=25).grid(row=0,column=3)
a=Label(root, text="Username").grid(row=2,column=0)
e1=Entry(root).grid(row=2,column=5)
b=Label(root, text="Password").grid(row=4,column=0)
e2=Entry(root).grid(row=4,column=5)

e=Button(root, text="Login").grid(row=10,column=3)
f=Button(root, text="Cancel").grid(row=10,column=4)
root.mainloop()