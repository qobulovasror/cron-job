import requests
import time
import random
from datetime import datetime

# Sozlanadigan parametrlar
SERVER_URL = "your_server_url_here"  # Server URL manzili
MIN_DELAY = 30  # soniya
MAX_DELAY = 40  # soniya
TIMEOUT = 10    # sekund
MAX_RETRIES = 3 # maksimal qayta urinishlar

def log(message):
    """Log xabarini vaqt belgisi bilan chiqaradi."""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def ping_server():
    """Serverga ping yuboradi va javobni qaytaradi."""
    try:
        response = requests.get(SERVER_URL, timeout=TIMEOUT)
        log(f"Serverga ping yuborildi - Status: {response.status_code}")
        log(f"Javob: {response.text[:100]}...")  # Javob uzun bo‘lsa qisqartiriladi
        return True
    except requests.exceptions.RequestException as e:
        log(f"Xatolik: {e}")
        return False

def keep_alive():
    """Serverni doimiy ping qilib turadi."""
    while True:
        success = False
        for attempt in range(1, MAX_RETRIES + 1):
            log(f"{attempt}-urinishda ping yuborilmoqda...")
            if ping_server():
                success = True
                break
            else:
                log("Qayta urinishdan oldin 5 soniya kutiladi...")
                time.sleep(5)
        if not success:
            log("Serverga ulanish muvaffaqiyatsiz tugadi. Keyingi urinish kutilyapti.")

        delay = random.randint(MIN_DELAY, MAX_DELAY)
        log(f"Keyingi ping {delay} soniyadan so‘ng...")
        time.sleep(delay)

if __name__ == "__main__":
    keep_alive()