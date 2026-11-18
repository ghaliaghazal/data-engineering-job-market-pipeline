import requests

url = "https://historical.api.jobtechdev.se/search"

response = requests.get(url, params={"q": "Data Engineer", "limit": 100})

print(response.status_code)

data = response.json()
print("Total ads:", data["total"]["value"])
print("Returned ads:", len(data["hits"]))

print(data.keys())
print(data["hits"][0].keys())