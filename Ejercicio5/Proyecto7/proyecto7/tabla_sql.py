import mysql.connector
import csv
from os import system
import msvcrt


def conectar():
    # hacemos conexion con MariaDB

    conn = mysql.connector.connect(host="localhost", port=3306, user='root', password='')
    cursor = conn.cursor()

    # creamos la base de datos

    cursor.execute("DROP DATABASE IF EXISTS Ranking")
    cursor.execute("CREATE DATABASE Ranking")
    print('Se creo correctamente la base de datos')

    cursor.execute('USE Ranking')

    cursor.execute("CREATE TABLE Hits("
                   "ID INT(2),"
                   "Tema VARCHAR(50),"
                   "Interprete VARCHAR(60),"
                   "Año INT(10),"
                   "Semanas INT(3),"
                   "Pais VARCHAR(30))")

    print('Se ha creado la tabla HITS')
    # insertar columnas
    insertar_columna =  "alter table hits add(Idioma varchar(20))"
    insertar_columna1 = "alter table hits add(Continente varchar(20))"
    insertar_columna2 = "alter table hits add(Cancion varchar(20))"

    cursor.execute(insertar_columna)
    cursor.execute(insertar_columna1)
    cursor.execute(insertar_columna2)

    # ejecutmamos commit para confirmar y cerramos la base de datos
    conn.commit()
    conn.close()


def insertar_datos(archivo):
    archivo_datos = archivo
    print('llega fichero')
    mydb = mysql.connector.connect(host="localhost", port=3306, user='root', password='', database='ranking')

    mycursor = mydb.cursor()
    print('llega fichero')
    mycursor.executemany('INSERT INTO hits VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)', archivo_datos)

    mydb.commit()
    mydb.close()


# abrimos fichero csv y lo preparamos para la carga de datos
def archivo_cambio():
    # archivo = open(ruta, 'r',  encoding="utf8")
    archivo = ""

    archivo = open('fichero_carga.csv', 'r', encoding="utf8")

    filas = csv.reader(archivo, delimiter=';')
    lista = list(filas)
    del (lista[0])
    print(lista)

    # hacemos una tupla
    tupla = tuple(lista)

    insertar_datos(tupla)


# hacer consultas:
def consultas():
    query = ''
    # conectamos con la base de datos
    conn = mysql.connector.connect(host="localhost", port=3306, user='root', password='', database='ranking')
    cursor = conn.cursor()
    consulta = 0
    salir = False
    dato = ''
    while not salir:

        print(' Por favor, elige una de estas opciones')
        print('''
                    1.- ¿Cuál es la canción más antigua de la lista?
                    2.- ¿Qué artista aparece más veces en esta lista?
                    3.- ¿Qué país tiene más artistas en esta lista?
                    4.- ¿Cuantas canciones distintas hay por cada idioma?
                    5.- ¿Cuál es el continente con más apariciones en la lista?
                    6.- ¿Qué canción ha estado más % de tiempo al año como número 1?
                    7.- Volver al Menú Principal
            
        ''')
        try:
            consulta = int(input("Elige por favor, una de estas opciones...> "))
        except:
            print("Por favor elige una opción correcta......")



        # realizamos la query



        if consulta == 1:
            query = "SELECT tema, año FROM hits ORDER BY año ASC LIMIT 1;"
            cursor.execute(query)
            dato = cursor.fetchall()
            for linea in dato:
                print(f' El tema más antiguo es {linea[0]}, que es el del año {linea[1]}')

        elif consulta == 2:
            query = "SELECT SUBSTR(interprete,1,16), COUNT(Interprete) FROM hits " \
                    "group by SUBSTR(Interprete,1,16) order by count(Interprete) DESC LIMIT 1;"
            cursor.execute(query)
            dato = cursor.fetchall()
            for linea in dato:
                print(f'El artísta que más veces aparece es {linea[0]}, con {linea[1]} apariciones')
        elif consulta == 3:
            query = "SELECT pais, COUNT(pais) AS TOTAL FROM hits GROUP BY substring_index(pais,','," \
                    "1) ORDER BY COUNT(Pais) DESC LIMIT 1; "

            cursor.execute(query)
            dato = cursor.fetchall()
            for linea in dato:
                print(f'El país con más artistas que aparece en la lista es {linea[0]}, con {linea[1]} artistas')

        # hay que tener en cuenta que hay canciones que no se cantan en el mismo idioma que el pais del artista
        elif consulta == 4:
            query = 'select cancion, count(cancion) from hits group by cancion order by cancion;'
            cursor.execute(query)
            dato = cursor.fetchall()
            for linea in dato:
                print(f'Las canciones con el idioma {linea[0]}, tiene {linea[1]} cancion/es')

        elif consulta == 5:
            query = "SELECT continente, COUNT(continente) AS TOTAL FROM hits GROUP BY continente LIMIT 1;"
            cursor.execute(query)
            dato = cursor.fetchall()
            for linea in dato:
                print(f'El continente con más apariciones en la lista es {linea[0]} con {linea[1]} canciones')
        elif consulta == 6:
            query = "SELECT tema, CONCAT(ROUND((semanas / 52 * 100), 2), '%') FROM hits GROUP BY semanas " \
                    "ORDER BY semanas DESC LIMIT 1;"
            cursor.execute(query)
            dato = cursor.fetchall()
            for linea in dato:
                print(f'La canción con mayor porcentaje es {linea[0]} con un {linea[1]}')

        elif consulta == 7:
            print('Volvemos al Menú Principal')

            print("Presione una tecla para continuar...")
            msvcrt.getch()
            salir = True


        print("Presione una tecla para continuar...")
        msvcrt.getch()



    conn.close()



# vamos a hacer el menú para arrancar el programa

opcion = False

while not opcion:
    system('cls')
    caso = 0
    print("CONSULTAS SOBRE UNA BASE DE DATOS")
    print('1.- Hacer una base de datos')
    print('2.- Insertar datos en una tabla')
    print('3.- Hacer alguna consulta sobre la tabla')
    print('4.- Salir')
    try:
        caso = int(input('Introduce por favor una opción: '))
    except:
        print(" Por favor intenta introducir una opción correcta")
        system('cls')

    match caso:
        case 1:
            print('menu1')
            conectar()
            print("Presione una tecla para continuar...")
            msvcrt.getch()
        case 2:
            print('menu2')
            archivo_cambio()
            print("Presione una tecla para continuar...")
            msvcrt.getch()
        case 3:
            system('cls')
            print('menu3')
            consultas()
            print("Presione una tecla para continuar...")
            msvcrt.getch()
        case 4:
            print(' Hasta luego')
            opcion = True
