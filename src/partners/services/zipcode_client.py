from typing import Union

import requests


class ZipCodeApi:
    def __init__(self):
        self.base_url = "https://viacep.com.br/ws/"
        self.suffix = "/json/"

    def get_address(self, zip_code: str) -> Union[dict, bool]:
        response = requests.get(self.base_url + zip_code + self.suffix)

        if response.status_code != 200 or response.json().get("erro", False):
            return False
        return response.json()
