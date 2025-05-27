# WakeupBot Cron Job Backend

Bu loyiha serveringizni doimiy ravishda "ping" qilib, uni faol holatda ushlab turadi. Python yordamida yozilgan va har xil serverlarni (masalan, Render, Heroku va boshqalar) "uyg‘otib" turish uchun ishlatiladi.

## Xususiyatlari

- Serverga vaqti-vaqti bilan HTTP so‘rovi yuboradi
- Xatolik yuz bersa, avtomatik qayta urinish qiladi
- Har bir harakat logga yoziladi (vaqt belgisi bilan)
- Sozlanadigan parametrlar: server manzili, ping oralig‘i, timeout va urinishlar soni

## Foydalanish

1. **Kodni yuklab oling yoki klon qiling:**
    ```sh
    git clone https://github.com/your-username/wakeupbot-cron-job-backend.git
    cd wakeupbot-cron-job-backend
    ```

2. **Talab qilinadigan kutubxonalarni o‘rnating:**
    ```sh
    pip install requests
    ```

3. **`cron_job_backend.py` faylida quyidagi parametrlarni o‘zgartiring:**
    - `SERVER_URL` — o‘z serveringiz manzilini kiriting
    - `MIN_DELAY`, `MAX_DELAY` — pinglar oralig‘ini soniyalarda belgilang
    - `TIMEOUT` — so‘rov uchun maksimal kutish vaqti (sekund)
    - `MAX_RETRIES` — maksimal qayta urinishlar soni

4. **Dasturini ishga tushiring:**
    ```sh
    python cron_job_backend.py
    ```

## Misol

```python
SERVER_URL = "https://your-server-url.com/"
MIN_DELAY = 60
MAX_DELAY = 120
TIMEOUT = 10
MAX_RETRIES = 3
```

## Hissa qo‘shish

Pull requestlar va takliflar uchun xush kelibsiz!

## Litsenziya

MIT