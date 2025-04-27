import tkinter as tk
from tkinter import font

def saver():
    with open('busdata.csv', 'a') as f:
        f.write(f"{entry1.get()}\n")
        f.close
    saved.config(text="Saved to csv")
    root.after(1200, lambda: saved.config(text=''))


root = tk.Tk()
root.title("Melbourne bus tracker")
root.geometry("400x300+1800+600")


image = tk.PhotoImage(file="tkinter apps/bustracker/bus.png").subsample(24,24)
tk.Label(root, image=image).place(x=250, y=20)

custom_font1 = font.Font(family="X'Trapolis Destination Headboard", size=30, weight="normal")
custom_font2 = font.Font(family="X'Trapolis Destination Headboard", size=20, weight="normal")
bustext = tk.Label(root, text="BUS", font=custom_font1, fg="orange").place(x=40, y=25)
trackertext = tk.Label(root, text="TRACKER", font=custom_font2, fg="orange").place(x=70, y=80)

canvas = tk.Canvas(width=400, height=10)
greenline1 = canvas.create_line(0,5,100,5, fill='green', width=5)
whiteline1 = canvas.create_line(100,0,200,10, fill='white', width=5)
greenline2 = canvas.create_line(200,5,300,5, fill='green', width=5)
whiteline2 = canvas.create_line(300,5,400,5, fill='white', width=5)

canvas.place(x=0, y=200)

entry1label = tk.Label(root, text="Bus number:").place(x=20, y=250)
entry1 = tk.Entry(width=5)
entry1.place(x=100, y=250)

save_button = tk.Button(root, text="Save to CSV", command=saver)
save_button.place(x=200, y=250)

saved = tk.Label(root, text="")
saved.pack()

root.mainloop()