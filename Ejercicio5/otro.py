import bs4
import requests
import os

def get_table(url):
    htlm_text= requests.get(url).text
    sopa = bs4.BeautifulSoup(htlm_text, 'html.parser')
    tabla = sopa.find("table").find_all('tr')

    return tabla
url = 'https://es.wikipedia.org/wiki/Anexo:Sencillos_n%C3%BAmero_uno_en_Espa%C3%B1a#Canciones_con_m%C3%A1s_semanas_en_el_n%C3%BAmero_uno'
resultado =get_table(url)

print (resultado)
