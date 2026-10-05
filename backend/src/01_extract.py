import requests

url = "https://jobsearch.api.jobtechdev.se/search"

params = {
    "q": "Data Engineer",
    "limit": 10
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())
