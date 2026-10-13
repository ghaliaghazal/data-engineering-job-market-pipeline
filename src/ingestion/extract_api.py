
import requests

API_URL = "https://jobsearch.api.jobtechdev.se/search"


def extract_job_ads(query="Data Engineer", limit=5):
    params = {
        "q": query,
        "limit": limit,
    }

    response = requests.get(
        API_URL,
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    data = extract_job_ads()

    print("Total jobs found:", data["total"]["value"])
    print("Jobs returned:", len(data["hits"]))
