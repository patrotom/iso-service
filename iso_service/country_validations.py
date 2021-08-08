from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

from iso_service.result import Result


match_country_schema = {
    'type': 'object',
    'required': [
        'iso',
        'countries'
    ],
    'properties': {
        'iso': {
            'type': 'string'
        },
        'countries': {
            'type': 'array',
            'additionalItems': False,
            'items': {
                'anyOf': [
                    {
                        'type': 'string'
                    }
                ]
            }
        }
    },
    'additionalProperties': False
}


class MatchCountryInputs(Inputs):
    json = [JsonSchema(schema=match_country_schema)]


def validate_match_country(request):
    inputs = MatchCountryInputs(request)

    if inputs.validate():
        return Result(True)
    else:
        return Result(False, http_code=400, errors=inputs.errors)
