from src.controllers.controller import *
from src.controllers.errors import NotFoundController


#definimos un diccionario para registrar las distintas rutas
# la primera clave será la ruta, la segunda clave es el controlador

routes = {
    "index_route": "/", "index_controller": IndexController.as_view("index"),
    "insert_route": "/insert/usuario", "insert_controller": InsertController.as_view("insert"),
    "update_route": "/update/usuario/<int:id>", "update_controller": updateController.as_view("actualizando"),
    "delete_route": "/delete/usuario/<int:id>", "delete_controller": DeleteController.as_view("borrando"),
    "not_found_route": 404, "not_found_controller": NotFoundController.as_view("not_found")
}