from flask import request, render_template, redirect
from flask.views import MethodView
from src.db import mysql



# vamos a crear el controlador para añadir nuevos usuarios
class IndexController(MethodView):

    def get(self):
    # pintamos los datos de la bd
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM usuario")
            datos = cur.fetchall()
            print(datos)
            return render_template("public/index.html", data=datos)




class InsertController(MethodView):
    def get(self):
        return render_template("/public/insert.html")

    def post(self):
        # vamos a hacer la insercción de datos
        nombre = request.form['nombre']
        apellido = request.form['apellidos']
        clave = request.form['password']
        telefono = request.form['telefono']
        edad = request.form['edad']

        # vamos a hacer la inserccion en la bd

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO usuario(nombre, apellidos, password, telefono, edad) VALUES(%s,%s,%s,%s,%s)",
                        (nombre, apellido, clave, telefono, edad))
            cur.connection.commit()
            print("inserccion realizada")
            return "Insercción realizada"





# vamos a crear el controlador para eliminar usuarios

class DeleteController(MethodView):
    def post(self, id):

        with mysql.cursor() as cur:
            cur.execute("DELETE FROM usuario WHERE id= %s", id)
            cur.connection.commit()
            print("elemento borrado")
            return redirect('/')

class updateController(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM usuario WHERE id = %s", id)
            #fetchone para que me devuelva solo ese valor
            usuarioEncontrado = cur.fetchone()
        return render_template('public/update.html', idEncontrado=usuarioEncontrado)

    def post(self, id):

        nombre = request.form['nombre']
        apellido = request.form['apellidos']
        password = request.form['password']
        telefono = request.form['telefono']
        edad = request.form['edad']
        print(nombre, apellido, password, telefono, edad)

        with mysql.cursor() as cur:
            cur.execute("UPDATE usuario SET nombre=%s, apellidos=%s, password=%s, telefono=%s, edad=%s WHERE ID=%s",
                        (nombre, apellido, password, telefono, edad, id))
            cur.connection.commit()
            return f"recopilando actualizacion de usuario {id}"
