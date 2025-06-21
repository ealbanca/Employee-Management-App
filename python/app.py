from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Update with your MySQL credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'employee_db'
}

@app.route('/')
def index():
    return render_template('addemployee.html')

@app.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    employee_Id = int(request.form['employeeId'])
    department = request.form['department']
    start_date = request.form['startDate']
    salary = request.form['salary']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = """
        INSERT INTO employees (name, email, phone, employee_id, department, start_date, salary)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (name, email, phone, employee_Id, department, start_date, salary)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/search', methods=['GET'])
def search_employee():
    search_type = request.args.get('searchType')
    search_value = request.args.get('searchValue')
    employees = []

    if search_type and search_value:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        # Map form field to actual column name
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
        cursor.close()
        conn.close()
    return render_template('searchemployee.html', employees=employees)