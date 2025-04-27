import tkinter as tk

def add():
    result = int(firstnumberentry.get())+int(secondnumberentry.get())
    resultentry.config(text=str(result))

def subtract():
    result = int(firstnumberentry.get())-int(secondnumberentry.get())
    resultentry.config(text=str(result))

root = tk.Tk()
root.title('Hello Python')
root.geometry("400x300+1800+600")

firstnumberlabel = tk.Label(root, text='First number')
firstnumberlabel.place(x=100, y=50)
firstnumberentry = tk.Entry(width=10)
firstnumberentry.place(x=200, y=50)

secondnumberlabel = tk.Label(root, text='Second number')
secondnumberlabel.place(x=100, y=100)
secondnumberentry = tk.Entry(width=10)
secondnumberentry.place(x=200, y=100)

resultlabel = tk.Label(root, text='Result:')
resultlabel.place(x=100, y=200)
resultentry = tk.Label(root, text='~')
resultentry.place(x=200, y=200)

addbutton = tk.Button(root, text='Add', command=add)
addbutton.place(x=100, y=150)
subtractbutton = tk.Button(root, text='Subtract', command=subtract)
subtractbutton.place(x=200, y=150)

root.mainloop()
