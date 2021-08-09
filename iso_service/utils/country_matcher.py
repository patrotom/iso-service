import os
import json

from typing import List

from iso_service.utils.result import Result


class CountryMatcher:
    '''
    The CountryMatcher class is a simple service class that takes `iso` code
    `countries` list and filters out the countries (names) corresponding to the
    given `iso` code.
    
    The `iso` code is a `String` that corresponds to the ISO 3166-1 alpha-2 or
    alpha-3 standards.

    The `countries` are a `List` of `String`s with the country names that can be
    in different languages.
    '''
    def __init__(self, iso: str, countries: List[str]):
        self.iso = iso
        self.countries = countries

    def run(self) -> Result:
        '''
        Filters out the country names based on the given ISO code. It returns the
        `Result` object that can be either success or failure.

        It uses localization data from the file `countries.json` located under
        the `data/` directory in the root of the repository.
        '''
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
    '''
    The `CountryMatcherError` class represents an error that occurred while
    matching the countries. This error occurs when someone provides invalid
    data to the `CountryMatcher`.
    '''
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message
