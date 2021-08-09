from typing import Any


class Result:
    '''
    The Result class represents a result of an operation. It can be used in
    various use-cases.

    * `success` - defines whether the operation was successful or not.
    * `http_code` - standard HTTP code corresponding to the result of the operation.
    * `data` - resulting data of the successful operation.
    * `errors` - list of errors when the operation fails.  
    '''
    def __init__(self, success: bool, http_code:int=200, data:Any=None, errors:[]=None):
        self.success = success
        self.http_code = http_code
        self.data = data
        self.errors = errors

    '''
    Converts the data, errors, and HTTP code to the response form based on the
    result of the operation.
    '''
    def to_response(self) -> ({}, int):
        if self.success:
            return {'data': self.data}, self.http_code
        else:
            return {'errors': self.errors}, self.http_code
