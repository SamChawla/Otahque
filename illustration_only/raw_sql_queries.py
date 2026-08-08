# illustration_only/raw_sql_queries.py
# Educational illustration only: the queries this chapter writes with the ORM.
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE events_event (
        id INTEGER PRIMARY KEY,
        title VARCHAR(200),
        location VARCHAR(200),
        capacity INTEGER,
        status VARCHAR(10)
    )"""
)
rows = [
    (1, "Intro to Git Workshop", "Innovation Lab", 25, "published"),
    (2, "Django Meetup: July", "Community Hall", 50, "published"),
    (3, "Summer Picnic", "Riverside Park", 100, "draft"),
]
cursor.executemany("INSERT INTO events_event VALUES (?, ?, ?, ?, ?)", rows)

# 1. Filtering: Event.objects.filter(status=...)
cursor.execute("SELECT title FROM events_event WHERE status = ?", ("published",))
print([row[0] for row in cursor.fetchall()])

# 2. Aggregation: aggregate(Count("id"), Sum("capacity"))
cursor.execute("SELECT COUNT(*), SUM(capacity) FROM events_event WHERE status = ?", ("published",))
print(cursor.fetchone())

# 3. OR conditions: filter(Q(capacity__gte=50) | Q(location="Community Hall"))
cursor.execute(
    "SELECT title FROM events_event WHERE status = ? AND (capacity >= ? OR location = ?)",
    ("published", 50, "Community Hall"),
)
print([row[0] for row in cursor.fetchall()])
connection.close()
