import json
import os
import re
from os import remove

def carga_datos(i):

    if i== 1:

        f = open("ligas/La_Liga.txt", "a", encoding="utf-8")
        with open("Liga_Española.json", encoding="utf-8") as contenido:
            curso = json.load(contenido)

    elif i== 2:
        f = open("ligas/Premier.txt", "a", encoding="utf-8")
        with open("Liga_Inglesa.json", encoding="utf-8") as contenido:
            curso = json.load(contenido)

    elif i== 3:
        f = open("ligas/Calcio.txt", "a", encoding="utf-8")
        with open("Liga_Italiana.json", encoding="utf-8") as contenido:
            curso = json.load(contenido)

    elif i == 4:
        f = open("ligas/Bundesliga.txt", "a", encoding="utf-8")
        with open("Liga_Alemana.json", encoding="utf-8") as contenido:
            curso = json.load(contenido)

    elif i == 5:
        f = open("ligas/Bundesliga_Aus.txt", "a", encoding="utf-8")
        with open("Liga_Austriaca.json", encoding="utf-8") as contenido:
            curso = json.load(contenido)

    for x in curso.values():

            if type(x) is list:
                    i = 0
                    for e in x:
                        f.write(str(e['name']) + " - " + str(e['code']) + '\n')
                        i += 1

                    f.write("los equipos que participan en esta liga son: " + str(i))
    f.close()


def salida_datos(fichero):

    for equipo in fichero:
        print(equipo)



def uno():
    os.system('cls')
    print('LA LIGA')
    print('-------')
    # carga de datos
    z = 1
    a1 = carga_datos(z)
    # salida de datos
    ligas = open("ligas/La_Liga.txt", "r", encoding="utf-8")
    fichero = ligas.readlines()
    a = salida_datos(fichero)
    ligas.close()
    remove("ligas/La_Liga.txt")




def dos():
    os.system('cls')
    print('PREMIER')
    print('-------')
    b = 2
    a1 = carga_datos(b)
    # salida
    ligas = open("ligas/Premier.txt", "r", encoding="utf-8")
    fichero = ligas.readlines()
    a = salida_datos(fichero)
    ligas.close()
    remove("ligas/Premier.txt")

def tres():
    os.system('cls')
    print('SERIE A')
    print('-------')
    # carga datos
    c = 3
    a2 = carga_datos(c)
    # salida
    ligas = open("ligas/Calcio.txt", "r", encoding="utf-8")
    fichero = ligas.readlines()
    a = salida_datos(fichero)
    ligas.close()
    remove("ligas/Calcio.txt")

def cuatro():
    os.system('cls')
    print('BUNDESLIGA ALEMANA')
    print('------------------')
    # carga
    d = 4
    e = carga_datos(d)
    # salida
    ligas = open("ligas/Bundesliga.txt", "r", encoding="utf-8")
    fichero = ligas.readlines()
    a = salida_datos(fichero)
    ligas.close()
    remove("ligas/Bundesliga.txt")

def cinco():
    os.system('cls')
    print('BUNDESLIGA AUSTRIACA')
    print('------------------')
    # carga
    f = 5
    g = carga_datos(f)
    # salida
    ligas = open("ligas/Bundesliga_Aus.txt", "r", encoding="utf-8")
    fichero = ligas.readlines()
    a = salida_datos(fichero)
    ligas.close()
    remove("ligas/Bundesliga_Aus.txt")




if __name__ == '__main__':

    indice =0


    while True:
        print("""
            1. La Liga (Liga Española)
            2. Premier League (Liga Inglesa)
            3. Serie A (Liga Italiana)
            4. Bundesliga Alemana (Liga Alemana)
            5. Bundesliga Austriaca (Liga Austriaca)
            0. Salir  
            """)

        x =int(input("por favor introduce tu opción----> "))



        os.system('cls')
        patron = '[0-5]'

        while True:
                cadena = input("Por favor introducir la opción deseada >  ")

                correcto = re.fullmatch(patron, cadena)
                if not correcto:
                    print('Error: Vuelva a ingresar la cadena')
                if correcto:
                    indice = cadena
                    break


        if (indice =='1'):
            uno()

        if (indice =='2'):
            dos()
        if (indice == '3'):
            tres()
        if (indice =='4'):
            cuatro()
        if (indice == '5'):
            cinco()
        if (indice =='0'):
            print("Hasta luego....")
            break


    



