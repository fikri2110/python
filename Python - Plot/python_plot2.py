import requests
import matplotlib.pyplot as plt

# API key OpenWeatherMap
api_key = 'bd5e378503939ddaee76f12ad7a97608'

# Mengirim permintaan ke API OpenWeatherMap untuk mendapatkan data suhu
city = 'Jakarta'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
response = requests.get(url)
data = response.json()

# Menyimpan data suhu dan tanggal dalam list
temperatures = []
dates = []
for entry in data['list']:
    temperatures.append(entry['main']['temp'])
    dates.append(entry['dt_txt'])

# Membuat grafik
plt.plot(dates, temperatures)
plt.title('Grafik Suhu Lingkungan di Jakarta')
plt.xlabel('Tanggal')
plt.ylabel('Suhu (°C)')
plt.xticks(rotation=50)
plt.grid(True)
plt.show()
