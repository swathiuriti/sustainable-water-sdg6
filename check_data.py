import sqlite3

conn = sqlite3.connect("database/sdg6.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM hygiene_assessments")
print(cursor.fetchall())

conn.close()