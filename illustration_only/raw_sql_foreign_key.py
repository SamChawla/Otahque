# illustration_only/raw_sql_foreign_key.py
# Educational illustration only: the plumbing behind ForeignKey.
import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

cursor.execute("CREATE TABLE events_category (id INTEGER PRIMARY KEY, name VARCHAR(100))")
cursor.execute(
    """CREATE TABLE events_event (
        id INTEGER PRIMARY KEY,
        title VARCHAR(200),
        category_id INTEGER REFERENCES events_category (id)
    )"""
)
cursor.execute("INSERT INTO events_category VALUES (1, 'Talks')")
cursor.execute("INSERT INTO events_event VALUES (1, 'Django Meetup: July', 1)")

# The constraint works: a category that does not exist is rejected.
try:
    cursor.execute("INSERT INTO events_event VALUES (2, 'Ghost Event', 99)")
except sqlite3.IntegrityError as error:
    print("IntegrityError:", error)

# Traversal means writing the JOIN yourself, every time.
cursor.execute(
    """SELECT events_event.title, events_category.name
       FROM events_event
       JOIN events_category ON events_event.category_id = events_category.id"""
)
print(cursor.fetchall())
connection.close()
