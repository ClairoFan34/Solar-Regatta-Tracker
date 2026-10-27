import sqlite3

connection = sqlite3.connect("tracker.db")
cursor = connection.cursor()

cursor.execute( """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    owner TEXT NOT NULL,
    subteam TEXT NOT NULL,
    due TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'to do',
    posted DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")

sample_tasks = [
    ("Wire battery to motor controller", "Ana", "Electrical", "2026-10-30", "in progress"),
    ("Seal pontoon seams", "Luis", "Pontoon", "2026-11-05", "to do"),
    ("Test hydrofoil angle", "Sofia", "Hydrofoil", "2026-10-25", "to do"),
]

cursor.executemany(
    "INSERT INTO tasks (title, owner, subteam, due, status) VALUES (?, ?, ?, ?, ?)", 
    sample_tasks,
)

connection.commit()
connection.close()

print("Data base has been created!!!!!! :3")