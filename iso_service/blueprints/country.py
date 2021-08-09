from flask import Blueprint, request

from iso_service.cache import cache
from iso_service.utils.country_matcher import CountryMatcher
from iso_service.validators.match_country_validator import MatchCountryValidator


bp = Blueprint('country', __name__)


@bp.route('/match_country', methods=['POST'])
@cache.cached(timeout=20)
def match_country():
    '''Filters out the country names corresponding to the given ISO code.'''
    validation = MatchCountryValidator().run(request)

    if not validation.success:
        return validation.to_response()

    payload = validation.data
    result = CountryMatcher(payload['iso'], payload['countries']).run()

    return result.to_response()
