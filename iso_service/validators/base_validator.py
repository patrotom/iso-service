from flask import Request


class BaseValidator:
    '''
    The `BaseValidator` class contains a common validation functionality. All
    specific validators should inherit from the `BaseValidator`. 
    '''
    def _is_json(self, request: Request) -> bool:
        return request.get_json(silent=True) != None
