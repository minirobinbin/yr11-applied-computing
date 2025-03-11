import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Temperature converter")
root.geometry("300x70+50+50")

def convert():
    try:
        step1 = int(fentry.get()) - 32
        step2 = step1 *5
        step3 = step2 / 9
        final = round(step3, 2)
        result.config(text=f"{fentry.get()} Fahrenheit = {final} Celsius")
    except:
        result.config(text="No temperture in textbox")

custom_font1 = font.Font(family="MPTG Siemens Train Desto", size=15, weight="normal")
flabel = tk.Label(root, text="Fahrenheit", font=custom_font1, fg="orange")
flabel.place(x=10, y=23)

result = tk.Label(root, text="")
result.place(x=60, y=45)

fentry = tk.Entry(width=10)
fentry.place(x=100, y=20)

convertbutton = tk.Button(root, text="Convert", command=convert)
convertbutton.place(x=200, y=20)

root.mainloop()