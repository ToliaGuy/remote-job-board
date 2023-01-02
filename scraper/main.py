import requests
from remoteok import scrape_remote_ok
from remotive import scrape_remotive
from himalayas import scrape_himalayas

def run_scraper():
    upload_jobs(scrape_remote_ok(), "remoteok")
    upload_jobs(scrape_remotive(), "remotive")
    upload_jobs(scrape_himalayas(), "himalayas")

def upload_jobs(jobs, source):
    try:
        if len(jobs) != 0:
            data = {"jobs": jobs, "source": source}
            requests.post("", json=data)
    except Exception as e:
        print(e)
