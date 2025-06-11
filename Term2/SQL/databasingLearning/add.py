import sqlite3

database_path = "coffee.db"

create = """INSERT INTO projects VALUES (2, "jeff", "24/04/2025", "25/04/2025");"""


with sqlite3.connect(database_path) as conn:
    cursor = conn.cursor()
    cursor.execute(create)
    conn.commit()