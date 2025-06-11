import sqlite3
def deletetable():
    database_path = "trains.db"

    delete1 = """DROP TABLE trains;"""


    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute(delete1)
        conn.commit()
