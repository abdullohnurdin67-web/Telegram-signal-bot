import requests
from datetime import datetime
import time
import pytz

# --- Konfigurasi ---
TOKEN = '7722424945:AAEyASUSc1nn0jBm--dxdn9lplQrePO3U28'
CHAT_ID = '@sinyalabdulloh'

def kirim_pesan(teks):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': teks, 'parse_mode': 'HTML'}
    requests.post(url, data=payload)

# --- Loop Utama ---
def loop():
    zona = pytz.timezone('Asia/Jakarta')
    sudah_kirim_pagi = False
    sudah_kirim_sore = False

    while True:
        sekarang = datetime.now(zona)
        jam = sekarang.strftime("%H:%M")

        if jam == '07:00' and not sudah_kirim_pagi:
            kirim_pesan("📈 <b>Sinyal Pagi:</b>\nBuy IMX di 0.57\nTarget 0.63\nSL 0.54")
            sudah_kirim_pagi = True
            sudah_kirim_sore = False

        elif jam == '15:00' and not sudah_kirim_sore:
            kirim_pesan("📊 <b>Sinyal Sore:</b>\nPantau RSI IMX, kemungkinan reversal\nCek indikator dan volume!")
            sudah_kirim_sore = True
            sudah_kirim_pagi = False

        time.sleep(60)

if __name__ == "__main__":
    loop()
