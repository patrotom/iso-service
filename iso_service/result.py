class Result:
    def __init__(self, data, success, http_code=200, error=''):
        self.data = data
        self.success = success
        self.http_code = http_code
        self.error = error
