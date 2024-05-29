import sqlite3
import os

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

for i in os.listdir('static'):
    cur.execute("INSERT INTO predictions (prompt,id) VALUES (?, ?)",
                (f'{i.split(".")[0]}', None)
                )

connection.commit()
connection.close()