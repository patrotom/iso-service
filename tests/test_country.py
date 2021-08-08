import pytest
import json


def test_match_country(client, valid_body):
    response = client.post('/match_country', data=valid_body)
    body = response.get_json(force=True)
    expected_body = {
        'iso': 'svk',
        'match_count': 3,
        'matches': [
            'Slowakei',
            'Slovaška',
            'Szlovakia'
        ]
    }

    assert response.status_code == 200
    assert body == expected_body
