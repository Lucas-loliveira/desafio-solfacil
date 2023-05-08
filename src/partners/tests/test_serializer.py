import csv
import io
from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from partners.models import Partner
from partners.serializers import PartnerSerializer

from .conftest import DATA_EXAMPLE


class PartnerSerializerTestCase(TestCase):
    def setUp(self):
        self.valid_cnpj = "01360643000109"
        self.invalid_cnpj = "11111111111111"
        self.valid_data = {
            "cnpj": self.valid_cnpj,
            "name": "Test Company",
            "trade_name": "Test Co",
            "phone": "1111111111",
            "email": "test@test.com",
            "zip_code": "11111-111",
        }
        self.invalid_data = {
            "cnpj": self.invalid_cnpj,
            "name": "Test Company",
            "trade_name": "Test Co",
            "phone": "1111111111",
            "email": "test@test.com",
            "zip_code": "11111-111",
        }

    def test_valid_partner_serializer(self):
        serializer = PartnerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_partner_serializer(self):
        serializer = PartnerSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors, {"cnpj": ["Invalid cnpj"]})

    def test_create_partner(self):
        serializer = PartnerSerializer(data=self.valid_data)
        serializer.is_valid()
        partner, created = serializer.save()
        self.assertTrue(created)
        self.assertIsInstance(partner, Partner)
