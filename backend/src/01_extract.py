import requests
import json

url = "https://jobsearch.api.jobtechdev.se/search"

params = {
    "q": "Data Engineer",
    "limit": 10
}

response = requests.get(url, params=params)

print(response.status_code)

data = response.json()

with open("backend/data/raw_job_ads.json", "w", encoding="utf-8") as file:  # Skapar/öppnar filen för att spara data
    json.dump(data, file, ensure_ascii=False, indent=2)      # Sparar data som JSON