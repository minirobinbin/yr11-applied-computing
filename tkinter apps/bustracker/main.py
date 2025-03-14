import tkinter as tk

def saver():
    with open('busdata.csv', 'a') as f:
        f.write(entry1.get())
        f.close
    

root = tk.Tk()
root.title("Melbourne bus tracker")
root.geometry("400x300+1800+600")

entry1label = tk.Label(root, text="Bus number").place(x=100, y=50)
entry1 = tk.Entry(root)
entry1.place(x=200, y=50)

save_button = tk.Button(root, text="Save to CSV", command=saver)
save_button.pack()


root.mainloop()