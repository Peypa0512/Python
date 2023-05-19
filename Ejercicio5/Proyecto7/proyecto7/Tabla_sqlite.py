import sqlite3
import csv
from os import system
import msvcrt



def crear_tabla():
    conn = sqlite3.connect("ranking_consulta.db")
    print("Conexión establecida")

    cursor = conn.cursor()



    cursor.execute('CREATE TABLE hits(ID integer ,Tema varchar(50),Interprete varchar(50),'
                   'Año integer,Semanas real,Pais varchar(50))')
    print('tabla creada')
    cursor.execute('alter table hits add Idioma TEXT(20)')
    print('Columna Insertada')
    cursor.execute('alter table hits add continente TEXT(20)')
    print('Columna Insertada')
    cursor.execute("alter table hits add Cancion varchar(20)")
    print('Columna Insertada')
    conn.close()

    print("Presione una tecla para continuar...")
    msvcrt.getch()

def insertar_datos():
    archivo = archivo_cambio()

    conn = sqlite3.connect("ranking_consulta.db")
    print('conexión establecida')

    cursor = conn.cursor()
    cursor.executemany('INSERT INTO hits values(?, ?, ?, ?, ?, ?,?,?,?)', archivo)
    print('inserción de datos correcto')
    conn.commit()
    conn.close()
    print("inserción realizada")
    #insertar_columnas()

def archivo_cambio():

    archivo = open('fichero_carga.csv', 'r', encoding="utf8")
    print('registros insertados')

    filas = csv.reader(archivo, delimiter=';')
    lista = list(filas)


    #hacemos una tupla
    tupla = tuple(lista)
    return tupla


def consultas():
    query = ''
    # conectamos con la base de datos
    conn = sqlite3.connect("ranking_consulta.db")
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
            query = "SELECT SUBSTRING_INDEX(interprete,'y'," \
                    "1) AS ARTISTA, COUNT(Interprete) AS TOTAL FROM hits group by SUBSTRING_INDEX(Interprete,'y'," \
                    "1) order by count(Interprete) DESC LIMIT 1; "
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
            query = "SELECT tema, ROUND((semanas / 52 * 100), 2) FROM hits GROUP BY semanas " \
                    "ORDER BY semanas DESC LIMIT 1;"
            cursor.execute(query)
            dato = cursor.fetchall()
            for linea in dato:
                print(f'La canción con mayor porcentaje es {linea[0]} con un {linea[1]} %')

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
            crear_tabla()

        case 2:
            print('menu2')
            insertar_datos()
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







