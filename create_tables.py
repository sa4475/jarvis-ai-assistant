import sqlite3

# Connect to (or create) the database
con = sqlite3.connect('jarvis.db')
cursor = con.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS sys_command (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    path TEXT
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS web_command (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    url TEXT
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    mobile_no TEXT
)''')

# Insert sample data
cursor.execute("INSERT INTO sys_command (name, path) VALUES (?, ?)", ("notepad", r"C:\\Windows\\System32\\notepad.exe"))
cursor.execute("INSERT INTO web_command (name, url) VALUES (?, ?)", ("google", "https://www.google.com"))
cursor.execute("INSERT INTO contacts (name, mobile_no) VALUES (?, ?)", ("sahyog", "+911234567890"))

con.commit()
con.close()

print("Tables created and sample data inserted.") 