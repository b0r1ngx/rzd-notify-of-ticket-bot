import requests

from business.api.constants import *
from business.is_tickets_available import is_tickets_available


def search_train_by_date():
    response = requests.post(
        url=search_train_url,
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return response.json()


# test
if __name__ == '__main__':
    request = search_train_by_date()
    is_available, train = is_tickets_available(request)
    print(is_available, train)
