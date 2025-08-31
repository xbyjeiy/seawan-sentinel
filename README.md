# Seawan Sentinel

**Author:** Jian Setiabudi  
**Branding:** Seawan Sentinel  

![Logo](https://1drv.ms/i/c/b4478bc043d7798b/IQSOufJOlIG7SZI1CFrdvtJbAUUmy5DL_NW_aiMJlxuJxtk)

Seawan Sentinel adalah sistem monitoring server berbasis **Python + FastAPI** dengan **AI Analysis** yang memanfaatkan model [IBM Granite](https://replicate.com/ibm-granite).  
Sistem ini memantau **CPU, Memory, Disk, dan Uptime** server secara real-time, kemudian memberikan analisis otomatis berbasis AI.

---

## ✨ Fitur
- Monitoring server langsung pada host tempat service dideploy
- Statistik: CPU, Memory, Disk Usage, Uptime
- Analisis AI otomatis menggunakan **IBM Granite**
- Dashboard interaktif berbasis **Swagger UI** (langsung tampil di root `/`)
- Aman dengan konfigurasi `.env` (API Token tidak ikut di-publish)

---

## ⚙️ Instalasi

1. Clone repository  
   ```bash
   git clone https://github.com/xbyjeiy/seawan-sentinel.git
   cd seawan-sentinel
````

2. Buat virtual environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Konfigurasi `.env`
   Buat file `.env` di root folder dengan isi:

   ```env
   REPLICATE_API_TOKEN=your_ibm_granite_api_token_here
   ```

5. Jalankan service

   ```bash
   python app.py
   ```

---

## 🌐 Akses Dashboard

Setelah service berjalan, buka di browser:

* Swagger UI (utama):

  ```
  http://127.0.0.1:8000/
  ```

* Endpoint API Monitoring:

  ```
  http://127.0.0.1:8000/monitor
  ```

---

## 📌 Catatan

* Pastikan server memiliki Python ≥ 3.9
* Jika dijalankan sebagai service (systemd/supervisor), gunakan `venv/bin/python` agar environment sesuai.
* API Token **wajib** diisi agar AI Analysis berfungsi.

```
