import tkinter as tk
from tkinter import messagebox  # This example has messageboxes


# ======== Define commands =========
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Here you would typically check the username and
    # password against a database
    # For this example, we'll use a simple condition
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        if username == "" or password == "":
            messagebox.showerror("Lgin Failed", "Please eneter a username and password")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


# ========= Create the main window ==========
root = tk.Tk()
root.title("Login")
root.geometry("300x150")

# ======= Create Widgets ===========
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)
# Create the password label and entry
password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show="*")
# The show="*" argument hides the password
# Create the login button
login_button = tk.Button(root, text="Login", command=login)

# ====== Place widgets =========
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
