from django.test import TestCase
from testcases.models import *
from unittest import mock
from datetime import datetime
import pytz

class MSFHistoryModelTest(TestCase):

    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            history_data = MSFHistory.objects.create(
                command = 'post/multi/manage/shell_to_meterpreters',
                job_id = '1254',
                user = 'admin',
            )

            self.assertEqual(history_data.job_id, '1254')
            self.assertEqual(history_data.user, 'admin')
            self.assertEqual(history_data.status, False)
            self.assertEqual(history_data.output, "")
            self.assertEqual(history_data.type, None)
            self.assertEqual(history_data.failed, False)
            self.assertEqual(history_data.initiated_at, mock_date)
            self.assertEqual(history_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            history_data = MSFHistory.objects.create(job_id='1254')

        self.assertEqual(history_data.initiated_at, mock_date)
        self.assertEqual(history_data.updated_at, mock_date)
        self.assertEqual(history_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            history_data.type = None
            history_data.save()

        self.assertEqual(history_data.initiated_at, mock_date)
        self.assertEqual(history_data.updated_at, mock_update_date)
        self.assertEqual(history_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')