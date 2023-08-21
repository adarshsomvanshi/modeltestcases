from django.test import TestCase
from testcases.models import *
from unittest import mock
from datetime import datetime
import pytz

class CVEDataModelTest(TestCase):
        
    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            cve_data = CVEData.objects.create(
                id = 'CVE-2021-147'
            )

            self.assertEqual(cve_data.id, 'CVE-2021-147')
            self.assertEqual(cve_data.status, 'ENTRY')
            self.assertEqual(cve_data.description, '')
            self.assertEqual(cve_data.references, '')
            self.assertEqual(cve_data.phase, '')
            self.assertEqual(cve_data.votes, '')
            self.assertEqual(cve_data.comments, '')
            self.assertEqual(cve_data.added_by, '')
            self.assertEqual(cve_data.created_at, mock_date)
            self.assertEqual(cve_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            cve_data = CVEData.objects.create(id = 'CVE-2021-147')

        self.assertEqual(cve_data.created_at, mock_date)
        self.assertEqual(cve_data.updated_at, mock_date)
        self.assertEqual(cve_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            cve_data.votes = ""
            cve_data.save()

        self.assertEqual(cve_data.created_at, mock_date)
        self.assertEqual(cve_data.updated_at, mock_update_date)
        self.assertEqual(cve_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')