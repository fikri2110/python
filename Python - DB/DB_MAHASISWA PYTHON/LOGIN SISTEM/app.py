#Author = FIKRI HADI NUGRAHA
# Python DataBase System CRUD 

from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

application = Flask(__name__)
application.secret_key = 'something_secret_and_unique'

conn = cursor = None

# Function to open database connection
def openDb():
   global conn, cursor
   conn = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password = '',
    database ='dbuser'    
   )
   cursor = conn.cursor()
   
# Function to close database connection
def closeDb():
   global conn, cursor
   cursor.close()
   conn.close()
   
@application.route('/login', methods=['GET', 'POST'])
def login():
    openDb()
    message = ''
    if request.method == 'POST':
        if request.form:
            username = request.form['username']
            password = request.form['password']
            sql = "SELECT * FROM login WHERE username = '%s' AND password = '%s'" % (username, password)
            cursor.execute(sql)
            user = cursor.fetchone()
            if user:
                session['loggedin'] = True
                return redirect(url_for('dosen'))
    message = 'login salah'
    return render_template('login.html', message=message)

@application.route('/dosen')
def dosen():
    return render_template('dosen.html')

if __name__ == '__main__':
    application.run(debug=True, port='3000')
    closeDb()