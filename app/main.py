from fastapi import FastAPI, File, UploadFile, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

@app.post("/scan")
async def scan_file(file: UploadFile = File(...)):
    try:
        files = {'file': (file.filename, await file.read())}
        params = {'apikey': VIRUSTOTAL_API_KEY}
        response = requests.post("https://www.virustotal.com/vtapi/v2/file/scan", files=files, params=params)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error contacting VirusTotal")

        return response.json()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
