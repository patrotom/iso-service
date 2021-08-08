import os
import json

from iso_service.utils.result import Result


class CountryMatcher:
    def __init__(self, iso, countries):
        self.iso = iso
        self.countries = countries

    def run(self):
        try:
            self.iso = self.iso.upper()
            matches = []

            iso_country_data = self.__find_iso_country_data()

            for country_name in self.countries:
                if self.__country_name_matches_iso(country_name, iso_country_data):
                    matches.append(country_name)

            data = {'iso': self.iso, 'match_count': len(matches), 'matches': matches}

            return Result(True, data=data)
        except CountryMatcherError as e:
            return Result(False, http_code=400, errors=[str(e)])
        except Exception as e:
            return Result(False, http_code=500, errors=[str(e)])

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
            raise CountryMatcherError('Invalid length of ISO code')

        country_data = next(
            (c for c in countries_data if c[iso_type].upper() == self.iso),
            None
        )

        if country_data == None:
            raise CountryMatcherError('ISO code not found in our database')

        return country_data

    def __load_countries_data(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path_segments = dir_path.split('/')[:-2]
        path_segments.append('data/countries.json')
        file_path = '/'.join(path_segments)

        with open(file_path, 'r') as f:
            return json.load(f)



class CountryMatcherError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message
