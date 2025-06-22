# Overview

This is an employee management web application built with Flask and MySQL for managing employee records. The app allows users to:

- Add new employees with details such as name, email, phone, employee ID, department, start date, and hourly salary.
- Search for employees by name, email, phone, employee ID, or department.
- View a list of employees in a table format.
- Edit employee details by clicking the "Edit" button next to an employee’s record.
- Delete employees by clicking the "Delete" button, with a confirmation prompt.
All employee data is stored in a MySQL database. The app uses HTML templates for the user interface and supports basic features like Create, Read, Update, and Delete operations for employee management.
Since this uses a local database, please Run the createTable.py file (Don't forget to update the database configuration user and password on the cretaeTable.py and app.py file with your local credentials).

[Demo Video](https://youtu.be/O5D6bLyjQjw )

# Relational Database

The relational database for this Employee Management App is a MySQL database named employee_db. It contains a main table called employees that stores all employee records.

- id	INT, PRIMARY KEY, AUTO_INCREMENT	Unique internal identifier for each record
- name	VARCHAR	The employee's full name
- email	VARCHAR	The employee's email address
- phone	VARCHAR	The employee's phone number
- employee_id	INT or VARCHAR	The unique employee ID
- department	VARCHAR	The department the employee belongs to
- start_date	DATE	The date the employee started
- salary	DECIMAL/DOUBLE	The employee's hourly salary

# Development Environment

- Frontend (HTML, CSS, and JavaScript)
- Backend (Python - using Flask as the web framework)
- Database (SQL - using a relational database MySQL)

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Pallets Projects](http://url.link.goes.here](https://flask.palletsprojects.com/en/stable/ )
- [Geeks for Geeks](https://www.geeksforgeeks.org/python/flask-tutorial/)
