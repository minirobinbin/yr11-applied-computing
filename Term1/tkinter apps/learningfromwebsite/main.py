import tkinter as tk
from PIL import Image

root  = tk.Tk()
# window1 = tk.Tk()

# window1.title("window 1")
# window1.geometry("300x300+50+50")
root.title("Tk Example")
# root.configure(background="yellow")

root.minsize(200,200)
root.maxsize(500,500)
root.geometry("300x300+50+50")

tk.Label(root, text="Northing will work unless you do.").pack()
tk.Label(root,text="- Someone").pack()

frameCnt = 12
frames = [tk.PhotoImage(file='1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    tk.Label.configure(image=frame)
    root.after(100, update, ind)
tk.Label(root, image=frames).pack()
root.after(0, update, 0)
root.mainloop()
# window1.mainloop()


# when inserting a image, you can only have one window