import tkinter as tk

def add():
    add = int(entry1.get()) + int(entry2.get())
    entry3.config(text=str(add))

def subtract():
    subtract = int(entry1.get()) - int(entry2.get())
    entry3.config(text=str(subtract))

root = tk.Tk()
root.title("Hello python")
root.geometry("400x300+1800+600")

entry1label = tk.Label(root, text="First number").place(x=100, y=50)
entry1 = tk.Entry(width=10)
entry1.place(x=200, y=50)

entry2label = tk.Label(root, text="Second number").place(x=100, y=100)
entry2 = tk.Entry(width=10)
entry2.place(x=200, y=100)

add_button = tk.Button(root, text="Add", command=add).place(x=100, y=150)
subtract_button = tk.Button(root, text="Subtract", command=subtract).place(x=200, y=150)

entry3label = tk.Label(root, text="Result:").place(x=100, y=200)
entry3 = tk.Label(root, text="")
entry3.place(x=200, y=200)

root.mainloop()