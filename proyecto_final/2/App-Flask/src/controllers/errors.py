from flask.views import MethodView


#creamos la ruta
class NotFoundController(MethodView):
    def get(self, error):
        return f"Pagina no se encontró, {error}"
