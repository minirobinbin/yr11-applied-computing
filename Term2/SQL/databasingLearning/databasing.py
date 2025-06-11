import sqlite3

database_path = "coffee.db"

projects = """CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY,
        name text NOT NULL,
        begin_date DATE,
        end_date DATE
    );"""

tasks = """CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        priority INT,
        project_id INT NOT NULL,
        status_id INT NOT NULL,
        begin_date DATE NOT NULL,
        end_date DATE NOT NULL,
        FOREIGN KEY (project_id) 
        REFERENCES projects (id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );"""



with sqlite3.connect(database_path) as conn:
    cursor = conn.cursor()
    cursor.execute(projects)
    cursor.execute(tasks)
    conn.commit()