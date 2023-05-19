import bs4
import requests as requests
import pandas as pd
from selenium import webdriver
import requests
import sys
#sys.path.insert(0,'/usr/lib/chromium-brower/chromedriver')


url ='https://es.wikipedia.org/wiki/Anexo:Sencillos_n%C3%BAmero_uno_en_Espa%C3%B1a#Canciones_con_m%C3%A1s_semanas_en_el_n%C3%BAmero_uno'
headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
respuesta = requests.get(url, headers=headers)

all_tables = pd.read_html(respuesta.content, encoding = 'utf8')

matched_tabla = pd.read_html(respuesta.text, match= 'class = "sortable wikitable jquery-tablesorter"')

print(f'total tabla encontrada: {len(matched_tabla)}')


