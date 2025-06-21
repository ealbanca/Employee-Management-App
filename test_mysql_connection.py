import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",      # <-- replace with your MySQL username
    password="password",  # <-- replace with your MySQL password
    database="employee_db"           # <-- replace with your database name
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Example: Check connection
print("Connected to MySQL database!")

# Don't forget to close the connection when done
cursor.close()
conn.close()