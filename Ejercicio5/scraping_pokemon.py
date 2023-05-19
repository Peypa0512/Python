import requests
from bs4 import BeautifulSoup
import pandas as pd

url ='https://pokemondb.net/pokedex/all'
r = requests.get(url)
sopa = BeautifulSoup(r.content, 'html.parser')

# para encontrar la tabla utilizaremos find() ---> utilizamos find para encontrar la tabla
#despues de encontrar el tbody hay muchos tr y hay que usar el metodo find_all(tr) y encuentra todas las filas
rows = sopa.find('table',attrs={"id":"pokedex"}).find('tbody').find_all('tr')

# nos va a mostrar todos los elementos de la tabla y vamos a buscar el nombre del primer elemento
nombre = rows[0].find_all('td')[1].getText()
print(nombre)


#vamos a recorrer la lista y vemos el primer elemento
nombres = []
total = []
hp = []
attack = []
defense = []
sp_atack = []
sp_defense = []
speed = []
for row in rows:
    nombres.append(row.find_all('td')[1].getText())
    total.append(row.find_all('td')[3].getText())
    hp.append(row.find_all('td')[4].getText())
    attack.append(row.find_all('td')[5].getText())
    defense.append(row.find_all('td')[6].getText())
    sp_atack.append(row.find_all('td')[7].getText())
    sp_defense.append(row.find_all('td')[8].getText())
    speed.append(row.find_all('td')[9].getText())




# hacemos un data frame, en el cual es un diccionario en el que tiene el key que va ser el nombre y los valores el resto

df = pd.DataFrame({'nombres': nombres, 'total' : total, 'hp': hp, 'attack': attack, 'defense': defense,
                   'sp_atack' : sp_atack, 'sp_defense' : sp_defense, 'speed' : speed})
print(df)

#vamos a exportarlo a un csv

df.to_csv('pokemon.csv')