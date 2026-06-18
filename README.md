# 🛡️ Seawan Sentinel

**Author:** Jian Setiabudi  
**Brand:** Seawan Sentinel

![Seawan Sentinel Logo](https://1drv.ms/i/c/b4478bc043d7798b/IQSOufJOlIG7SZI1CFrdJbAUUmy5DL_NW_aiMJlxuJxtk)

## Overview

**Seawan Sentinel** is an AI-powered server monitoring platform built with **Python** and **FastAPI**. It provides real-time system monitoring and automated infrastructure analysis using the **IBM Granite AI Model** through Replicate.

The platform continuously monitors server health metrics such as CPU, memory, disk usage, and uptime, then generates intelligent operational insights to assist system administrators, DevOps engineers, and security teams.

---

## ✨ Features

- 📊 Real-time server monitoring
- 🖥️ CPU utilization monitoring
- 💾 Memory usage monitoring
- 📁 Disk usage monitoring
- ⏱️ System uptime tracking
- 🤖 AI-powered infrastructure analysis using IBM Granite
- 📖 Interactive API documentation with Swagger UI
- 🔒 Secure configuration using environment variables
- ⚡ Lightweight FastAPI-based architecture

---

## 🏗️ Technology Stack

- Python 3.9+
- FastAPI
- Psutil
- Replicate API
- IBM Granite AI Model
- Uvicorn

---

## 📦 Installation

### 1. Clone Repository

```bash
git clone https://github.com/xbyjeiy/seawan-sentinel.git
cd seawan-sentinel
```

### 2. Create Virtual Environment

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
REPLICATE_API_TOKEN=your_replicate_api_token
```

> Obtain your API token from Replicate and ensure it has access to the IBM Granite model.

### 5. Run the Application

```bash
python app.py
```

Or using Uvicorn:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

## 🌐 API Endpoints

### Swagger UI

Interactive API documentation:

```text
http://127.0.0.1:8000/
```

### Monitoring Endpoint

Retrieve server metrics and AI analysis:

```text
GET /monitor
```

Example:

```text
http://127.0.0.1:8000/monitor
```

---

## 📊 Sample Response

```json
{
  "cpu_percent": 12.4,
  "memory_percent": 45.8,
  "disk_percent": 63.1,
  "uptime_hours": 125.6,
  "ai_analysis": "System resources are operating within normal thresholds. No immediate action is required."
}
```

---

## 🔐 Security

For security reasons:

- Never commit `.env` files to source control.
- Store API tokens securely.
- Add `.env` to `.gitignore`.
- Restrict access to monitoring endpoints when deployed publicly.

Example `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

## 🚀 Deployment

The application can be deployed using:

- Systemd
- Supervisor
- Docker
- Kubernetes
- Nginx Reverse Proxy

Recommended production command:

```bash
uvicorn app:app \
    --host 0.0.0.0 \
    --port 8000 \
    --workers 2
```

---

## 📌 Requirements

- Python 3.9 or newer
- Internet access for AI analysis
- Valid Replicate API Token
- Linux, macOS, or Windows environment

---

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

---

## 📄 License

This project is maintained by **Seawan Sentinel**.

Copyright © 2026 Jian Setiabudi.
