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
                    # check if data exists
                    if raw_job["title"] and raw_job["companyName"] and raw_job["applicationLink"] and raw_job["description"]:
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
    try:
        url = 'https://remoteok.com/api'
        response = requests.get(url)
        jobs_json = response.json()
        raw_jobs = jobs_json[1:]
        jobs = []
        for job in raw_jobs:
            # check if data exists
            if job["position"] and job["company"] and job["apply_url"] and job["description"]:
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
    #return []
    try:
        response = requests.get("https://remotive.com/api/remote-jobs")
        json_data = response.json()
        jobs = []
        for job in json_data["jobs"]:
            # check if data exists
            if job["title"] and job["company_name"] and job["url"] and job["description"]:
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


def upload_data(jobs, source):
    # upload data all at once to api using requests
    try:
        # delete all jobs from source
        del_res = requests.delete(f"http://djangoapp:8000/api/", json={"source": source})
        for job in jobs:
            response = requests.post("http://djangoapp:8000/api/", json=job)
    except Exception as e:
        print(e)


def run_scraper():
    upload_data(scrape_remote_ok(), "remoteok")
    upload_data(scrape_remotive(), "remotive")
    upload_data(scrape_himalayas(), "himalayas")