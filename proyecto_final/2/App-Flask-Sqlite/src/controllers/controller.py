from flask import request, render_template, redirect, flash
from flask.views import MethodView
import sqlite3
from src.db import conn



# pagina de inicio
class IndexController(MethodView):
    def get(self):
        return render_template("/public/index.html")

# mostramos datos de la base de datos
class ShowController(MethodView):

    def get(self):
    # pintamos los datos de la bd

        cursor = conn.execute("SELECT id,nombre,apellidos,password,telefono,edad FROM usuario")
        datos = cursor.fetchall()
        return render_template("/public/mostrar.html", data=datos)



# vamos a crear el controlador para añadir nuevos usuarios
class InsertController(MethodView):
    def get(self):
        return render_template("/public/mostrar.html")

    def post(self):
        # Traemos los datos desde el formulario de navbar.html
        nombre = request.form['nombre']
        apellido = request.form['apellidos']
        clave = request.form['password']
        telefono = request.form['telefono']
        edad = request.form['edad']
        print(nombre, apellido, clave, telefono, edad)
        # vamos a hacer la inserccion en la bd
        try:
            conn.execute("INSERT INTO usuario(nombre, apellidos, password, telefono, edad) VALUES(?,?,?,?,?)",
                        (nombre, apellido, clave, telefono, edad))
            conn.commit()
            flash("inserccion realizada", "success")
        except:
            flash("Ha ocurrido un error", "error")

        return redirect('/show/usuario')





# vamos a crear el controlador para eliminar usuarios

class DeleteController(MethodView):
    def post(self, id):

        # para ejecutar bien esta query hay que poner una tupla en este caso vacia (id, )
        try:
            conn.execute("DELETE FROM usuario WHERE id= ?", (id,))
            conn.commit()
            flash("Usuario Eliminado", "success")
            return render_template('/public/index.html')
        except:
            flash("No se ha podido eliminar el Usuario", "error")
        return render_template('/public/mostrar.html')

class updateController(MethodView):
    def get(self, id):
        cursor = conn.execute("SELECT * FROM usuario WHERE id = ?", (id,))
        # fetchone para que me devuelva solo ese valor
        usuario_encontrado = cursor.fetchone()
        return render_template('public/update.html', data=usuario_encontrado)

    def post(self, id):

        try:
            nombre = request.form['nombre']
            apellido = request.form['apellidos']
            password = request.form['password']
            telefono = request.form['telefono']
            edad = request.form['edad']
            # traemos los datos desde update.html, hacemos  la query y la ejecutamos con commit()
            conn.execute("UPDATE usuario SET nombre=?, apellidos=?, password=?, telefono=?, edad=? WHERE ID=?",
                        (nombre, apellido, password, telefono, edad, id))
            conn.commit()
            flash("Actualización realizada", "success")
        except:
            flash("Ha habido un error en la Actualización", "error")
        return redirect('/show/usuario')
