# Oled Desk API

This is an api project that gives you information about your daily hackatime time, your timezone's date, time, the last 2 numbers of the year and how much day left until january 1!!

---

# Tech Stack

- Python
- FastAPI
- datetime
- ZoneInfo
- requests
- [tzdata](https://pypi.org/project/tzdata/)
- uvicorn
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

---

# Usage

This api only have 1 endpoint and it called `oled-desk-api.ereninki.hackclub.app/get-the-informations` anb it has 3 required variable, `api_key` `timezone` and `hackatime_api`.

the `hackatime_api` is **your hackatime api key**, its required for getting your daily hackatime time.

the `api_key` is you api key that you set in the .env file, so that only people who has the api key can use your api.

and the last one `timezone` is your timezone, for example **Europe/Istanbul** and thats it!!

# Locally running

if you want to locally run this, you just need to git clone this repo with `git clone https://github.com/Ereninki/Oled-Desk-API` and then you just enter the folder it created and run `uv run main.py` and thats it, you just locally run this api!!
