import tkinter as tk

#setup
root = tk.Tk()
root.geometry("500x250")
root.title("Player Registry")

#setting up image
logo = tk.PhotoImage(file="cricket-logo.gif")
tk.Label(root, image=logo, height=200, width=200).grid(row=0, column=2, rowspan=3, sticky="news")

#label set up
Name_label = tk.Label(root, text="Player Name:").grid(row=0, column=0)
Team_label = tk.Label(root, text="Team:").grid(row=1, column=0)
Age_label = tk.Label(root, text="Age Group:").grid(row=2, column=0)

#entry setting up
Name_entry = tk.Entry(root, text="")
Name_entry.grid(row=0, column=1)
Team_entry = tk.Entry(root, text="")
Team_entry.grid(row=1, column=1)
Age_entry = tk.Entry(root, text="")
Age_entry.grid(row=2, column=1)

#setting up submit button
submit_button = tk.Button(root, text="Submit", command=lambda: print(f"Player Name: {Name_entry.get()}\nTeam: {Team_entry.get()}\nAge Group: {Age_entry.get()}"))
submit_button.grid(row=3, column=0, columnspan=3)

#make the window stay by looping the code
root.mainloop()