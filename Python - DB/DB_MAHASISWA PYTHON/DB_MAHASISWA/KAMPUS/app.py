#Author  FIKRI HADI NUGRAHA
# APLIKASI SEDERHANA DATABASE KAMPUS 


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
    database ='db_kampus'     # DataBase yang dipakai
   )
   cursor = conn.cursor()
   
# Function to close database connection
def closeDb():
   global conn, cursor
   cursor.close()
   conn.close()
   
### login system ##
@application.route('/login', methods=['GET', 'POST'])
def login():
    openDb()
    message = ''
    if request.method == 'POST':
        if request.form:
            email = request.form['email']
            password = request.form['password']
            sql = "SELECT * FROM user WHERE email = '%s' AND password = '%s'" % (email, password)
            cursor.execute(sql)
            user = cursor.fetchone()
            if user:
                session['loggedin'] = True
                return redirect(url_for('view'))
    message = 'login salah'
    return render_template('login/login.html', message=message)

### Register Login ## 
@application.route('/register', methods =['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password =  request.form['password']
        openDb()
        sql = "INSERT INTO user (email,password) VALUES (%s, %s)"
        val = (email,password)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('login'))
    else:
        return render_template('login/register.html')
        
    
@application.route('/page')
def page():
    #Tambahkan logika untuk halaman utama disini
    return render_template('page.html')

######################################## DATA MAHASISWA ######################################################
#Fungsi untuk menampilkan DataBase Mahasiswa dari DB_Kampus
@application.route('/view')
def view():
    openDb()
    container = []
    sql = "SELECT * FROM mahasiswa"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
      container.append(data)
    closeDb()
    return render_template('datamahasiswa/index.html', container=container,)
#Fungsi untuk edit data
@application.route('/edit/<id_mahasiswa>', methods=['GET','POST'])
def edit(id_mahasiswa):
   openDb()
   cursor.execute("SELECT * FROM mahasiswa WHERE id_mahasiswa=%s", (id_mahasiswa,))
   data = cursor.fetchone()
   if request.method == 'POST':
      id_mahasiswa = request.form['id_mahasiswa']
      NIM = request.form['nim']
      nama = request.form['nama']
      Fakultas = request.form['fakultas']
      Prodi = request.form['prodi']
      PHONE = request.form['phone']
      Email = request.form['email']
      Alamat = request.form['alamat']
      sql = "UPDATE mahasiswa SET nim=%s,nama_mahasiswa=%s,fakultas=%s,prodi=%s,phone=%s, email=%s, alamat=%s WHERE id_mahasiswa=%s"
      val = (NIM,nama, Fakultas,Prodi,PHONE,Email,Alamat, id_mahasiswa)
      cursor.execute(sql, val)
      conn.commit()
      closeDb()
      return redirect(url_for('view'))
   else:
      closeDb()
      return render_template('datamahasiswa/edit.html', data=data)
  
#fungsi view tambah() untuk membuat form tambah
@application.route('/tambah', methods=['GET','POST'])
def tambah():
   if request.method == 'POST':
      NIM = request.form['nim']
      nama = request.form['nama']
      Fakultas = request.form['fakultas']
      Prodi = request.form['prodi']
      PHONE = request.form['phone']
      Email = request.form['email']
      Alamat = request.form['alamat']
      openDb()
      sql = "INSERT INTO mahasiswa (nim,nama_mahasiswa,fakultas,prodi,phone,email,alamat) VALUES (%s, %s, %s,%s,%s,%s,%s)"
      val = (NIM,nama,Fakultas,Prodi,PHONE,Email,Alamat)
      cursor.execute(sql, val)
      conn.commit()
      closeDb()
      return redirect(url_for('view'))
   else:
      return render_template('datamahasiswa/tambah.html') 
#fungsi untuk menghapus data
@application.route('/hapus/<id_mahasiswa>', methods=['GET','POST'])
def hapus(id_mahasiswa):
   openDb()
   cursor.execute('DELETE FROM mahasiswa WHERE id_mahasiswa=%s', (id_mahasiswa,))
   conn.commit()
   closeDb()
   return redirect(url_for('view'))
######################################## DATA MAHASISWA ######################################################


if __name__ == '__main__':
    application.run(debug=True, port='3000')
    closeDb()