import requests
import json


url = "https://historical.api.jobtechdev.se/search"

response = requests.get(url, params={"q": "Data Engineer", "limit": 100, "offset":0})


print(response.status_code)

data = response.json()
with open("backend/data/raw_job_ads.json", "w", encoding="utf-8") as file:
    json.dump(data["hits"], file, ensure_ascii=False, indent=4)
    
print("Total ads:", data["total"]["value"])
print("Returned ads:", len(data["hits"]))

print(data.keys())
print(data["hits"][0].keys())