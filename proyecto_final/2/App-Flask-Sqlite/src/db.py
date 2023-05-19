import sqlite3

# modulo de conexion a la db
conn = sqlite3.connect("usuarios.db", check_same_thread=False)