import sqlite3

# Connect to the existing database
conn = sqlite3.connect('database/hotel.db')
cursor = conn.cursor()

# Add new columns to the rooms table
try:
    cursor.execute('ALTER TABLE rooms ADD COLUMN check_in_date TEXT')
    cursor.execute('ALTER TABLE rooms ADD COLUMN check_out_date TEXT')
    print("Columns added successfully.")
except sqlite3.OperationalError as e:
    print("Error:", e)

# Commit the changes and close the connection
conn.commit()
conn.close()
