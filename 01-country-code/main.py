import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
print("Hello! Please choose select a country by number")
country_name=[]
country_code=[]

def get_input():
  idx = input('# : ')
  try:
    if int(idx)<len(country_code):
      print('You choose '+country_name[int(idx)]+'\nThe current code is '+country_code[int(idx)])
    else:
      print('Choose a number from the list.')
  except:
    print("That wasn't a number.")
  get_input()

def get_string():
  url = "https://www.iban.com/currency-codes"

  indeed_result = requests.get(url)
  indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")
  table_sorter = indeed_soup.find("tbody")
  trs = table_sorter.find_all('tr')
  idx = 0

  for tr in trs:
    country_name.append(tr.select("td")[0].string.capitalize())
    country_code.append(tr.select("td")[2].string)

  for i in country_name:
    print('# {} {}'.format(idx, i))
    idx += 1
  

def init():
  get_string()
  get_input()

init()