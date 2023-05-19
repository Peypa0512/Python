def insertar_datos():
    archivo = archivo_cambio()
    print(archivo)
    print(len(archivo))
    cuenta=0
    for n in range(len(archivo)):
        print(archivo[cuenta])
        cuenta +=1
    conn = sqlite3.connect("ranking_consulta.db")
    cursor = conn.cursor()

    for n in range(len(archivo)):

        cursor.executemany('insert into hits  values (?,?,?,?,?,?)',
                           (archivo[n]))

    conn.commit()
    conn.close()
    print("inserccion realizada")
	

def archivo_cambio():

    archivo = open('ranking.csv', 'r',  encoding="utf8")

    filas = csv.reader(archivo, delimiter=';')
    lista = list(filas)
    #del(lista[0])

    #hacemos una tupla
    tupla = tuple(lista)
    return tupla
