Seawan Sentinel

**Author:** Jian Setiabudi  
**Branding:** Seawan Sentinel  
![Logo](https://1drv.ms/i/c/b4478bc043d7798b/IQSOufJOlIG7SZI1CFrdvtJbAUUmy5DL_NW_aiMJlxuJxtk)

Seawan Sentinel adalah sistem monitoring server berbasis **Python + Flask** yang terintegrasi dengan **IBM Granite AI** untuk memberikan analisis cerdas terhadap kondisi server.  
Sistem ini memantau **CPU, Memory, Disk, dan Uptime** server secara real-time, kemudian memberikan insight dengan bantuan AI.

---

## ✨ Fitur
- Monitoring server langsung pada host tempat service dideploy  
- Statistik: CPU, Memory, Disk Usage, Uptime  
- Analisis AI otomatis menggunakan [IBM Granite](https://replicate.com/ibm-granite/granite-3.3-8b-instruct)  
- Dashboard web sederhana & mudah digunakan  
- Aman dengan konfigurasi `.env` (API Token tidak ikut di-publish)

---

## Instalasi

1. Clone repository

git clone https://github.com/xbyjeiy/seawan-sentinel.git
cd seawan-sentinel

2. Buat virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Konfigurasi .env

REPLICATE_API_TOKEN=your_ibm_granite_api_token_here

5. Jalankan service
python app.py

Akses di browser:
http://localhost:5000

------------

Contoh Output JSON:

{
  "branding": "Seawan Sentinel",
  "server": "jian",
  "metrics": {
    "cpu": 21.7,
    "memory": 33.2,
    "disk": 36.6,
    "uptime_hours": 109.22
  },
  "ai_analysis": "CPU Usage: 21.7% - server memiliki kapasitas cukup. Memory 33.2% masih rendah, Disk 36.6% cukup aman. Uptime 109 jam menunjukkan server stabil."
}

