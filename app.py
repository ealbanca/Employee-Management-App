# A simple Flask application to manage employee records with MySQL database
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)
# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'employee_db'
}
# Route to render the search page
# Search types and their corresponding database columns
@app.route('/')
def index():
    search_type = request.args.get('searchType')
    search_value = request.args.get('searchValue')
    employees = []

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    if search_type and search_value:
        column_map = {
            'name': 'name',
            'email': 'email',
            'phone': 'phone',
            'employeeId': 'employee_id',
            'department': 'department'
        }
        column = column_map.get(search_type, 'name')
        sql = f"SELECT * FROM employees WHERE {column} LIKE %s"
        cursor.execute(sql, (f"%{search_value}%",))
        employees = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('index.html', employees=employees)

# Route to render the search page
#Add employee page with the matching columns of the database
@app.route('/addemployee.html')
def add_employee_page():
    return render_template('addemployee.html')

@app.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    employee_id = request.form['employeeId']
    department = request.form['department']
    start_date = request.form['startDate']
    salary = request.form['salary']
# Connect to the database and insert the new employee record
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = """
        INSERT INTO employees (name, email, phone, employee_id, department, start_date, salary)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (name, email, phone, employee_id, department, start_date, salary)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

# Route to edit an employee's details
@app.route('/edit_employee/<int:employee_id>')
def edit_employee_page(employee_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees WHERE employee_id = %s", (employee_id,))
    employee = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit_employee.html', employee=employee)

@app.route('/update_employee/<int:employee_id>', methods=['POST'])
def update_employee(employee_id):
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    department = request.form['department']
    start_date = request.form['startDate']
    salary = request.form['salary']
# Connect to the database and update the employee record
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = """
        UPDATE employees
        SET name=%s, email=%s, phone=%s, department=%s, start_date=%s, salary=%s
        WHERE employee_id=%s
    """
    values = (name, email, phone, department, start_date, salary, employee_id)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

# Route to delete an employee record
@app.route('/delete_employee/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE employee_id = %s", (employee_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)




