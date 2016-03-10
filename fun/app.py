from flask import Flask
from flask import render_template

from shared import settings


def create_app():
    app = Flask(__name__)
    app.secret_key = settings.SECRET_KEY
    app.debug = settings.DEBUG
    return app

app = create_app()


@app.route('/')
def main():
    return 'HELLO WORLD'


if __name__ == '__main__':
    app.run('0.0.0.0')
