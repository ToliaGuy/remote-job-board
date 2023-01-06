import requests
from . import remotive, remoteok, himalayas


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
    upload_data(remoteok.scrape_remote_ok(), "remoteok")
    upload_data(remotive.scrape_remotive(), "remotive")
    upload_data(himalayas.scrape_himalayas(), "himalayas")