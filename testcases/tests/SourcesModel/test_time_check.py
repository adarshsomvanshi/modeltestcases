from django.test import TestCase
from testcases.models import *
from unittest import mock
from datetime import datetime
import pytz

class SourceModelTest(TestCase):
    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            src_data = Sources.objects.create(
                source = 'name.examples.com',
                type = Sources.SourceTypes.IP,
            )

            self.assertEqual(src_data.source, 'name.examples.com')
            self.assertEqual(src_data.type, Sources.SourceTypes.IP)
            self.assertFalse(src_data.is_excluded)
            self.assertFalse(src_data.is_sensitive)
            self.assertIsNone(src_data.included_rules)
            self.assertIsNone(src_data.exclude_rules)
            self.assertIsNone(src_data.org_name)
            self.assertIsNone(src_data.description)
            self.assertIsNone(src_data.identifier)
            self.assertEqual(src_data.created_at, mock_date)
            self.assertEqual(src_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            src_data = Sources.objects.create(source='name.examples.com', type = Sources.SourceTypes.IP)

        self.assertEqual(src_data.created_at, mock_date)
        self.assertEqual(src_data.updated_at, mock_date)
        self.assertEqual(src_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            src_data.is_sensitive = True
            src_data.save()

        self.assertEqual(src_data.created_at, mock_date)
        self.assertEqual(src_data.updated_at, mock_update_date)
        self.assertEqual(src_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')