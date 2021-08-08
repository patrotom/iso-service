class Result:
    def __init__(self, success, http_code=200, data=None, errors=None):
        self.success = success
        self.http_code = http_code
        self.data = data
        self.errors = errors

    def to_response(self):
        if self.success:
            return {'data': self.data}, self.http_code
        else:
            return {'errors': self.errors}, self.http_code
