import os

from flask import Flask

from iso_service.blueprints import country


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is not None:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(country.bp)

    return app
