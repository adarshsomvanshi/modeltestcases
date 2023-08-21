from django.test import TestCase
from testcases.models import *

class MSFHistoryTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'command': 'test-command',
            'job_id': 'test-job-id',
            'user': 'TestUser',
            'status': True,
            'output': 'Test output.',
            'type': 'Test type',
            'failed': False,
        }
        self.user = MSFHistory.objects.create(**self.user_data)

    def test_user_deletion(self):
        # Ensure the user exists before deletion
        self.assertTrue(MSFHistory.objects.filter(job_id=self.user_data['job_id']).exists())

        # Delete the user
        self.user.delete()

        # Ensure the user no longer exists after deletion
        self.assertFalse(MSFHistory.objects.filter(job_id=self.user_data['job_id']).exists())
