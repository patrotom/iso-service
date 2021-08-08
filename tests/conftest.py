import pytest

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
def valid_request_data():
    return {
        'iso': 'sVk',
        'countries': [
            'iran',
            'Slowakei',
            'Vatikan',
            'Slovačka',
            'Szlovákia',
            'Belgrade',
            'España',
            'Nizozemsko'
        ]
    }


@pytest.fixture
def valid_response_data():
    return {
        'iso': 'SVK',
        'match_count': 3,
        'matches': [
            'Slowakei',
            'Slovačka',
            'Szlovákia'
        ]
    }
