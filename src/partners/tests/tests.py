import csv
import io
from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITransactionTestCase
from .conftest import DATA_EXAMPLE
from partners.models import Partner



class PartnerTestCase(APITransactionTestCase):

    def setUp(self):
        data = DATA_EXAMPLE

        csv_string = io.StringIO()
        writer = csv.DictWriter(csv_string, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        csv_string.seek(0)

        self.csv_file = io.StringIO(csv_string.read())
        self.csv_file.name = 'test.csv'

    def test_import_partner(self):
        url = reverse("import-partners-list")
        response = self.client.post(url, {"data": self.csv_file})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Partner.objects.count(), 1)

    def test_import_partner_wrong_file_type(self):
        url = reverse("import-partners-list")
        self.csv_file.name = 'test.txt'
        response = self.client.post(url, {"data": self.csv_file})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["data"][0],'File extension “txt” is not allowed. Allowed extensions are: csv.')
    
    
        
