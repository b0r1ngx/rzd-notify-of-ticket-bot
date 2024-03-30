from datetime import date

import requests

from business.api.constants import *


def search_train_by_date(date: date):
    response = requests.post(
        url=search_train_url,
        params=params,
        cookies=cookies,
        headers=headers,
        json=_create_body(date=date),
    )
    return response.json()


# todo: need to understand Origin & Destination,
#       for user can search for any cities
def _create_body(date: date):
    return {
        'Origin': '2005594',
        'Destination': '2004000',
        'DepartureDate': date.isoformat() + 'T00:00:00',
        'TimeFrom': 0,
        'TimeTo': 24,
        'CarGrouping': 'DontGroup',
        'GetByLocalTime': True,
        'SpecialPlacesDemand': 'StandardPlacesAndForDisabledPersons',
        'CarIssuingType': 'All',
        'GetTrainsFromSchedule': True,
    }
