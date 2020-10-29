import os
import csv
import requests
from bs4 import BeautifulSoup


os.system("clear")

alba_url = "http://www.alba.co.kr"

def save_to_file(company,jobs):
  file = open(f"{company}.csv",mode="w")
  writer = csv.writer(file)
  writer.writerow(["근무지","지점","포지션","근무시간","급여"])

  for job in jobs:
    writer.writerow(list((job.values())))
  return


def extract_job(text, link):
  jobs = []

  result = requests.get(link)
  soup = BeautifulSoup(result.text,"html.parser")

  locations = soup.find_all("td",{"class":"local"})
  companies = soup.find_all("span",{"class":"company"})
  titles = soup.find_all("span",{"class":"title"})
  times = soup.find_all("td",{"class":"data"})
  pays = soup.find_all("td",{"class":"pay"})
  for i in range(len(locations)):
    row = {
      '근무지' : locations[i].text,
      '지점' : companies[i].text,
      '포지션' : titles[i].text,
      '근무시간' : times[i].text,
      '급여' : pays[i].text
    }
    jobs.append(row)
  save_to_file(text,jobs)


def get_company_name():
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text,"html.parser")
  companies = soup.find("div",{"id":"MainSuperBrand"}).find_all("a",{"class":"goodsBox-info"})

  for company in companies:
    text = company.find("span",{"class":"company"}).text
    link = company["href"]
    print(text)
    extract_job(text,link)

get_company_name()