import tkinter as tk
import csv

def save_to_csv():
    if good_password() and entry2.get == entry3.get:
        # get the data from the entries and store it as a list called data
        data = [entry1.get(), entry2.get(), entry3.get()]
        # open a csv file called data.csv in the append mode, create a writer, and write data as a row
        with open('data.csv', 'a', newline ='') as file:
            writer = csv.writer(file)
            writer.writerow(data) 
        # config the status label to read "Data saved to data.csv"
        status_label.config(text="Data saved to data.csv")
        # after 3000 cycles config the status label to ""
        root.after(3000, lambda: status_label.config(text=''))

        #def reset_status_label:
            #status_label.config(text='')
    else:
        status_label.config(text="Re-eneter your password")
        root.after(3000, lambda: status_label.config(text=''))

def good_password():
    password = entry2.get()
    if password == "Password" or password == "":
        # if the user has not inputted anything
        status_label.config(text="Please enter your password")
        root.after(3000, lambda: status_label.config(text=''))
        return False
    elif password != entry3.get():
        status_label.config(text="Passwords do not match")
        root.after(3000, lambda: status_label.config(text=''))
    elif len(password) < 8:
        # password length
        status_label.config(text="Password must be at least 8 characters")
        root.after(3000, lambda: status_label.config(text=''))
        return False
    else:
        # contains all values
        upper = False
        lower = False
        number = False
        special = False
        for letter in password:
            if letter.isupper():
                upper = True
            if letter.islower():
                lower = True
            if letter.isnumeric():
                number = True
        for char in "!@#$%^&*()_+-=;":
            if char in password:
                special = True
        if upper and lower and number and special:
            return True
        else:
            return False



# Create the main window
root = tk.Tk()
root.title("Data Entry")

# Create and place entry widgets
title = tk.Label(text="Sign up")
title.pack()
entry1 = tk.Entry(root)
entry1.insert(0, "Username")
entry1.pack()
entry2 = tk.Entry(root)
entry2.insert(0, "Password")
entry2.pack()
entry3 = tk.Entry(root)
entry3.insert(0, "Re-enter Password")
entry3.pack()

# Create and place the save button
save_button = tk.Button(root, text="Save to CSV", command=save_to_csv)
save_button.pack()

# Create and place the status label
status_label = tk.Label(root, text="")
status_label.pack()

# Start the Tkinter event loop
root.mainloop()
