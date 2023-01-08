# Remote Job Board
## Intro
Remote work is becoming more and more common way of working, so I decided to create my own job board for remote workers. 

## How this project works?
This projects uses [Celery beat scheduler](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html) and [Celery worker](https://docs.celeryq.dev/en/stable/userguide/workers.html) to pull data from public remote job board APIs ([RemoteOk](https://remoteok.com/), [Remotive](https://remotive.com/), [Himalayas](https://himalayas.app/)) every 6 hours, updates the data in the database and displays all the data with [Django](https://www.djangoproject.com/).

## Built With
* [Docker](https://docs.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Celery](https://docs.celeryq.dev/en/stable/)
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Bootstrap](https://getbootstrap.com/)

## Roadmap
- [x] Pull data from APIs
- [x] Create a Django app
- [x] Create a basic UI
- [x] Dockerize everything
- [] Create an AUTH system for API
- [] Find a better way for updating the data
- [] Add more info e.g. salary range, experience level, job type
