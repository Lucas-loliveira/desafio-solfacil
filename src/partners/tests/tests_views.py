import csv
import io
from unittest.mock import patch

from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITransactionTestCase

from partners.models import Partner

from .conftest import DATA_EXAMPLE


class PartnerTestCase(APITransactionTestCase):
    def setUp(self):
        self.url = reverse("import-partners-list")
        data = DATA_EXAMPLE

        csv_string = io.StringIO()
        writer = csv.DictWriter(csv_string, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        csv_string.seek(0)

        self.csv_file = io.StringIO(csv_string.read())
        self.csv_file.name = "test.csv"

    @patch("partners.serializers.ZipCodeApi.get_address")
    def test_import_partner(self, mock_address):
        mock_address.return_value = {
            "localidade": "São Paulo",
            "uf": "SP",
        }
        response = self.client.post(self.url, {"data": self.csv_file})
        response_json = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Partner.objects.count(), 1)
        self.assertEqual(len(response_json["created"]), 1)
        self.assertEqual(len(response_json["updated"]), 0)
        self.assertEqual(len(response_json["errors"]), 4)

    def test_import_partner_wrong_file_type(self):
        self.csv_file.name = "test.txt"
        response = self.client.post(self.url, {"data": self.csv_file})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()["data"][0],
            "File extension “txt” is not allowed. Allowed extensions are: csv.",
        )
