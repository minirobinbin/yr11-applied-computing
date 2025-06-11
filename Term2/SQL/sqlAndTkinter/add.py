import sqlite3

def add():
    database_path = "trains.db"

    create = """INSERT INTO trains (station_name, line_name, trains, old_trains, about) 
           VALUES (?, ?, ?, ?, ?)"""


    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute(create, (
            ui.station_name.get(),
            ui.line_name.get(),
            ui.trains.get(),
            ui.former_trains.get(),
            ui.about.get()
        ))
        conn.commit()