import sqlite3
import csv
import pandas as pd



def crear_tabla():
    conn = sqlite3.connect("ranking_consulta.db")
    print("Conexión establecida")

    cursor = conn.cursor()
    cursor.execute('CREATE TABLE hits(ID integer ,Tema varchar(50),Interprete varchar(50),'
                   'Año integer,Semanas integer,Pais varchar(50))')
    print('tabla creada')
    cursor.execute('alter table hits add Idioma TEXT(20)')
    print('Columna Insertada')
    cursor.execute('alter table hits add continente TEXT(20)')
    print('Columna Insertada')
    conn.close()

def insertar_datos():
    archivo = archivo_cambio()

    conn = sqlite3.connect("ranking_consulta.db")
    print('conexión establecida')

    cursor = conn.cursor()
    cursor.executemany('INSERT INTO hits values(?, ?, ?, ?, ?, ?,?,?)', archivo)
    print('inserción de datos correcto')
    conn.commit()
    conn.close()
    print("inserción realizada")
    #insertar_columnas()

def archivo_cambio():
    archivo =""
    for n in range(1,3):
        archivo = open(f'{n}.csv', 'r',  encoding="utf8")

    filas = csv.reader(archivo, delimiter=';')
    lista = list(filas)
    del(lista[0])

    #hacemos una tupla
    tupla = tuple(lista)
    return tupla



def consultas(opcion):

    conexion = sqlite3.connect("ranking_consulta.db")
    print('conexión establecida')

    mi_cursor = conexion.cursor()

    match opcion:

        case 1:
            query = "SELECT MIN(año) FROM hits"
        case 2:

            query = "SELECT SUBSTRING_INDEX(interprete,'y'," \
            "1) AS ARTISTA, COUNT(Interprete) AS TOTAL FROM hits group by SUBSTRING_INDEX(Interprete,'y'," \
            "1) order by count(Interprete) DESC LIMIT 1; "

        case 3:
            query = "SELECT pais, COUNT(pais) AS TOTAL FROM hits GROUP BY substring_index(pais,','," \
                "1) ORDER BY COUNT(Pais) DESC LIMIT 1; "

        case 4:
            query =


crear_tabla()
insertar_datos()




'''
idioma = ('Español','Español', 'Inglés', 'Español', 'Español', 'Inglés', 'Español', 'Español','Inglés', 'Inglés',
            'Francés', 'Español', 'Portugués', 'Inglés', 'Español', 'Portugués', 'Español', 'Alemán', 'Español',
            'Inglés', 'Español', 'Inglés', 'Español', 'Sueco')
continente = ('América','América', 'América', 'Europa','Europa', 'América', 'América', 'América', 'América', 'América',
             'América', 'América', 'América', 'Europa', 'América', 'América', 'Europa', 'Europa', 'América', 'Europa',
             'América', 'Europa', 'Europa', 'Europa')


df = pd.DataFrame({"idioma": idioma, "continente": continente})

df.to_csv('tabla2.csv')
'''