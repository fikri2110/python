import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Membuat koneksi ke database
mydb = mysql.connector.connect(
    host="localhost",     
    user="username",
    password="password",
    database="nama_database"   # Masukan Database MYSQL 
)

# Membuat objek kursor
cursor = mydb.cursor()

# Eksekusi query
query = "SELECT * FROM nama_tabel"      #Input Table DB
cursor.execute(query)

# Mendapatkan hasil query
result = cursor.fetchall()

# Membuat DataFrame dari hasil query
df = pd.DataFrame(result, columns=[column[0] for column in cursor.description])

# Menampilkan data
print(df)

# Membuat bar plot
plt.bar(df['KolomX'], df['KolomY'])
plt.xlabel('Kolom X')
plt.ylabel('Kolom Y')
plt.title('Grafik Data')
plt.show()

# Menyimpan laporan sebagai file PDF
plt.savefig('laporan.pdf')

# Menutup koneksi ke database
mydb.close()
