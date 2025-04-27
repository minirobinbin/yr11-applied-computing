from tkinter import Tk, Label, Button, Entry, END


def add():
    t3.delete(0, 'end')
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1+num2
    t3.insert(END, str(result))


def sub(event):
    t3.delete(0, 'end')
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1-num2
    t3.insert(END, str(result))


window = Tk()
window.title('Hello Python')
window.geometry("400x300+10+10")

lbl1 = Label(window, text='First number')
lbl2 = Label(window, text='Second number')
lbl3 = Label(window, text='Result')
t1 = Entry(width=10)
t2 = Entry(width=10)
t3 = Entry(width=10)
btn1 = Button(window, text='Add')
btn2 = Button(window, text='Subtract')
lbl1.place(x=100, y=50)
t1.place(x=200, y=50)
lbl2.place(x=100, y=100)
t2.place(x=200, y=100)
b1 = Button(window, text='Add', command=add)
b2 = Button(window, text='Subtract')
b2.bind('<Button-1>', sub)
b1.place(x=100, y=150)
b2.place(x=200, y=150)
lbl3.place(x=100, y=200)
t3.place(x=200, y=200)


window.mainloop()
