from django.test import TestCase
from testcases.models import *

class PortServiceTestCase(TestCase):
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

        self.port_service_data = {
            'port': 8080,
            'port_status': True,
            'service': 'HTTP',
            'job': self.user,
        }
        self.port_service = PortService.objects.create(**self.port_service_data)

    def test_user_deletion(self):
        self.assertTrue(MSFHistory.objects.filter(job_id=self.user_data['job_id']).exists())
        self.assertTrue(PortService.objects.filter(port=8080, service='HTTP').exists())
        self.user.delete()
        self.assertFalse(MSFHistory.objects.filter(job_id=self.user_data['job_id']).exists())
        self.assertFalse(PortService.objects.filter(port=8080, service='HTTP').exists())

