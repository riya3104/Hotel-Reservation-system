import sqlite3

conn = sqlite3.connect('database/hotel.db')
cursor = conn.cursor()

# Create table for rooms
cursor.execute('''
CREATE TABLE IF NOT EXISTS rooms (
    room_id INTEGER PRIMARY KEY,
    room_type TEXT NOT NULL,  -- 'AC' or 'Non-AC'
    status TEXT NOT NULL      -- 'Available' or 'Booked'
)
''')

# Insert 15 rooms (some AC, some Non-AC)
rooms = [
    (1, 'AC', 'Available'), (2, 'Non-AC', 'Available'), (3, 'AC', 'Available'),
    (4, 'Non-AC', 'Available'), (5, 'AC', 'Available'), (6, 'Non-AC', 'Available'),
    (7, 'AC', 'Available'), (8, 'Non-AC', 'Available'), (9, 'AC', 'Available'),
    (10, 'Non-AC', 'Available'), (11, 'AC', 'Available'), (12, 'Non-AC', 'Available'),
    (13, 'AC', 'Available'), (14, 'Non-AC', 'Available'), (15, 'AC', 'Available')
]

cursor.executemany('INSERT OR IGNORE INTO rooms (room_id, room_type, status) VALUES (?, ?, ?)', rooms)

conn.commit()
conn.close()
