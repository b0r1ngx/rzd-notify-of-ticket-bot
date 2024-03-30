import requests

from business.api.constants import *


def search_train_by_date():
    response = requests.post(
        url=search_train_url,
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return response.json()
