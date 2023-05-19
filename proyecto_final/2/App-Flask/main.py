from src.app import app

# parametros del host
HOST = "localhost"
DEBUG = True
PORT = 4000


if __name__ == '__main__':

    # arrancamos el servidor
    app.run(HOST, PORT, DEBUG)


