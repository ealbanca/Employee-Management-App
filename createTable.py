import mysql.connector

# Database configuration - Update it with the local MySQL database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password'
}

def create_database_and_table():
    # Connect to MySQL server
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")
    cursor.execute("USE employee_db")

    # Create employees table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            phone VARCHAR(15),
            department VARCHAR(50),
            start_date DATE,
            salary DECIMAL(10, 2)
        )
    """)

    # Commit changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_database_and_table()