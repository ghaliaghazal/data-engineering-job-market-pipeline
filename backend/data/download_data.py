import requests

url = "https://historical.api.jobtechdev.se/search"

response = requests.get(url, params={"q": "Data Engineer"})

print(response.status_code)

data = response.json()

print(data.keys())