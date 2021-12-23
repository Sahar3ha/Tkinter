from tkinter import *

root=Tk()

z=Label(root, text="Registration Form",font=23).grid(row=0,column=3)
a=Label(root, text="First name").grid(row=2,column=0)
e1=Entry(root).grid(row=2,column=5)
b=Label(root, text="Last name").grid(row=4,column=0)
e2=Entry(root).grid(row=4,column=5)
c=Label(root, text="Email").grid(row=6,column=0)
e3=Entry(root).grid(row=6,column=5)
d=Label(root, text="Password").grid(row=8,column=0)
e4=Entry(root).grid(row=8,column=5)

e=Button(root, text="Login").grid(row=10,column=3)
f=Button(root, text="Cancel").grid(row=10,column=4)
root.mainloop()