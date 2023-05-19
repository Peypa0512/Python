import pandas as pd
from requests import get
import bs4
import re
from datetime import datetime

websitio = "https://es.wikipedia.org/wiki/Anexo:Sencillos_n%C3%BAmero_uno_en_Espa%C3%B1a#Canciones_con_m%C3%A1s_semanas_en_el_n%C3%BAmero_uno"

response = get(websitio)
my_sopa = bs4.BeautifulSoup(response.text, 'html.parser') # lo transformamos en texto

ranking = my_sopa.find_all("table", class_="sortable wikitable") # table, y la clase donde tiene que coger los datos

ranking = str(ranking)


ranking = re.sub(r'<.*?>', lambda g: g.group(0), ranking)

df = pd.read_html(ranking)[0]
df.head()
print(df)
titulo =['Tema', 'Interpretes', 'Año', 'Semanas', 'País']
tema =[]
interprete=[]
anio = []
semanas =[]
pais =[]

