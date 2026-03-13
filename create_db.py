import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
date TEXT,
revenue INTEGER
)
""")

# Keep setup deterministic on repeated runs.
cursor.execute("DELETE FROM sales")
cursor.execute("INSERT INTO sales VALUES ('2026-03-13',12000)")
cursor.execute("INSERT INTO sales VALUES ('2026-03-12',9000)")

conn.commit()
conn.close()