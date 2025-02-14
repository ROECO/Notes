import sqlite3

conn = sqlite3.connect("../notes.db")  # Create or open database
cursor = conn.cursor()

# Check if "projects" category exists
cursor.execute("SELECT id FROM categories WHERE name = ?", ("projects",))
projects = cursor.fetchone()

# add notes if category exists
if projects:
    category_id = projects[0]
else:
    print("No category 'projects' found, creating one...")
    cursor.execute("INSERT INTO categories (name) VALUES (?)", ("projects",))
    category_id = cursor.lastrowid # Get the new category ID

cursor.execute("INSERT INTO notes (title, category_id, content) VALUES (?, ?, ?)", ("My Note", category_id, "This is my first note in projects."))
conn.commit()

# Retrieve notes

def retrieve_notes(category):
    return cursor.execute("""
        SELECT notes.id, notes.title, notes.content, categories.name AS category
        FROM notes
        JOIN categories ON notes.category_id = categories.id
        WHERE categories.name = ?
    """, (category,)).fetchall()

cursor.execute("SELECT * FROM notes")
print(cursor.fetchall())

conn.close()