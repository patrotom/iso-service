from iso_service.utils.country_matcher import CountryMatcher


def test_run_with_valid_data(valid_request_data, valid_response_data):
    result = CountryMatcher(valid_request_data['iso'],
                            valid_request_data['countries']).run()

    assert result.success == True
    assert result.data == valid_response_data
    assert result.http_code == 200


def test_run_with_invalid_iso(valid_request_data):
    result = CountryMatcher('123', valid_request_data['countries']).run()

    expected_errors = ['ISO code not found in our database']

    assert result.success == False
    assert result.errors == expected_errors
    assert result.http_code == 400


def test_run_with_invalid_iso_length(valid_request_data):
    result = CountryMatcher('a', valid_request_data['countries']).run()

    expected_errors = ['Invalid length of ISO code']

    assert result.success == False
    assert result.errors == expected_errors
    assert result.http_code == 400


def test_run_with_invalid_input():
    result = CountryMatcher([], []).run()

    expected_errors = ["'list' object has no attribute 'upper'"]

    assert result.success == False
    assert result.errors == expected_errors
    assert result.http_code == 500
