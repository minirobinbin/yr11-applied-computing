import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("iOS calculator")
root.geometry("300x500+1800+650")
equation = ""
operation = ""
firstpart = ""
secondpart = ""

def cal(number):
    update = True
    history.config(text="")
    global equation
    global operation
    global firstpart
    global secondpart
    if number == 'c':
        equation = ""
        bigtext.config(text='0')
        update = False
    elif number == '/':
        operation = "divide"
        firstpart = equation
        equation += str(number)
    elif number == 'x':
        operation = "times"
        firstpart = equation
        equation += str(number)
    elif number == '+':
        operation = "add"
        firstpart = equation
        equation += str(number)
    elif number == '-':
        operation = "minus"
        firstpart = equation
        equation += str(number)
    elif number == '=':
        # print(equation)
        try:
            temp = equation.split('/')
            # print("/")
            # print(temp)
            secondpart = temp[1]
        except:
            try:
                temp = equation.split('x')
                # print("x")
                # print(temp)
                secondpart = temp[1]
            except:
                try:
                    temp = equation.split('-')
                    secondpart = temp[1]
                except:
                    temp = equation.split('+')
                    secondpart = temp[1]
        history.config(text=equation)
        try:
            if operation == 'divide':
                equation = int(firstpart) / int(secondpart)
            elif operation == 'times':
                equation = int(firstpart) * int(secondpart)
                # print(equation)
            elif operation == 'minus':
                equation = int(firstpart) - int(secondpart)
            elif operation == 'add':
                equation = int(firstpart) + int(secondpart)
        except:
            equation = "e: no dot"
        bigtext.config(text=equation)
        equation = ""
        update = False
    else:
        equation += str(number)
    # print(equation)
    if update == True:
        bigtext.config(text=equation)
    # return equation

#buttons 
one = tk.Button(root, text='1', command=lambda: cal(1))
two = tk.Button(root, text='2', command=lambda: cal(2))
three = tk.Button(root, text='3', command=lambda: cal(3))
four = tk.Button(root, text='4', command=lambda: cal(4))
five = tk.Button(root, text='5', command=lambda: cal(5))
six = tk.Button(root, text='6', command=lambda: cal(6))
seven = tk.Button(root, text='7', command=lambda: cal(7))
eight = tk.Button(root, text='8', command=lambda: cal(8))
nine = tk.Button(root, text='9', command=lambda: cal(9))
zero = tk.Button(root, text='0', command=lambda: cal(0))

divide = tk.Button(root, text='÷', command=lambda: cal('/'))
times = tk.Button(root, text='X', command=lambda: cal('x'))
minus = tk.Button(root, text='-', command=lambda: cal('-'))
plus = tk.Button(root, text='+', command=lambda: cal('+'))

equal = tk.Button(root, text='=', command=lambda: cal('='))
clear = tk.Button(root, text='AC', command=lambda: cal('c'))
dot = tk.Button(root, text='.', command=lambda: cal('.'))

root.columnconfigure((0,1,2,3),weight=1)

root.rowconfigure((0,1),weight=2)
root.rowconfigure((2,3,4,5,6),weight=1)

one.grid(row=5,column=0, sticky='nsew')
two.grid(row=5,column=1, sticky='nsew')
three.grid(row=5,column=2, sticky='nsew')
four.grid(row=4,column=0, sticky='nsew')
five.grid(row=4,column=1, sticky='nsew')
six.grid(row=4,column=2, sticky='nsew')
seven.grid(row=3,column=0, sticky='nsew')
eight.grid(row=3,column=1, sticky='nsew')
nine.grid(row=3,column=2, sticky='nsew')
zero.grid(row=6,column=0, columnspan=2, sticky='nsew')

dot.grid(row=6,column=2, sticky='nsew')
clear.grid(row=2,column=0, sticky='nsew')
equal.grid(row=6,column=3, sticky='nsew')

divide.grid(row=2,column=3, sticky='nsew')
times.grid(row=3,column=3, sticky='nsew')
minus.grid(row=4,column=3, sticky='nsew')
plus.grid(row=5,column=3, sticky='nsew')

custom_font1 = font.Font(family="Chalkboard", size=30, weight="normal")
custom_font2 = font.Font(family="Chalkboard", size=60, weight="normal")
history = tk.Label(root, text="", anchor='se', font=custom_font1, fg="grey")
bigtext = tk.Label(root, text='0', anchor='se', font=custom_font2,)
bigtext.grid(row=1, column=0, columnspan=4, sticky='nswe')
history.grid(row=0, column=0, columnspan=4, sticky='nswe')

root.mainloop()