from dotenv import load_dotenv
import os
load_dotenv()

import uvicorn
from fastapi import HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

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
async def get_the_informations(api_key: str, hackatime_api: str, timezone: str):
    if api_key != os.getenv("API_KEY"):
        raise HTTPException(403, detail="sorry but your api key isnt matching,, pls check it again")
    try:
        timezone_now = ZoneInfo(timezone)
    except ZoneInfoNotFoundError:
        raise HTTPException(400, detail="sorry but your timezone you inserted isnt right..... pls check it again!")

    headers = {"Authorization": f"Bearer {hackatime_api}"}
    url = f"https://hackatime.hackclub.com/api/hackatime/v1/users/0/statusbar/today"

    try:
        hackatime_response = requests.get(url, headers=headers)
        hackatime_response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise HTTPException(e.response.status_code, detail=e.response.text)

    hackatime_json = hackatime_response.json()

    hackatime_seconds = hackatime_json["data"]["grand_total"]["total_seconds"]

    hackatime_hours = str(int(hackatime_seconds / 3600))
    hackatime_minutes = str(int(int((hackatime_seconds % 3600)) / 60))

    now = datetime.now(timezone_now)
    day_of_the_year = now.timetuple().tm_yday
    hour = str(now.hour)
    minute = str(now.minute)
    day = str(now.day)
    year = str(now.year)[2:4]
    month = str(now.month)

    return {"hackatime hours": hackatime_hours, "hackatime minutes": hackatime_minutes, "hour": hour, "minute": minute, "year": year, "month": month, "day": day, "until january": str(365 - day_of_the_year)}

@app.get("/")
async def health():
    return {"health": "OK"}

if __name__ == "__main__":
    uvicorn.run(app)