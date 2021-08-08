import pytest
import json

from iso_service import create_app


@pytest.fixture
def app():
    app = create_app({'TESTING': True})
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def valid_body():
    return json.dumps({
        'iso': 'svk',
        'countries': [
            'iran',
            'Slowakei',
            'Vatikan',
            'Slovaška',
            'Szlovakia',
            'Belgrade',
            'España',
            'Nizozemsko'
        ]
    })
