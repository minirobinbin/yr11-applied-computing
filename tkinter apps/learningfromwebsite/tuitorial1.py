import tkinter as tk

root  = tk.Tk()
# window1 = tk.Tk()

# window1.title("window 1")
# window1.geometry("300x300+50+50")

root.title("Tk Example")
root.configure(background="yellow")
root.minsize(200,200)
root.maxsize(500,500)
root.geometry("300x300+50+50")

tk.Label(root, text="Northing will work unless you do.").pack()
tk.Label(root,text="- Someone").pack()

# image = tk.PhotoImage(file="Image copy.gif")
# tk.Label(window1, image=image).pack()

root.mainloop()
# window1.mainloop()