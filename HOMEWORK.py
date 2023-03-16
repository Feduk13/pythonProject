# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get("https://bank.gov.ua./")
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, features="html.parser")
#     soup_list = soup.find_all("a", {"row": "https://bank.gov.ua/"})
#     res = soup_list[0].find("value")
#     print(res.text)



# class CurrencyConverter:
#     def __init__(self, rate):
#         self.rate = rate
#
#     def convert_currency(self, amount):
#         return float(amount) * float(self.rate)
#
#
# converter = CurrencyConverter(res.text)
# amount = input('Введіть суму в валюті вашої країни: ')
# print(f'Результат конвертації: {converter.convert_currency(amount)} USD')
# class CurrencyConverter:
#     def __init__(self, rate):
#         self.rate = rate
#
#     def convert(self, amount):
#         return amount * self.rate
#
#
# # Driver code
# converter = CurrencyConverter(rate=36.57)
# amount = 1000
#
# amount = input('Введіть суму в валюті вашої країни: ')
# print(f'Результат конвертації: {converter.convert_currency(amount)} USD')
import requests
from bs4 import BeautifulSoup

url = 'https://www.bank.gov.ua/control/uk/curmetal/detail/currency?period=daily'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")
soup_list = soup.find_all("td",{"class_=""usd"})
Usd = soup_list[0].find("class_=""rate").text
print(Usd.text)

#
# class CurrencyConverter:
#     def __init__(self, rate):
#         self.rate = float(rate)
#
#     def convert(self, amount):
#         return amount / self.rate
#
# converter = CurrencyConverter(res.text)
# amount = float(input('Введіть суму в гривнях: '))
# print('Сума в доларах:', converter.convert(amount))