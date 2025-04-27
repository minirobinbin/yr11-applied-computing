import tkinter as tk
number = input("1 or 2?")
root = tk.Tk()
root.title("Tk Example")
root.minsize(200,200)
root.maxsize(500,500)
root.geometry("300x300+50+50")
tk.Label(root, text="Northing will work unless you do.").pack()
tk.Label(root,text="- Someone").pack()
frameCnt = 22
frames = [tk.PhotoImage(file=f'{number}.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = tk.Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()