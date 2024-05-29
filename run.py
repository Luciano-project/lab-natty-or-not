from app import *
from app.routes import app_flask


# Função pra criação de uma predição e salva-lá em static


if __name__ == '__main__':
    app_flask.run(port=5000, debug=True)