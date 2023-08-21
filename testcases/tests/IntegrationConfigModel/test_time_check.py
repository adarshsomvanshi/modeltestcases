from django.test import TestCase
from testcases.models import *
from unittest import mock
from datetime import datetime
import pytz

class IntegrationConfigModelTest(TestCase):

    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            ic_data = IntegrationConfig.objects.create(
                org_name = 'Sample_org'
            )

            self.assertEqual(ic_data.org_name, 'Sample_org')
            self.assertEqual(ic_data.type, IntegrationConfig.NotificationTypes.NOTIFICATION)
            self.assertEqual(ic_data.identifier, IntegrationConfig.SourceTypes.HTTPENDPOINT)
            self.assertIsNone(ic_data.description)
            self.assertEqual(ic_data.filters, {})
            self.assertEqual(ic_data.config, {})
            self.assertEqual(ic_data.extra, {})
            self.assertEqual(ic_data.created_at, mock_date)
            self.assertEqual(ic_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            ic_data = IntegrationConfig.objects.create(org_name='Sample_org')

        self.assertEqual(ic_data.created_at, mock_date)
        self.assertEqual(ic_data.updated_at, mock_date)
        self.assertEqual(ic_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            ic_data.org_name = None
            ic_data.save()

        self.assertEqual(ic_data.created_at, mock_date)
        self.assertEqual(ic_data.updated_at, mock_update_date)
        self.assertEqual(ic_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')