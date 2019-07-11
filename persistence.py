import sqlite3

conn = sqlite3.connect('./database/passwdng.db')

cursor = conn.cursor()

with open('./database/passwdng_schema.sql') as f:
    db_schema = f.read()
    cursor.executescript(db_schema)


conn.close()