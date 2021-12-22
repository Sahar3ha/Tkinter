from tkinter import *

root = Tk()
root.geometry("400x400")
z=Label(root, text="Login",font=23).pack(side=TOP)

a=Label(root, text="Username").pack(padx=3,pady=5)
e1=Entry(root).pack(padx=10,pady=5)
b=Label(root, text="Password").pack(padx=2,pady=6)
e2=Entry(root).pack(padx=10,pady=9)
c=Button(root, text="Login").pack(padx=15,pady=12)
d=Button(root, text="Cancel").pack(padx=15,pady=12)

root.mainloop()