# microsoft access - sql queries but weird (not v. user-friendly)

import sqlite3

conn = sqlite3.connect('students.sqlite')
cursor = conn.cursor()

# noinspection SqlNoDataSourceInspection
create_students_table = """
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
firstname TEXT NOT NULL,
lastname TEXT NOT NULL,
age INTEGER,
gender TEXT)
"""
cursor.execute(create_students_table)

conn.close() # make sure to end program with database closing

# commit - locally there is a milestone which you can travel back to
# push pushes to git --> puts into current branch