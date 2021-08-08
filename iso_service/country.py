from flask import Blueprint, request


from iso_service.country_matcher import CountryMatcher
from iso_service.country_validations import validate_match_country


bp = Blueprint('country', __name__)


@bp.route('/match_country', methods=['POST'])
def match_country():
    payload = request.get_json(force=True)

    result = validate_match_country(request)
    if result.success:
        result = CountryMatcher(payload['iso'], payload['countries']).run()

    if result.success:
        return {'data': result.data}, result.http_code
    else:
        return {'errors': result.errors}, result.http_code
