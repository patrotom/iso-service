class BaseValidator:
    def _is_json(self, request):
        return request.get_json(silent=True) != None
