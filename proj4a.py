import tkinter
from tkinter import *
from functools import partial

win = Tk()

def add(label,x1,x2):
    n1 = x1.get()
    n2 = x2.get()
    z = float(n1) + float(n2)
    l4.config(text="The result is: %s" %z)
    return
def sub(label,x1,x2):
    n1 = x1.get()
    n2 = x2.get()
    z = float(n1) - float(n2)
    l4.config(text="The result is: %s" %z)
    return
def mul(label,x1,x2):
    n1 = x1.get()
    n2 = x2.get()
    z = float(n1) * float(n2)
    l4.config(text="The result is: %s" %z)
    return
def div(label,x1,x2):
    n1 = x1.get()
    n2 = x2.get()
    z = float(n1) / float(n2)
    l4.config(text="The result is: %s" %z)
    return



win.geometry("400x200")

l1 = Label(win, text="Basic Calculator")
l1.place(x=120,y=10)
l2 = Label(win, text=" Enter first number:")
l2.place(x=10,y=40)
l3 = Label(win, text="Enter second number:")
l3.place(x=10,y=80)
l4 = Label(win)
l4.place(x=50,y=160)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win,textvariable=x1)
e1.place(x=140,y=40)
e2 = Entry(win,textvariable=x2)
e2.place(x=140,y=80)

add = partial(add,l4,x1,x2)
sub = partial(sub,l4,x1,x2)
mul = partial(mul,l4,x1,x2)
div = partial(div,l4,x1,x2)

b1 = Button(win, text="  Add  ", command=add,activeforeground='red',bg='grey',activebackground="blue")
b1.place(x=20,y=120)
b1 = Button(win, text="Subtract", command=sub,activeforeground='red',bg='grey',activebackground="blue")
b1.place(x=100,y=120)
b1 = Button(win, text="Multiply", command=mul,activeforeground='red',bg='grey',activebackground="blue")
b1.place(x=180,y=120)
b1 = Button(win, text=" Divide ", command=div,activeforeground='red',bg='grey',activebackground="blue")
b1.place(x=260,y=120)

win.mainloop()
