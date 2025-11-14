# Hotel Reservation System

A simple Hotel Reservation Management System built using Python (Flask), SQLite database, and HTML templates.  
This project demonstrates CRUD operations, SQL queries, database handling, and basic web-based reservation features.

---

## 📌 Project Overview

The Hotel Reservation System allows users to:
- Book a hotel room  
- View all reservations  
- Cancel an existing reservation  
- Update reservation details  
- Store all information securely in an SQLite database  

This project reflects real-world database usage and SQL operations, making it suitable for demonstrating hands-on experience in SQL and backend development.

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Database:** SQLite  
- **Frontend:** HTML5, CSS (basic)  
- **Tools:** SQL queries, Python database connectivity (sqlite3)

---

## 📂 Folder Structure

Hotel-Reservation-system/
│── app.py # Main Flask application
│── create_db.py # Script to create the SQLite database
│── update_database.py # Script to update database entries
│── templates/
│ ├── index.html # Home page
│ ├── book.html # Room booking page
│ ├── display.html # Display reservations
│ ├── cancel.html # Cancel a reservation
│── Screenshot.png # Project screenshot


---

## 🧩 Features

### ✔ Room Booking  
Users can enter:
- Name  
- Check-in date  
- Check-out date  
- Room type  

The system stores this data in the database using SQL INSERT operations.

### ✔ Display Reservations  
Shows all bookings using SQL SELECT queries.

### ✔ Cancel Reservation  
Allows users to cancel using reservation ID (SQL DELETE).

### ✔ Update Reservation  
Modifies existing booking details using SQL UPDATE queries.

---

## 🗄️ Database Details (SQLite)

### **Table: reservations**

| Column Name | Type     | Description               |
|------------|----------|---------------------------|
| id         | INTEGER  | Primary key (auto)        |
| name       | TEXT     | Customer name             |
| checkin    | TEXT     | Check-in date             |
| checkout   | TEXT     | Check-out date            |
| roomtype   | TEXT     | Selected room category    |

The database is created using `create_db.py`.

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
pip install flask


### 2️⃣ Create the database
python create_db.py


### 3️⃣ Run the application
python app.py

## 🧪 SQL Operations Used

This project demonstrates:

- **CREATE TABLE**
- **INSERT**
- **SELECT**
- **UPDATE**
- **DELETE**
- **Joins not required** (single-table system)
- **Constraints: Primary key (auto increment)**


## 📸 Screenshot

<img width="797" height="714" alt="Screenshot 2025-11-14 211203" src="https://github.com/user-attachments/assets/a383746b-df70-49ad-afe1-45d70a6fe719" />
<img width="1263" height="369" alt="Screenshot 2025-11-14 211336" src="https://github.com/user-attachments/assets/1425e682-e7f9-4e7d-8a1e-c4dce4153bf6" />
<img width="1123" height="667" alt="Screenshot 2025-11-14 211531" src="https://github.com/user-attachments/assets/a2636428-5e35-4d1d-bedb-36cedf1b435c" />

## 📘 Purpose of the Project

This project was developed as part of backend & database learning to:

- Practice SQL queries in a real scenario  
- Understand how Python interacts with SQL databases  
- Build a functional system using CRUD operations  
- Demonstrate hands-on SQL experience for placements  




