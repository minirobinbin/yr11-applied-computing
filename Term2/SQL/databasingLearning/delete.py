import sqlite3

database_path = "coffee.db"

delete1 = """DROP TABLE projects;"""

delete2 = """DROP TABLE tasks;"""

with sqlite3.connect(database_path) as conn:
    cursor = conn.cursor()
    cursor.execute(delete1)
    cursor.execute(delete2)
    conn.commit()