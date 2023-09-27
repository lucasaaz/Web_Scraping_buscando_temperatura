import requests
from bs4 import BeautifulSoup

link = 'https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/107/belohorizonte-mg'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=headers)

site = BeautifulSoup(requisicao.text, 'html.parser')

temp_min = site.find("span", class_='_margin-r-15')
temperatura = site.find("div", class_='-gray _flex _margin-l-5').get_text().strip().split()

print(f'\n BELO HORIZONTE\n')
print(f' Temperatura mínima: {temperatura[0]} \n Temperatura máxima: {temperatura[1]}\n')