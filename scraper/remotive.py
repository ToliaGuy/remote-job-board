import requests


def scrape_remotive():
    response = requests.get("https://remotive.com/api/remote-jobs")
    json_data = response.json()
    jobs = []
    for job in json_data["jobs"]:
        jobs.append({
            "title": job["title"],
            "company": job["company_name"],
            "link": job["url"],
            "description": job["description"],
            "source": "remotive"
        })
    return jobs