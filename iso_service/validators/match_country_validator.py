from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

from iso_service.utils.result import Result
from iso_service.validators.base_validator import BaseValidator


SCHEMA = {
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
    json = [JsonSchema(schema=SCHEMA)]


class MatchCountryValidator(BaseValidator):
    def run(self, request):
        if not self._is_json(request):
            return Result(False, http_code=400, errors=['Payload is not a valid JSON'])

        inputs = MatchCountryInputs(request)

        if inputs.validate():
            return Result(True, data=request.get_json())
        else:
            return Result(False, http_code=400, errors=inputs.errors)
