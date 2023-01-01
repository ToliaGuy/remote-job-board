from remoteok import scrape_remote_ok
from remotive import scrape_remotive

def run_scraper():
    print("running scraper")
    jobs = []
    jobs.extend(scrape_remote_ok())
    jobs.extend(scrape_remotive())
