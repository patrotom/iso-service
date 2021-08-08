import json


def test_match_country_with_valid_data(client, valid_request_data, valid_response_data):
    response = client.post('/match_country', data=json.dumps(valid_request_data),
                                             content_type='application/json')
    body = response.get_json()
    expected_body = {'data': valid_response_data}

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert body == expected_body


def test_match_country_with_invalid_iso(client):
    data = {'iso': '123', 'countries': []}
    response = client.post('/match_country', data=json.dumps(data),
                                             content_type='application/json')

    assert response.status_code == 400


def test_match_country_with_missing_property(client):
    data = {'countries': []}
    response = client.post('/match_country', data=json.dumps(data),
                                             content_type='application/json')
    body = response.get_json()

    assert body['errors'][0] == "'iso' is a required property"
    assert response.status_code == 400


def test_match_country_with_invalid_data(client):
    response = client.post('/match_country', data=json.dumps([]),
                                             content_type='application/json')
    body = response.get_json()

    assert body['errors'][0] == "None is not of type 'object'"
    assert response.status_code == 400


def test_match_country_with_invalid_content_type(client):
    response = client.post('/match_country', data=json.dumps({}))
    body = response.get_json()

    assert body['errors'][0] == 'Payload is not a valid JSON'
    assert response.status_code == 400


def test_match_country_with_invalid_json(client):
    response = client.post('/match_country', data='<>',
                                             content_type='application/json')
    body = response.get_json()

    assert body['errors'][0] == 'Payload is not a valid JSON'
    assert response.status_code == 400
