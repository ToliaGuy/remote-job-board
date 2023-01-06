import requests

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