import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def extract_job(html):
    try:
        title = html.find("h2").text
        company = html.find("h3").text
        apply_link = html.find("a").attrs['href']
        return {'title': title, 'company': company,
                'apply_link': f"https://remoteok.io/{apply_link}"
                }
    except:
        pass


def extract_jobs(url):
    jobs = []
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, "html.parser")
    td_lists = soup.find_all("td", {"class": "company_and_position_mobile"})

    for result in td_lists:
        job = extract_job(result)
        jobs.append(job)

    return jobs


def get_jobs_ro(word):
    url = f"https://remoteok.io/remote-{word}-jobs"
    jobs = extract_jobs(url)

    return jobs
