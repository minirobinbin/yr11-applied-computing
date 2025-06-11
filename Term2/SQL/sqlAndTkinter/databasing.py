import sqlite3
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