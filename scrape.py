import os
from celery import Celery
from celery.schedules import crontab
from scraper.main import run_scraper

app = Celery(__name__, broker=os.environ['BROKER_URL'])

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls matcher every day 
    sender.add_periodic_task(10, scrape.s(), name='run scraper')


@app.task
def scrape():
    return run_scraper()