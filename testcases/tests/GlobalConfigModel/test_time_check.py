from django.test import TestCase
from testcases.models import *
from unittest import mock
from datetime import datetime
import pytz

class GlobalConfigModelTest(TestCase):

    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            gc_data = GlobalConfig.objects.create(
                action = 'increase'
            )

            self.assertEqual(gc_data.action, 'increase')
            self.assertIsNone(gc_data.value)
            self.assertIsNone(gc_data.setting)
            self.assertIsNone(gc_data.description)
            self.assertEqual(gc_data.extra, {})
            self.assertEqual(gc_data.created_at, mock_date)
            self.assertEqual(gc_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            gc_data = GlobalConfig.objects.create(action='increase')

        self.assertEqual(gc_data.created_at, mock_date)
        self.assertEqual(gc_data.updated_at, mock_date)
        self.assertEqual(gc_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            gc_data.setting = None
            gc_data.save()

        self.assertEqual(gc_data.created_at, mock_date)
        self.assertEqual(gc_data.updated_at, mock_update_date)
        self.assertEqual(gc_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')