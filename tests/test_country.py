import json


def test_match_country_with_valid_data(client, valid_request_data, valid_response_data):
    response = client.post('/match_country', data=json.dumps(valid_request_data))
    body = response.get_json(force=True)
    expected_body = {'data': valid_response_data}

    assert response.status_code == 200
    assert body == expected_body
