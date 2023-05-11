import csv
import io
from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from partners.models import Partner
from partners.serializers import PartnerSerializer

from .conftest import INVALID_CNPJ, INVALID_DATA, VALID_CNPJ, VALID_DATA


class PartnerSerializerTestCase(TestCase):
    def setUp(self):
        self.valid_cnpj = VALID_CNPJ
        self.invalid_cnpj = INVALID_CNPJ
        self.valid_data = VALID_DATA
        self.invalid_data = INVALID_DATA

    def test_valid_partner_serializer(self):
        serializer = PartnerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_partner_serializer(self):
        serializer = PartnerSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors, {"cnpj": ["Invalid cnpj"]})

    @patch("partners.serializers.ZipCodeApi.get_address")
    def test_create_partner(self, mock_address):
        mock_address.return_value = {
            "localidade": "São Paulo",
            "uf": "SP",
        }
        serializer = PartnerSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)

        partner = Partner.objects.get(name="Test Company")
        self.assertEqual(partner.cnpj, self.valid_cnpj)
        self.assertEqual(partner.city, "São Paulo")
        self.assertEqual(partner.state, "SP")
