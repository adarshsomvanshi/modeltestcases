from django.test import TestCase
from testcases.models import *

class MSFHistoryModelTest(TestCase):
    def setUp(self):
        self.history_data = MSFHistory.objects.create(
            command='exploit/windows/smb/ms17_010_eternalblue',
            job_id='12346789',
            user='admin',
            status=True,
            output='Exploit Completed successfully',
            type='expliot',
            failed= False
        )
    
    def test_string_representation(self):
        self.assertEqual(str(self.history_data.command), self.history_data.command)
        self.assertEqual(str(self.history_data.job_id), self.history_data.job_id)
        self.assertEqual(str(self.history_data.user), self.history_data.user)
        self.assertEqual(bool(self.history_data.status), self.history_data.status)
        self.assertEqual(str(self.history_data.output), self.history_data.output)
        self.assertEqual(str(self.history_data.type), self.history_data.type)
        self.assertEqual(bool(self.history_data.failed), self.history_data.failed)