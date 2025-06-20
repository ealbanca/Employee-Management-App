import mysql.connector

# Replace with your MySQL credentials
conn = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="employee_db"  # Use the database you created
)

if conn.is_connected():
    print("Connection successful!")
else:
    print("Connection failed.")

conn.close()