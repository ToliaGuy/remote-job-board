from remoteok import scrape_remote_ok
from remotive import scrape_remotive
from himalayas import scrape_himalayas

def run_scraper():
    jobs = []
    jobs.extend(scrape_remote_ok())
    jobs.extend(scrape_remotive())
    jobs.extend(scrape_himalayas())
    return jobs

def upload_jobs(jobs):
    for job in jobs:
        #TODO: Upload job to database
        print(job)
    return
