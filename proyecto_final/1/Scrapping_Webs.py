import requests
from bs4 import BeautifulSoup


web = requests.get('https://tienda.consum.es/es/s/+busqueda.replace("", "%20")')

status_code = web.status_code
if status_code == 200:
    print(status_code)

soup = BeautifulSoup(web.text, 'lxml')

tags = soup.find_all('div')


productos = list()
precios = list()
#for tag in tags:


