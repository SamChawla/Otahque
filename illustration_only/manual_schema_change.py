# illustration_only/manual_schema_change.py
# Educational illustration only: schema management without migrations.
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Monday: the table ships to production.
cursor.execute("CREATE TABLE events_event (id INTEGER PRIMARY KEY, title VARCHAR(200))")

# Wednesday: someone adds a column, live, by hand.
cursor.execute("ALTER TABLE events_event ADD COLUMN capacity INTEGER DEFAULT 50")

# Friday: what does the schema look like now? Only the database knows.
cursor.execute("SELECT name FROM pragma_table_info('events_event')")
print([row[0] for row in cursor.fetchall()])

connection.close()
