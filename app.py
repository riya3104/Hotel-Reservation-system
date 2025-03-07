from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database/hotel.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    conn = get_db_connection()
    if request.method == 'POST':
        room_id = request.form['room_id']
        room_type = request.form['room_type']
        check_in_date = request.form['check_in_date']
        check_out_date = request.form['check_out_date']

        # Check room availability
        room = conn.execute('SELECT * FROM rooms WHERE room_id = ? AND room_type = ? AND status = "Available"', 
                            (room_id, room_type)).fetchone()

        if room:
            # Update room status and store check-in/check-out dates
            conn.execute('UPDATE rooms SET status = "Booked", check_in_date = ?, check_out_date = ? WHERE room_id = ?', 
                         (check_in_date, check_out_date, room_id))
            conn.commit()
            message = f"Room booked successfully! Check-in: {check_in_date}, Check-out: {check_out_date}"
        else:
            message = "Room is not available or doesn't match type."
        conn.close()
        return render_template('book.html', message=message)
    return render_template('book.html')


@app.route('/cancel', methods=['GET', 'POST'])
def cancel():
    conn = get_db_connection()
    if request.method == 'POST':
        room_id = request.form['room_id']
        # Cancel the booking by making the room "Available"
        conn.execute('UPDATE rooms SET status = "Available" WHERE room_id = ?', (room_id,))
        conn.commit()
        conn.close()
        return redirect(url_for('display'))
    return render_template('cancel.html')

@app.route('/display')
def display():
    conn = get_db_connection()
    rooms = conn.execute('SELECT * FROM rooms').fetchall()
    conn.close()
    return render_template('display.html', rooms=rooms)

if __name__ == '__main__':
    app.run(debug=True)
