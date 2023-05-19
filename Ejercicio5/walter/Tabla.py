import sqlite3
import csv



def crear_tabla():
    conn = sqlite3.connect("ranking_consulta.db")
    print("Conexion establecida")

    cursor = conn.cursor()
    cursor.execute('CREATE TABLE hits(id,tema,interprete,año,semanas,pais)')
    conn.close()

def insertar_datos():
    archivo = archivo_cambio()
    print(type(archivo))

    cuenta=0
    for n in range(len(archivo)):
        print(archivo[cuenta])
        cuenta +=1

    conn = sqlite3.connect("ranking_consulta.db")
    cursor = conn.cursor()

    #for n in range(len(archivo)):

    cursor.executemany('INSERT INTO hits values(?, ?, ?, ?, ?, ?)', archivo)
    #cursor.execute('Insert into hits values(7,"Waka Waka(Esto es África)","Shakira",2010,17,"Colombia")')
    conn.commit()
    conn.close()
    print("inserccion realizada")

def archivo_cambio():

    archivo = open('ranking.csv', 'r',  encoding="utf8")

    filas = csv.reader(archivo, delimiter=';')
    lista = list(filas)
    del(lista[0])

    #hacemos una tupla
    tupla = tuple(lista)
    return tupla


#archivo_cambio()
insertar_datos()

conn = sqlite3.connect("ranking_consulta.db")
cursor = conn.cursor()
instruccion = "select * from hits;"
cursor.execute(instruccion)
datos = cursor.fetchall()
conn.commit()
conn.close()
print(datos)
print(len(datos))
