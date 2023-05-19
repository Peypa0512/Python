import mysql.connector


def conectar():
    #hacemos conexion con MariaDB

    conn = mysql.connector.connect(host="localhost", port= 3306, user = 'root', password= '', database= 'ranking')

    cursor = conn.cursor()

    # insertar columnas
    insertar_columna = "alter table hits add(idioma varchar(20))"
    insertar_columna1 = "alter table hits add(continente varchar(20))"
    cursor.execute(insertar_columna)
    cursor.execute(insertar_columna1)


    # ejecutmamos commit para confirmar y cerramos la base de datos
    conn.commit()
    conn.close()


def insertar_columna():
    mydb = mysql.connector.connect(host="localhost", port=3306, user='root', password='', database='ranking')

    mycursor = mydb.cursor()

    # insertamos datos en columna

    idioma = ['Español', 'Español', 'Inglés', 'Español', 'Español', 'Inglés', 'Español', 'Español', 'Inglés',
              'Inglés', 'Inglés', 'Francés', 'Español', 'Portugues', 'Inglés', 'Español', 'Portugues',
              'Español', 'Alemán', 'Español', 'Inglés', 'Español', 'Inglés', 'Español', 'Sueco']



    continente = ['América', 'América', 'América', 'Europa', 'Europa', 'América', 'América', 'América', 'América',
                  'América',
                  'Europa', 'América', 'América', 'Europa', 'América', 'América', 'Europa', 'Europa', 'América',
                  'Europa',
                  'América', 'Europa', 'Europa', 'Europa']
    sql = ('INSERT INTO (idioma) values(%s)')

    for n in tupla1:
        mycursor.executemany(sql, tupla1)
        print(mycursor._rowcount, 'Registro insertado')
    mydb.commit()
    mydb.close()

# hacer consultas:
def consultas(consulta):
    query = ''
    # conectamos con la base de datos
    conn = mysql.connector.connect(host="localhost", port=3306, user='root', password='', database='ranking')
    cursor = conn.cursor()

    # realizamos la query

    if consulta == 1:
        query = "SELECT MIN(año) FROM hits"
    if consulta == 2:
        query = "SELECT SUBSTRING_INDEX(interprete,'y'," \
                "1) AS ARTISTA, COUNT(Interprete) AS TOTAL FROM hits group by SUBSTRING_INDEX(Interprete,'y'," \
                "1) order by count(Interprete) DESC LIMIT 1; "
    if consulta == 3:
        query = "SELECT pais, COUNT(pais) AS TOTAL FROM hits GROUP BY substring_index(pais,','," \
                "1) ORDER BY COUNT(Pais) DESC LIMIT 1; "
    if consulta == 4:
        query = 'SELECT idioma, distinct(tema) from hits'
    if consulta == 5:
        query = "SELECT continente, MAX(COUNT(continente)) from hits"
    if consulta == 6:
        query = "SELECT tema, CONCAT(ROUND(semanas/SUM(semanas * 100),2)) from hits"

    cursor.execute(query)
    dato = cursor.fetchall()

    conn.close()
    print(dato)


insertar_columna()