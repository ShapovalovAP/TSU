#на новостном сайте https://www.sport-express.ru/news/ ищем новости по теме Зенит и UFC

import requests
from bs4 import BeautifulSoup
import time
import csv

def get_html(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    return res.text

def avtor_link(url:str):
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, 'html.parser')
    avtor = soup.find_all('div', class_='se-author__content')
    for avtor_novost in avtor:
        text_avtor = avtor_novost.text
        avtor_short = text_avtor.split()
        avtor_short = ' '.join(avtor_short)
    return avtor_short
    

def parser(url:str):
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, 'html.parser')
    news = soup.find_all('div', class_='se-material__title se-material__title--size-middle')


    for novost in news:
        link = novost.findNext().get('href')
        text_novost = novost.text

        if 'Зенит' in text_novost or 'UFC' in text_novost: 
            print (f'{text_novost}')
            print (f'Ссылка:{link}')
            print(f'Автор:{avtor_link(link)}')
            

start_time = time.time()
duration = 1600
interval = 120


while time.time() - start_time < duration:
    parser(url="https://www.sport-express.ru/news/")
    time.sleep(interval)
    
