from flask import Flask
from src.routes.routes import *
# con esto iniciamos la aplicacion
app = Flask(__name__)

# es importarte por tema de seguridad la llave secreta y con ello podemos utilizar los mensajes flash
app.config.from_mapping(
    SECRET_KEY='development')

# Rutas de la aplicación
app.add_url_rule(routes["index_route"], view_func=routes['index_controller'])
app.add_url_rule(routes["show_route"], view_func=routes["show_controller"])
app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])
app.add_url_rule(routes["update_route"], view_func=routes["update_controller"])
app.add_url_rule(routes["insert_route"], view_func=routes["insert_controller"])

# ruta del 404
@app.errorhandler(404)
def base_error(e):
    return render_template("public/404.html"), 404

#ruta del 405
@app.errorhandler(405)
def base_error(e):
    return render_template("public/404.html"), 405
