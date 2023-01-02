import requests
import psycopg2


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="db", database="postgres", user="postgres", password="postgres")
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        #cur.execute("SELECT * FROM jobs_jobpost")
        #print(cur.fetchall())
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def scrape_himalayas():
    print("scraping himalayas")
    return []
    try:
        jobs = []
        offset = 0
        limit = 200
        while True:
            response = requests.get(f"https://himalayas.app/jobs/api?limit={limit}&offset={offset}")
            json_data = response.json()
            raw_jobs = json_data["jobs"]
            if len(raw_jobs) == 0:
                break
            else:
                for raw_job in raw_jobs:
                    jobs.append({
                        "title": raw_job["title"],
                        "company": raw_job["companyName"],
                        "link": raw_job["applicationLink"],
                        "description": raw_job["description"],
                        "source": "himalayas"
                    })
            offset = offset + limit
        return jobs
    except Exception as e:
        print(e)
    

def scrape_remote_ok():
    print("scraping remote ok")
    return []
    try:
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
    except Exception as e:
        print(e)




def scrape_remotive():
    print("scraping remotive")
    return []
    try:
        response = requests.get("https://remotive.com/api/remote-jobs")
        json_data = response.json()
        jobs = []
        for job in json_data["jobs"]:
            jobs.append({
                "title": job["title"],
                "company": job["company_name"],
                "link": job["url"],
                "description": job["description"],
                "source": "remotive"
            })
        return jobs
    except Exception as e:
        print(e)




def upload_jobs(jobs, source):
    try:
        if len(jobs) != 0:
            data = {"jobs": jobs, "source": source}
            requests.post("djangoapp:8000/jobs/api", json=data)
    except Exception as e:
        print(e)


def run_scraper():
    connect()
    upload_jobs(scrape_remote_ok(), "remoteok")
    upload_jobs(scrape_remotive(), "remotive")
    upload_jobs(scrape_himalayas(), "himalayas")