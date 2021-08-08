import os
import json

from iso_service.result import Result


class CountryMatcher:
    def __init__(self, iso, countries):
        self.iso = iso.upper()
        self.countries = countries

    def run(self):
        matches = []

        iso_country_data = self.__find_iso_country_data()

        for country_name in self.countries:
            if self.__country_name_matches_iso(country_name, iso_country_data):
                matches.append(country_name)

        data = {"iso": self.iso, "match_count": len(matches), "matches": matches}

        return Result(data, True)

    def __country_name_matches_iso(self, country_name, country_data):
        for trans in country_data['translations'].values():
            if country_name == trans['official'] or country_name == trans['common']:
                return True

        return False

    def __find_iso_country_data(self):
        countries_data = self.__load_countries_data()

        if len(self.iso) == 3:
            iso_type = 'cca3'
        elif len(self.iso) == 2:
            iso_type = 'cca2'
        else:
            raise RuntimeError('Invalid length of ISO code')

        return next(c for c in countries_data if c[iso_type].upper() == self.iso)

    def __load_countries_data(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path_segments = dir_path.split('/')[:-1]
        path_segments.append('data/countries.json')
        file_path = '/'.join(path_segments)

        with open(file_path, 'r') as f:
            return json.load(f)
