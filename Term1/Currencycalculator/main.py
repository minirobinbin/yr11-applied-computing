from tkinter import *

root = Tk()
root.minsize(600, 500)
root.title("Currency Calculator")
from_label = Label(root, text="FROM CURRENCY")
to_label = Label(root, text="TO CURRENCY")
amount_label = Label(root, text="AMOUNT")
from_box = Entry(root)
to_box = Entry(root)
amount_box = Entry(root)

clear_button = Button(root, text="Clear", command="")
exot_button = Button(root, text="Exit", command="")

# from_label.place(x=0.3,y=60)
# to_label.place(relx=0.3,y=70)
# amount_label.grid(column=0,row=0)

from_label.grid(column=0,row=0)
from_box.grid(column=1,row=0)
to_label.grid(column=2,row=0)
to_box.grid(column=3,row=0)
amount_label.grid(column=4,row=0)
amount_box.grid(column=5,row=0)

root.mainloop()