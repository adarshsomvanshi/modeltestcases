from django.test import TestCase
from testcases.models import *

class MSFHistoryModelTest(TestCase):

    def test_default_values(self):
        new_history_entry = MSFHistory.objects.create(
            command='post/multi/manage/shell_to_meterpreter',
            job_id='987654321',
            user='user1',
            type = 'post',
        )
        self.assertEqual(new_history_entry.output,"")
        self.assertFalse(new_history_entry.status)
        self.assertFalse(new_history_entry.failed)
