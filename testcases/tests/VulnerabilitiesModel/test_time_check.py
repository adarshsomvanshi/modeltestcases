from django.test import TestCase
from django.contrib.auth.models import User
from testcases.models import *
from unittest import mock
from datetime import datetime
import pytz


class VulnerabilitiesModelTest(TestCase):
    
    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            vul_data = Vulnerabilities.objects.create(
                unique_id = 'CVE-2023-1245',
                ip = '192.168.1.6',
                port = 448,
                location = 'Another Sample Location',
                rule_id='R504',
                source='Another Sample Sources',
                rule_severity=6,
            )

            self.assertEqual(vul_data.unique_id, 'CVE-2023-1245')
            self.assertEqual(vul_data.ip, '192.168.1.6')
            self.assertEqual(vul_data.port, 448)
            self.assertEqual(vul_data.location, 'Another Sample Location')
            self.assertEqual(vul_data.rule_id, 'R504')
            self.assertEqual(vul_data.source, 'Another Sample Sources')
            self.assertEqual(vul_data.rule_severity, 6)
            self.assertEqual(vul_data.status, 'Open')
            self.assertEqual(vul_data.assignee, 'Unassigned')
            self.assertEqual(vul_data.history, '')
            self.assertIsNone(vul_data.org)
            self.assertIsNone(vul_data.rule_description)
            self.assertIsNone(vul_data.rule_finding)
            self.assertIsNone(vul_data.info)
            self.assertIsNone(vul_data.timestamp)
            self.assertIsNone(vul_data.jira)
            self.assertIsNone(vul_data.notes)
            self.assertIsNone(vul_data.creator)
            self.assertIsNone(vul_data.owner)
            self.assertIsNone(vul_data.creator)
            self.assertIsNone(vul_data.service_owner)
            self.assertEqual(vul_data.created_at, mock_date)
            self.assertEqual(vul_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            vul_data = Vulnerabilities.objects.create(
                unique_id = 'CVE-2023-1245',
                ip = '192.168.1.6',
                port = 448,
                location = 'Another Sample Location',
                rule_id='R504',
                source='Another Sample Sources',
                rule_severity=6,
            )

        self.assertEqual(vul_data.created_at, mock_date)
        self.assertEqual(vul_data.updated_at, mock_date)
        self.assertEqual(vul_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            vul_data.unique_id = True
            vul_data.save()

        self.assertEqual(vul_data.created_at, mock_date)
        self.assertEqual(vul_data.updated_at, mock_update_date)
        self.assertEqual(vul_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')