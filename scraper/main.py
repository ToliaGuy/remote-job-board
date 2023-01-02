import requests

def scrape_himalayas():
    print("scraping himalayas")
    return []
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
    

def scrape_remote_ok():
    print("scraping remote ok")
    return []
    try:
        url = 'https://remoteok.com/api'
        response = requests.get(url)
        jobs_json = response.json()
        raw_jobs = jobs_json[1:]
        jobs = []
        for job in raw_jobs:
            jobs.append({
                'title': job['position'],
                'company': job['company'],
                'link': job['apply_url'],
                'description': job['description'],
                'source': 'remoteok'
            })
        return jobs
    except Exception as e:
        print(e)




def scrape_remotive():
    print("scraping remotive")
    return []
    try:
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
    except Exception as e:
        print(e)




def upload_jobs(jobs, source):
    try:
        if len(jobs) != 0:
            data = {"jobs": jobs, "source": source}
            requests.post("", json=data)
    except Exception as e:
        print(e)


def run_scraper():
    upload_jobs(scrape_remote_ok(), "remoteok")
    upload_jobs(scrape_remotive(), "remotive")
    upload_jobs(scrape_himalayas(), "himalayas")