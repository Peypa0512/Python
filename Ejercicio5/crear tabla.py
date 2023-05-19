import sqlite3


conn = sqlite3.connect("ranking.db")
print("Conexion establecida")

cursor = conn.cursor()
cursor.execute("CREATE TABLE hits(id,tema, interprete, año, semanas, pais)")
conn.close()