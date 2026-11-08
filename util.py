import sqlite3

con = sqlite3.connect('async_tasks.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tasks
               (
                id INTEGER PRIMARY KEY AUTOINCREMENT,   
                    status TEXT NOT NULL,
                    duration INTEGER NOT NULL
                    )'''
            )