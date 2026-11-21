from dotenv import load_dotenv
import os
load_dotenv()

import uvicorn
from fastapi import HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=["*"]
)

async def hackatime_information():
    ...

@app.get("/get-the-informations")
async def get_the_informations(api_key: str, hackatime_api: str, hackatime_id: str):
    headers = {"Authorization": f"Bearer {hackatime_api}"}
    url = f"https://hackatime.hackclub.com/api/hackatime/v1/users/{hackatime_id}/statusbar/today"

    try:
        hackatime_response = requests.get(url, headers=headers)
        hackatime_response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise HTTPException(e.response.status_code, detail=e.response.text)

    hackatime_json = hackatime_response.json()

    hackatime_seconds = hackatime_json["data"]["grand_total"]["total_seconds"]

    hackatime_hours = hackatime_seconds / 3600
    hackatime_minutes = (hackatime_seconds % 3600) / 60

@app.get("/")
async def health():
    return {"health": "OK"}

if __name__ == "__main__":
    uvicorn.run(app)