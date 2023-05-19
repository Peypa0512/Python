import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#creamos la conexion con la url

url ='https://es.wikipedia.org/wiki/Anexo:Sencillos_n%C3%BAmero_uno_en_Espa%C3%B1a#Canciones_con_m%C3%A1s_semanas_en_el_n%C3%BAmero_uno'
r = requests.get(url)
sopa = BeautifulSoup(r.content, 'html.parser')
ranking = sopa.find("table", class_="sortable wikitable").find('tbody').find_all('tr')


tema =[]
interprete=[]
anio = []
semanas =[]
pais =[]
idioma = ['Español','Español','Inglés','Español','Español','Inglés','Español','Español','Inglés','Inglés',
          'Francés','Español','Portugués','Inglés','Español','Portugués','Español','Alemán','Español',
          'Inglés','Español','Inglés','Español','Sueco']
continente = ['América','América','América','Europa','Europa','América','América','América','América','América',
              'América','América','América','Europa','América','América','Europa','Europa', 'América', 'Europa',
              'América','Europa','Europa','Europa']

cancion = ['Español', 'Español', 'Inglés', 'Español', 'Español', 'Inglés', 'Español','Español','Inglés','Inglés',
           'Francés', 'Español', 'Portugués',  'Inglés', 'Español', 'Portugués', 'Español', 'Inglés',
           'Español', 'Inglés', 'Español', 'Inglés', 'Español', 'Inglés']


i = 1
# vamos rellenado las listas con todos sus valores

tema.append(ranking[1].find_all('td')[0].getText())
tema.append(ranking[2].find_all('td')[0].getText())
tema.append(ranking[3].find_all('td')[0].getText())
tema.append(ranking[4].find_all('td')[0].getText())
tema.append(ranking[5].find_all('td')[0].getText())
tema.append(ranking[6].find_all('td')[0].getText())
tema.append(ranking[7].find_all('td')[0].getText())
tema.append(ranking[8].find_all('td')[0].getText())
tema.append(ranking[9].find_all('td')[0].getText())
tema.append(ranking[10].find_all('td')[0].getText())
tema.append(ranking[11].find_all('td')[0].getText())
tema.append(ranking[12].find_all('td')[0].getText())
tema.append(ranking[13].find_all('td')[0].getText())
tema.append(ranking[14].find_all('td')[0].getText())
tema.append(ranking[15].find_all('td')[0].getText())
tema.append(ranking[16].find_all('td')[0].getText())
tema.append(ranking[17].find_all('td')[0].getText())
tema.append(ranking[18].find_all('td')[0].getText())
tema.append(ranking[19].find_all('td')[0].getText())
tema.append(ranking[20].find_all('td')[0].getText())
tema.append(ranking[21].find_all('td')[0].getText())
tema.append(ranking[22].find_all('td')[0].getText())
tema.append(ranking[23].find_all('td')[0].getText())
tema.append(ranking[24].find_all('td')[0].getText())

interprete.append(ranking[1].find_all('td')[1].getText())
interprete.append(ranking[2].find_all('td')[1].getText())
interprete.append(ranking[3].find_all('td')[1].getText())
interprete.append(ranking[4].find_all('td')[1].getText())
interprete.append(ranking[5].find_all('td')[1].getText())
interprete.append(ranking[6].find_all('td')[1].getText())
interprete.append(ranking[7].find_all('td')[1].getText())
interprete.append(ranking[8].find_all('td')[1].getText())
interprete.append(ranking[9].find_all('td')[1].getText())
interprete.append(ranking[10].find_all('td')[1].getText())
interprete.append(ranking[11].find_all('td')[1].getText())
interprete.append(ranking[12].find_all('td')[1].getText())
interprete.append(ranking[13].find_all('td')[1].getText())
interprete.append(ranking[14].find_all('td')[1].getText())
interprete.append(ranking[15].find_all('td')[1].getText())
interprete.append(ranking[16].find_all('td')[1].getText())
interprete.append(ranking[17].find_all('td')[1].getText())
interprete.append(ranking[18].find_all('td')[1].getText())
interprete.append(ranking[19].find_all('td')[1].getText())
interprete.append(ranking[20].find_all('td')[1].getText())
interprete.append(ranking[21].find_all('td')[1].getText())
interprete.append(ranking[22].find_all('td')[1].getText())
interprete.append(ranking[23].find_all('td')[1].getText())
interprete.append(ranking[24].find_all('td')[1].getText())

anio.append(ranking[1].find_all('td')[2].getText())
anio.append(ranking[2].find_all('td')[2].getText())
anio.append(ranking[3].find_all('td')[2].getText())
anio.append(ranking[4].find_all('td')[2].getText())
anio.append(ranking[5].find_all('td')[2].getText())
anio.append(ranking[6].find_all('td')[2].getText())
anio.append(ranking[7].find_all('td')[2].getText())
anio.append(ranking[8].find_all('td')[2].getText())
anio.append(ranking[9].find_all('td')[2].getText())
anio.append(ranking[10].find_all('td')[2].getText())
anio.append(ranking[11].find_all('td')[2].getText())
anio.append(ranking[12].find_all('td')[2].getText())
anio.append(ranking[13].find_all('td')[2].getText())
anio.append(ranking[14].find_all('td')[2].getText())
anio.append(ranking[15].find_all('td')[2].getText())
anio.append(ranking[16].find_all('td')[2].getText())
anio.append(ranking[17].find_all('td')[2].getText())
anio.append(ranking[18].find_all('td')[2].getText())
anio.append(ranking[19].find_all('td')[2].getText())
anio.append(ranking[20].find_all('td')[2].getText())
anio.append(ranking[21].find_all('td')[2].getText())
anio.append(ranking[22].find_all('td')[2].getText())
anio.append(ranking[23].find_all('td')[2].getText())
anio.append(ranking[24].find_all('td')[2].getText())

semanas.append(ranking[1].find_all('td')[3].getText())
semanas.append(ranking[2].find_all('td')[3].getText())
semanas.append(ranking[3].find_all('td')[3].getText())
semanas.append(ranking[4].find_all('td')[3].getText())
semanas.append(ranking[5].find_all('td')[3].getText())
semanas.append(ranking[6].find_all('td')[3].getText())
semanas.append(ranking[7].find_all('td')[3].getText())
semanas.append(ranking[8].find_all('td')[3].getText())
semanas.append(ranking[9].find_all('td')[3].getText())
semanas.append(ranking[10].find_all('td')[3].getText())
semanas.append(ranking[11].find_all('td')[3].getText())
semanas.append(ranking[12].find_all('td')[3].getText())
semanas.append(ranking[13].find_all('td')[3].getText())
semanas.append(ranking[14].find_all('td')[3].getText())
semanas.append(ranking[15].find_all('td')[3].getText())
semanas.append(ranking[16].find_all('td')[3].getText())
semanas.append(ranking[17].find_all('td')[3].getText())
semanas.append(ranking[18].find_all('td')[3].getText())
semanas.append(ranking[19].find_all('td')[3].getText())
semanas.append(ranking[20].find_all('td')[3].getText())
semanas.append(ranking[21].find_all('td')[3].getText())
semanas.append(ranking[22].find_all('td')[3].getText())
semanas.append(ranking[23].find_all('td')[3].getText())
semanas.append(ranking[24].find_all('td')[3].getText())

pais.append(ranking[1].find_all('td')[4].getText())
pais.append(ranking[2].find_all('td')[4].getText())
pais.append(ranking[3].find_all('td')[4].getText())
pais.append(ranking[4].find_all('td')[4].getText())
pais.append(ranking[5].find_all('td')[4].getText())
pais.append(ranking[6].find_all('td')[4].getText())
pais.append(ranking[7].find_all('td')[4].getText())
pais.append(ranking[8].find_all('td')[4].getText())
pais.append(ranking[9].find_all('td')[4].getText())
pais.append(ranking[10].find_all('td')[4].getText())
pais.append(ranking[11].find_all('td')[4].getText())
pais.append(ranking[12].find_all('td')[4].getText())
pais.append(ranking[13].find_all('td')[4].getText())
pais.append(ranking[14].find_all('td')[4].getText())
pais.append(ranking[15].find_all('td')[4].getText())
pais.append(ranking[16].find_all('td')[4].getText())
pais.append(ranking[17].find_all('td')[4].getText())
pais.append(ranking[18].find_all('td')[4].getText())
pais.append(ranking[19].find_all('td')[4].getText())
pais.append(ranking[20].find_all('td')[4].getText())
pais.append(ranking[21].find_all('td')[4].getText())
pais.append(ranking[22].find_all('td')[4].getText())
pais.append(ranking[23].find_all('td')[4].getText())
pais.append(ranking[24].find_all('td')[4].getText())


df = pd.DataFrame({"tema": tema, "interprete": interprete, "año" : anio, "semanas": semanas, "pais" : pais,
                   "idioma": idioma, "continente": continente, "cancion": cancion })
print(df)
df.to_json("ranking.json")
print("hecho")

