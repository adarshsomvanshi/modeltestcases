from django.test import TestCase
from django.contrib.auth.models import User
from testcases.models import *
from unittest import mock
from datetime import datetime
import pytz

class RawRequestModelTest(TestCase):

    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            raw_data = RawRequests.objects.create(
                unique_id = '12478'
            )
            self.assertEqual(raw_data.unique_id, '12478')
            self.assertEqual(raw_data.request, None)
            self.assertEqual(raw_data.response, None)
            self.assertEqual(raw_data.created_at, mock_date)
            self.assertEqual(raw_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            raw_data = RawRequests.objects.create(unique_id='12478')

        self.assertEqual(raw_data.created_at, mock_date)
        self.assertEqual(raw_data.updated_at, mock_date)
        self.assertEqual(raw_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            raw_data.request = None
            raw_data.save()

        self.assertEqual(raw_data.created_at, mock_date)
        self.assertEqual(raw_data.updated_at, mock_update_date)
        self.assertEqual(raw_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')