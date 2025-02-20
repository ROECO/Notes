import sqlite3
import os
from os.path import exists
import uuid
# constants
conn = sqlite3.connect('notes.db')
cursor = conn.cursor()
DB_PATH = "notes.db"




# basic sql error handling
def get_connection():
    """Returns a new database connection, ensuring the database exists."""
    if not os.path.exists(DB_PATH):
        print("Error: Database file 'notes.db' is missing. Please run setup.sql.")
        exit(1)
    return sqlite3.connect(DB_PATH)

# helper functions

def execute_query(query, params=(), fetchone=False, fetchall=False, commit=True):
    """Executes a SQL query with optional parameters and handling."""
    conn= get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)

    result = None
    if fetchone:
        result = cursor.fetchone()
    elif fetchall:
        result = cursor.fetchall()
    if commit:
        conn.commit()
    conn.close()
    return result
def generate_id():
    return str(uuid.uuid4())

# CRUD functions
def find_make_category(category_name):
    """Returns category ID, creating it if necessary."""
    category = execute_query("select id FROM categories WHERE name = ?",
                             (category_name,), fetchone=True)
    if category:
        return category[0]

    execute_query("INSERT INTO categories (name) VALUES (?)",
                  (category_name,),
                  commit = True)
    return execute_query("SELECT id FROM categories WHERE name = ?",
                         (category_name,),
                         fetchone=True)[0]

def remove_note(note_id):
    note = execute_query("SELECT id FROM notes WHERE id = ?",
                         (note_id,),
                         fetchone=True)

    if note:
        execute_query("DELETE FROM notes WHERE id = ?",
                      (int(note_id),),
                      commit = True)
        return True
    else:
         print("Error: Note id '{}' doesn't exist.".format(note_id))
         return False

# def create_note(note_id):
#     if note_id = is None:
#         note = execute_query("INSERT INTO notes (name) VALUES (?)",)
#
#
