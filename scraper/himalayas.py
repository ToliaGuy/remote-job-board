import requests


def scrape_himalayas():
    try:
        jobs = []
        offset = 0
        limit = 200
        while True:
            response = requests.get(f"https://himalayas.app/jobs/api?limit={limit}&offset={offset}")
            json_data = response.json()
            raw_jobs = json_data["jobs"]
            if len(raw_jobs) == 0:
                break
            else:
                for raw_job in raw_jobs:
                    jobs.append({
                        "title": raw_job["title"],
                        "company": raw_job["companyName"],
                        "link": raw_job["applicationLink"],
                        "description": raw_job["description"],
                        "source": "himalayas"
                    })
            offset = offset + limit
        return jobs
    except Exception as e:
        print(e)
    