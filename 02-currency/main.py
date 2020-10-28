import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

print("Hello! Please choose select a country by number")

country_url = "https://www.iban.com/currency-codes"
currency_url = "https://transferwise.com/gb/currency-converter/"

country_list = []

def get_input(text):
    print(text)
    idx = input('\n# : ')
    try:
        if int(idx)<len(country_list):
        name = country_list[int(idx)]["name"]
        code = country_list[int(idx)]["code"]
        print(name)
        return code
        else:
        print('Choose a number from the list.')
    except:
        print("That wasn't a number.")

def get_string():
    indeed_result = requests.get(country_url)
    indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")
    table_sorter = indeed_soup.find("tbody")
    trs = table_sorter.find_all('tr')
    idx = 0

    for tr in trs:
        country_name = tr.select("td")[0].string.capitalize()
        country_code = tr.select("td")[2].string
        country_list.append({"name":country_name,"code":country_code})

    for i in country_list:
        print('# {} {}'.format(idx, i["name"]))
        idx += 1


get_string()
a_country = get_input("\nWhere are you from? Choose a country by number.")
b_country = get_input("\nNow choose another country.")

if a_country == b_country:
    print(f"\nYou don't need to convert currency. Both of them use {a_country}")
else:
    print(f"\nHow many {a_country} do you want to convert to {b_country}?")
    amount = input()

    url = f"{currency_url}{a_country.lower()}-to-{b_country.lower()}-rate?amount={amount}"
    indeed_result = requests.get(url)
    indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")
    currency = indeed_soup.find("span",{"class":"text-success"})
    value = float(currency.text)*float(amount)

    amount_from = format_currency(amount, "KRW", locale="ko_KR")
    amount_to = format_currency(value, "USD", locale="ko_KR")
    print(f"\n{amount_from} is {amount_to}")
