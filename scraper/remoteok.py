import requests

def scrape_remote_ok():
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
