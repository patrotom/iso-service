from flask import Blueprint, request


from iso_service.country_matcher import CountryMatcher


bp = Blueprint('country', __name__)


@bp.route('/match_country', methods=['POST'])
def match_country():
    payload = request.get_json(force=True)
    result = CountryMatcher(payload['iso'], payload['countries']).run()

    if result.success:
        return {'data': result.data}, result.http_code
    else:
        return {'error': result.error}, result.http_code
