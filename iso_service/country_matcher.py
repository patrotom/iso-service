from iso_service.result import Result


class CountryMatcher:
    def __init__(self, iso, countries):
        self.iso = iso
        self.countries = countries

    def run(self):
        result = Result({}, True)

        return result
