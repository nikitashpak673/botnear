import requests
import time as t
from bs4 import BeautifulSoup
URL='https://ru.investing.com/crypto/near-protocol'
HEADERS={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36','accept':'*/*'}
def get_html(url,params=None):
    r=requests.get(url,headers=HEADERS,params=params)
    return r
def get_content(html,value):
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find_all('div',class_='top bold inlineblock')
    for item in items:
        a=float(item.find('span', class_='pid-1177211-last', id='last_last').get_text().replace(",","."))
        now_kurs=float(item.find('span', class_='pid-1177211-last', id='last_last').get_text().replace(",","."))
        if(a>=value):
            return a, now_kurs

def parse(value2):
    html=get_html(URL)
    if html.status_code==200:
        return get_content(html.text,value2)
    else:
        print("error")

