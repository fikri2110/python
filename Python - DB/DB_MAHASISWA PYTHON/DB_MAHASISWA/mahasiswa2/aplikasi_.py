#Author = FIKRI HADI NUGRAHA
# Python DataBase Sistem CRUD 

from flask import Flask, render_template, \
  request, redirect, url_for
import mysql.connector

application = Flask(__name__)

conn = cursor = None
#fungsi koneksi database
def openDb():
   global conn, cursor
   conn = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password = '',
    database ='db_mahasiswa'    
)
   cursor = conn.cursor()	
   
#fungsi untuk menutup koneksi
def closeDb():
   global conn, cursor
   cursor.close()
   conn.close()
   
@application.route('/show')
def show():
   return render_template('show.html')

#fungsi view index() untuk menampilkan data dari database
@application.route('/view')
def index():   
   openDb()
   container = []
   sql = "SELECT * FROM datamahasiswa"
   cursor.execute(sql)
   results = cursor.fetchall()
   for data in results:
      container.append(data)
   closeDb()
   return render_template('index.html', container=container,)

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
      sql = "INSERT INTO datamahasiswa (nim,nama_mahasiswa,fakultas,prodi,phone,email,alamat) VALUES (%s, %s, %s,%s,%s,%s,%s)"
      val = (NIM,nama,Fakultas,Prodi,PHONE,Email,Alamat)
      cursor.execute(sql, val)
      conn.commit()
      closeDb()
      return redirect(url_for('index'))
   else:
      return render_template('tambah.html')
  
#fungsi view edit() untuk form edit
@application.route('/edit/<id_mahasiswa>', methods=['GET','POST'])
def edit(id_mahasiswa):
   openDb()
   cursor.execute("SELECT * FROM datamahasiswa WHERE id_mahasiswa=%s", (id_mahasiswa,))
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
      sql = "UPDATE datamahasiswa SET nim=%s,nama_mahasiswa=%s,fakultas=%s,prodi=%s,phone=%s, email=%s, alamat=%s WHERE id_mahasiswa=%s"
      val = (NIM,nama, Fakultas,Prodi,PHONE,Email,Alamat, id_mahasiswa)
      cursor.execute(sql, val)
      conn.commit()
      closeDb()
      return redirect(url_for('index'))
   else:
      closeDb()
      return render_template('edit.html', data=data)
#fungsi untuk menghapus data
@application.route('/hapus/<id_mahasiswa>', methods=['GET','POST'])
def hapus(id_mahasiswa):
   openDb()
   cursor.execute('DELETE FROM datamahasiswa WHERE id_mahasiswa=%s', (id_mahasiswa,))
   conn.commit()
   closeDb()
   return redirect(url_for('index'))
      
if __name__ == '__main__':
   application.run(debug=True)

