import os

from flask import Flask

from iso_service.blueprints import country
from iso_service.cache import cache


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    if test_config is not None:
        app.config.from_mapping(test_config)

    cache.init_app(app)

    app.register_blueprint(country.bp)

    return app
