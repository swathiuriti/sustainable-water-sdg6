import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/sdg6.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS hygiene_assessments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER,
    recommendation TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sanitation_assessments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER,
    recommendation TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS community_reports(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    issue_type TEXT,
    location TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database and tables created successfully")