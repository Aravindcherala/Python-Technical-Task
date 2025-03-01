from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(_name_)

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="companyDB",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    age = request.form['age']
    city = request.form['city']
    email = request.form['email']
    salary = request.form['salary']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, age, city, email, salary) VALUES (%s, %s, %s, %s, %s)", 
                   (name, age, city, email, salary))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        email = request.form['email']
        salary = request.form['salary']

        cursor.execute("UPDATE employees SET name=%s, age=%s, city=%s, email=%s, salary=%s WHERE id=%s", 
                       (name, age, city, email, salary, id))
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        cursor.execute("SELECT * FROM employees WHERE id=%s", (id,))
        employee = cursor.fetchone()
        conn.close()
        return render_template('edit.html', employee=employee)

@app.route('/delete/<int:id>')
def delete_employee(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if _name_ == '_main_':
    app.run(debug=True)