from tkinter import *

root=Tk()
root.geometry("1240x1020")

root.title('Registration form')
z=Label(root, text="Registration form",font=23).pack(side=TOP)

a=Label(root, text="First name",).pack(padx=3,pady=5)
e1=Entry(root).pack(padx=10,pady=5)
b=Label(root, text="Last name",).pack(padx=3,pady=9)
e2=Entry(root).pack(padx=10,pady=9)

c=Label(root, text="Email",).pack(padx=3,pady=16)
e3=Entry(root).pack(padx=3,pady=16)

c=Label(root, text="Password",).pack(padx=3,pady=19)
e4=Entry(root).pack(padx=10,pady=19)

e=Button(root, text="Login").pack(padx=24,pady=25)
f=Button(root, text="Cancel").pack(padx=29,pady=25)


root.mainloop()
