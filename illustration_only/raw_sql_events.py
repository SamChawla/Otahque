# illustration_only/raw_sql_events.py
# Educational illustration only: the manual work Django's ORM does for us.
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# 1. We write the schema by hand, and nothing checks it against our code.
cursor.execute(
    """CREATE TABLE events_event (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(200) NOT NULL,
        slug VARCHAR(50) NOT NULL UNIQUE,
        starts_at TIMESTAMP NOT NULL,
        capacity INTEGER NOT NULL DEFAULT 50,
        status VARCHAR(10) NOT NULL DEFAULT 'draft'
    )"""
)

# 2. Inserting means hand-matching placeholders to columns, in order.
cursor.execute(
    "INSERT INTO events_event (title, slug, starts_at) VALUES (?, ?, ?)",
    ("Django Meetup: July", "django-meetup-july", "2026-07-18 18:00:00"),
)
connection.commit()

# 3. Reading back gives anonymous tuples, not objects.
cursor.execute("SELECT id, title, status FROM events_event")
row = cursor.fetchone()
print(row)
print(f"title is field number 1: {row[1]}")

connection.close()
