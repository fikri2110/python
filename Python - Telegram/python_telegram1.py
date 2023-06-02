import requests

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Notifikasi berhasil terkirim!")
    else:
        print("Gagal mengirim notifikasi.")

# Contoh penggunaan
bot_token = "6144183984:AAG14yiJBkJ6bL-5kjmZvhR8-5UuxTn5j1M"
chat_id = "-896811473"
message = "Halo, Selamat pagi semuanya!"

send_telegram_message(bot_token, chat_id, message)
