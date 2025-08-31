import os, time, platform, psutil, replicate
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn

# Branding
APP_NAME = "Seawan Sentinel"
AUTHOR = "Jian Setiabudi"
LOGO_URL = "https://1drv.ms/i/c/b4478bc043d7798b/IQSOufJOlIG7SZI1CFrdvtJbAUUmy5DL_NW_aiMJlxuJxtk"

# Load token
load_dotenv()
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

# FastAPI config Swagger UI langsung di root
app = FastAPI(
    title=APP_NAME,
    description=f"""
<img src="{LOGO_URL}" width="150"/><br>
**{APP_NAME}** - AI-Powered Server Monitoring<br>
Author: {AUTHOR}
""",
    version="1.0.0",
    docs_url="/",    # Swagger langsung di root
    redoc_url=None   # ReDoc dimatikan
)

def get_server_status():
    return {
        "server": platform.node(),
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "uptime_hours": round((time.time() - psutil.boot_time()) / 3600, 2)
    }

def analyze_server(data):
    prompt = f"""
    Laporan server:
    - CPU: {data['cpu']}%
    - Memory: {data['memory']}%
    - Disk: {data['disk']}%
    - Uptime: {data['uptime_hours']} jam

    Tolong analisa kondisi server ini, sebutkan potensi masalah, dan berikan rekomendasi singkat.
    """
    output = replicate.run(
        "ibm-granite/granite-3.3-8b-instruct",
        input={
            "prompt": prompt,
            "max_tokens": 256,
            "temperature": 0.6,
            "top_p": 0.9
        }
    )
    return "".join(output)

@app.get("/monitor")
def monitor():
    data = get_server_status()
    analysis = analyze_server(data)
    return {
        "branding": APP_NAME,
        "server": data["server"],
        "metrics": data,
        "ai_analysis": analysis
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

