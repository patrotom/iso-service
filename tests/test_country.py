import json


def test_match_country_with_valid_data(client, valid_request_data, valid_response_data):
    response = client.post('/match_country', data=json.dumps(valid_request_data))
    body = response.get_json(force=True)
    expected_body = {'data': valid_response_data}

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert body == expected_body


def test_match_country_with_invalid_iso(client):
    data = {'iso': '123', 'countries': []}
    response = client.post('/match_country', data=json.dumps(data))

    assert response.status_code == 400


def test_match_country_with_invalid_data(client):
    data = {'iso': '123', 'countries': []}
    response = client.post('/match_country', data=json.dumps(data))

    assert response.status_code == 400
