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
    def test_model_creation(self):
        self.assertTrue(isinstance(self.history_data, MSFHistory))
