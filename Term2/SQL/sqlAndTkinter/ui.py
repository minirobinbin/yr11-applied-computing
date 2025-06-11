import tkinter as tk
import sqlite3

root = tk.Tk()
root.title("SQL UI")
root.geometry("400x400")
uitable = tk.Tk()
uitable.title("SQL table")
uitable.geometry("400x400")

database_path = "trains.db"

select = """SELECT * FROM trains"""
with sqlite3.connect(database_path) as conn:
    cursor = conn.cursor()
    rows = cursor.execute(select).fetchall()
showData = ''
for data in rows:
        showData += str(data) + "\n"
table = tk.Label(uitable, text=showData)
table.pack()

def uitables():
    database_path = "trains.db"

    select = """SELECT * FROM trains"""
    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        rows = cursor.execute(select).fetchall()
    showData = ''
    for data in rows:
            showData += str(data) + "\n"
    table.config(text=showData)
    


def add():
    database_path = "trains.db"

    create = """INSERT INTO trains (station_name, line_name, trains, old_trains, about) 
           VALUES (?, ?, ?, ?, ?)"""

    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute(create, (
            station_name.get(),
            line_name.get(),
            trains.get(),
            former_trains.get(),
            about.get()
        ))
        conn.commit()
    uitables()
    status.config(text=f"Added {station_name.get()}")
    root.after(1000, lambda: status.config(text=''))

def createtable():
    database_path = "trains.db"

    trains = """CREATE TABLE IF NOT EXISTS trains (
            station_name TEXT NOT NULL,
            line_name TEXT NOT NULL,
            trains TEXT NOT NULL,
            old_trains TEXT NOT NULL,
            about TEXT NOT NULL
        );"""

    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute(trains)
        conn.commit()
    uitables()
    status.config(text="Created table")
    root.after(1000, lambda: status.config(text=''))

def deletetable():
    database_path = "trains.db"

    delete1 = """DROP TABLE trains;"""


    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute(delete1)
        conn.commit()
    uitables()
    status.config(text="Deleted table")
    root.after(1000, lambda: status.config(text=''))

def deletedata():
    database_path = "trains.db"

    delete1 = """DELETE FROM trains WHERE station_name = ?;"""

    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute(delete1, (
            station_name.get(),
        ))
        conn.commit()
    uitables()
    status.config(text=f"Deleted {station_name.get()}")
    root.after(1000, lambda: status.config(text=''))

def add_placeholder(entry, placeholder):
    # Function to add the placeholder if the entry is empty
    if not entry.get():
        entry.insert(0, placeholder)
        entry.config(fg='grey')

def remove_placeholder(entry, placeholder):
    # Function to remove the placeholder if it's currently displayed
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg='white')


root.columnconfigure((0,1, 2),weight=1)
root.rowconfigure((0,1,2,3),weight=1)

image = tk.PhotoImage(file="xtrapolis.png").subsample(24,24)
tk.Label(root, image=image).grid(row=2, column=1)

create_table = tk.Button(root, text="Create table", command=createtable)
create_table.grid(row=3, column=0)


delete_table = tk.Button(root, text="Delete table", command=deletetable)
delete_table.grid(row=3, column=2)

station_name = tk.Entry(root)
station_name.grid(row=0, column=0)
station_name.insert(0, 'Station name')
station_name.config(fg='grey')

line_name = tk.Entry(root)
line_name.grid(row=0, column=1)
line_name.insert(0, 'Line name')
line_name.config(fg='grey')

trains = tk.Entry(root)
trains.grid(row=0, column=2)
trains.insert(0, 'Trains')
trains.config(fg='grey')

former_trains = tk.Entry(root)
former_trains.grid(row=1, column=0)
former_trains.insert(0, 'Old trains')
former_trains.config(fg='grey')

about = tk.Entry(root)
about.grid(row=1, column=1)
about.insert(0, 'About')
about.config(fg='grey')

save_button = tk.Button(root, text="Add data", command=add)
save_button.grid(row=1, column=2, sticky='n')

delete_button = tk.Button(root, text="Delete data", command=deletedata)
delete_button.grid(row=1, column=2, sticky='s')

status = tk.Label(root, text="")
status.grid(row=3, column=1)

station_name.bind("<FocusIn>", lambda e: remove_placeholder(station_name, "Station name"))
station_name.bind("<FocusOut>", lambda e: add_placeholder(station_name, "Station name"))

line_name.bind("<FocusIn>", lambda e: remove_placeholder(line_name, "Line name"))
line_name.bind("<FocusOut>", lambda e: add_placeholder(line_name, "Line name"))

trains.bind("<FocusIn>", lambda e: remove_placeholder(trains, "Trains"))
trains.bind("<FocusOut>", lambda e: add_placeholder(trains, "Trains"))

former_trains.bind("<FocusIn>", lambda e: remove_placeholder(former_trains, "Old trains"))
former_trains.bind("<FocusOut>", lambda e: add_placeholder(former_trains, "Old trains"))

about.bind("<FocusIn>", lambda e: remove_placeholder(about, "About"))
about.bind("<FocusOut>", lambda e: add_placeholder(about, "About"))



uitable.mainloop()
root.mainloop()