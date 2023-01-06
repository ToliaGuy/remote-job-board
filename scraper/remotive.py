import requests

def scrape_remotive():
    print("scraping remotive")
    #return []
    try:
        response = requests.get("https://remotive.com/api/remote-jobs")
        json_data = response.json()
        jobs = []
        for job in json_data["jobs"]:
            # check if data exists
            if job["title"] and job["company_name"] and job["url"] and job["description"]:
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