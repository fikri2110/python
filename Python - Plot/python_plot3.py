import requests
import matplotlib.pyplot as plt
import datetime

# API key OpenWeatherMap
api_key = 'bd5e378503939ddaee76f12ad7a97608'

# Mengirim permintaan ke API OpenWeatherMap untuk mendapatkan data suhu
city = 'BANDUNG'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
response = requests.get(url)
data = response.json()

# Menyimpan data suhu dan jam dalam list
temperatures = []
hours = []
for entry in data['list']:
    temperature = entry['main']['temp']
    timestamp = entry['dt']
    date_time = datetime.datetime.fromtimestamp(timestamp)
    hour = date_time.strftime("%H:%M")
    temperatures.append(temperature)
    hours.append(hour)

# Membuat grafik
plt.plot(hours, temperatures)
plt.title('Grafik Suhu di kota serang')
plt.xlabel('Jam')
plt.ylabel('Suhu (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
