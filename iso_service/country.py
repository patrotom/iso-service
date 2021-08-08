from flask import Blueprint, request


from iso_service.country_matcher import CountryMatcher
from iso_service.validators.match_country_validator import MatchCountryValidator


bp = Blueprint('country', __name__)


@bp.route('/match_country', methods=['POST'])
def match_country():
    validation = MatchCountryValidator().run(request)

    if not validation.success:
        return validation.to_response()

    payload = validation.data
    result = CountryMatcher(payload['iso'], payload['countries']).run()

    return result.to_response()
