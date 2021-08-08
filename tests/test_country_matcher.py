from iso_service.country_matcher import CountryMatcher


def test_run_with_valid_data(valid_request_data, valid_response_data):
    result = CountryMatcher(valid_request_data['iso'],
                            valid_request_data['countries']).run()

    assert result.success == True
    assert result.data == valid_response_data
