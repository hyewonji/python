import requests
from bs4 import BeautifulSoup


def extract_job(html):
    title = html.find("span", {"class": "title"}).text
    company = html.find("span", {"class": "company"}).text
    link = html.find_all("a")[-1].attrs['href']
    # recursive=False : span안에 있는 span까지 가져오는것을 방지
    return {'title': title, 'company': company,
            'apply_link': f"https://weworkremotely.com/{link}"
            }


def extract_jobs_wwr(url):
    jobs = []
    result_wwr = requests.get(url)
    soup_wwr = BeautifulSoup(result_wwr.text, "html.parser")
    sections = soup_wwr.find_all("section", {"class": "jobs"})

    results = []
    for section in sections:
        lists = section.find_all("li")[:-1]
        for list in lists:
            results.append(list)

    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs


def get_jobs_wwr(word):
    url_wwr = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs_wwr = extract_jobs_wwr(url_wwr)

    return jobs_wwr
