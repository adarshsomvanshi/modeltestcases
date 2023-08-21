from django.test import TestCase
from testcases.models import *

class MSFHistoryModelTest(TestCase):

    def test_nullable_type_field(self):
        history_entry = MSFHistory.objects.create(
            command='use auxiliary/scanner/smb/smb_version',
            # job_id='246813579',
            user='user2',
            status=True,
            output='Scanning completed',
            failed=False
        )
        self.assertIsNone(history_entry.job_id)
        self.assertIsNone(history_entry.type)