from remoteok import scrape_remote_ok

def run_scraper():
    print("running scraper")
    jobs = []
    jobs.extend(scrape_remote_ok())
