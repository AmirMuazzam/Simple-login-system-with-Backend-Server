import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
""")

# Insert sample user data
users_data = [
    ("john", "password123"),
    ("jane", "password456"),
    ("smith", "password789")
]

cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users_data)

# Commit the changes and close the database connection
conn.commit()
conn.close()
