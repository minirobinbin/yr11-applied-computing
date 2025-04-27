import sqlite3

create_coffee = [
    # """CREATE TABLE IF NOT EXISTS projects (
    #     id INTEGER PRIMARY KEY,
    #     name text NOT NULL,
    #     begin_date DATE,
    #     end_date DATE
    # );""",

    # """CREATE TABLE IF NOT EXISTS tasks (
    #     id INTEGER PRIMARY KEY,
    #     name TEXT NOT NULL,
    #     priority INT,
    #     project_id INT NOT NULL,
    #     status_id INT NOT NULL,
    #     begin_date DATE NOT NULL,
    #     end_date DATE NOT NULL,
    #     FOREIGN KEY (project_id) REFERENCES projects (id)
    # );"""

]

try:
    with sqlite3.connect("cafe.db") as conn:
        print(sqlite3.sqlite_version)
        cursor = conn.cursor()
        for coffee in create_coffee:
            cursor.execute(coffee)
        conn.commit()
        print("Done.")
except sqlite3.OperationalError as e:
    print("Sorry dave, I can't do that right now:", e)
