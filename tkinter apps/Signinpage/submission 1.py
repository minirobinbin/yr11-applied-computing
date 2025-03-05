import tkinter as tk
import csv

def save_to_csv():
    # get the data from the entries and store it as a list called data
    data = [entry1.get(), entry2.get(), entry3.get()]
    determine = list(entry2.get())
    # open a csv file called data.csv in the write mode, create a writer, and write data as a row
    with open('data.csv','r', newline='') as file:
        reader = csv.reader(file)
        has_uppercase = any(char.isupper() for char in determine) 
        has_lowercase = any(char.islower() for char in determine) 
        has_special = any(not char.isalnum() for char in determine)
        has_number = any(char.isdigit() for char in determine)  
        if has_uppercase and has_lowercase and has_special and has_number:
            if data in reader:
                status_label.config(text="already signed in!")
            elif entry2.get() != entry3.get():
                status_label.config(text="not same password!")
            else:
                with open('data.csv','a', newline='') as file_append:
                    writer = csv.writer(file_append)
                    writer.writerow(data)
                    status_label.config(text="Data saved to data.csv!")
                    entry1.delete(0, tk.END)
                    entry2.delete(0, tk.END)
                    entry3.delete(0, tk.END)
                    entry1.insert(0, 'Username')
                    entry2.insert(0, 'Password')
                    entry3.insert(0, 'Confirm password')
        else:
            if not has_uppercase:
                status_label.config(text="Need uppercase letter!")
            elif not has_lowercase:
                status_label.config(text="Need lowercase letter!")
            elif not has_special:
                status_label.config(text="Need special character!")
            elif not has_number:
                status_label.config(text="Need number!")
    # config the status label to read "Data saved to data.csv"
    
    # after 3000 cycles config the status label to ""
    root.after(1000, lambda: status_label.config(text=''))



# def delayed_action():
#     status_label.config(text='')
    
def add_placeholder(entry, placeholder):
    # Function to add the placeholder if the entry is empty
    if not entry.get():
        entry.insert(0, placeholder)
        entry.config(fg='grey')

def remove_placeholder(entry, placeholder):
    # Function to remove the placeholder if it's currently displayed
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg='black')

# Create the main window
root = tk.Tk()
root.title("Totally a real sign in page")
root.geometry("300x300+50+50")

# Create and place the status label
status_label = tk.Label(root, text="")
status_label.pack()

# Create and place entry widgets
entry1 = tk.Entry(root)
entry1.pack()
entry1.insert(0, 'Username')
entry1.config(fg='grey')
entry2 = tk.Entry(root)
entry2.pack()
entry2.insert(0, 'Password')
entry2.config(fg='grey')
entry3 = tk.Entry(root)
entry3.pack()
entry3.insert(0, 'Confirm password')
entry3.config(fg='grey')



def help():
    determine = list(entry2.get())
    status_label.config(text=determine)
    root.after(3000, lambda: status_label.config(text=''))

help_button = tk.Button(root, text="Help", command=help)
help_button.pack()
# Create and place the save button
save_button = tk.Button(root, text="Save to CSV", command=save_to_csv)
save_button.pack()

entry3.bind("<FocusIn>", lambda e: remove_placeholder(entry3, "Password"))
entry3.bind("<FocusOut>", lambda e: add_placeholder(entry3, "Password"))



# Start the Tkinter event loop
root.mainloop()
