from unittest.mock import patch

from django.test import TestCase

from partners.models import Partner

from .conftest import VALID_DATA


class SendWelcomeEmailTestCase(TestCase):
    def setUp(self):
        self.valid_data = VALID_DATA

    @patch("partners.signals.send_email")
    def test_send_welcome_email(self, mock_send_welcome_email):
        Partner.objects.create(**self.valid_data)
        self.assertTrue(mock_send_welcome_email.called)
