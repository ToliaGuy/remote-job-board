import os
from celery import Celery
from celery.schedules import crontab
from scraper.main import run_scraper

app = Celery(__name__, broker=os.environ['BROKER_URL'])

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls scraper every 6 hours
    sender.add_periodic_task(21600, scrape.s(), name='run scraper')


@app.task
def scrape():
    run_scraper()
    return