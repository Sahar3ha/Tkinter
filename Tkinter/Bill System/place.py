from tkinter import *

root = Tk()
root.geometry("600x400")

a=Label(root, text="Bill From:").place(x=30,y=50)
e1=Entry(root).place(x=100,y=50)
b=Label(root, text="Invoice:").place(x=30,y=90)
e2=Entry(root).place(x=100,y=90)
c=Label(root, text="Items:").place(x=30,y=160)
e3=Entry(root).place(x=100,y=160)
d=Label(root, text="Total").place(x=30,y=190)
e4=Entry(root).place(x=100,y=190)

e=Label(root, text="Bill Date:").place(x=250,y=50)
e5=Entry(root).place(x=320,y=50)
f=Label(root, text="Due Date:").place(x=250,y=90)
e4=Entry(root).place(x=320,y=90)
root.mainloop()