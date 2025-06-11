import tkinter as tk
import sqlite3

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
uitable.mainloop()