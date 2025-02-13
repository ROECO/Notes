import sqlite3

conn = sqlite3.connect("notes.db")  # Create or open database
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")



# Insert a test note
cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", ("My Note", "This is my first note."))
conn.commit()

# Retrieve notes
cursor.execute("SELECT * FROM notes")
print(cursor.fetchall())

conn.close()