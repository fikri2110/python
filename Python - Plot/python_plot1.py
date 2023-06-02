import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt

# Konfigurasi Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

# Mendapatkan data suhu lingkungan dari Google Sheets
sheet = client.open('Data Suhu Lingkungan').sheet1
data = sheet.get_all_records()

# Membuat list tanggal dan suhu dari data
tanggal = []
suhu = []
for row in data:
    tanggal.append(row['Tanggal'])
    suhu.append(row['Suhu'])

# Membuat grafik
plt.plot(tanggal, suhu)
plt.title('Grafik Suhu Lingkungan')
plt.xlabel('Tanggal')
plt.ylabel('Suhu (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
