from django.test import TestCase
from testcases.models import *

class PortServiceModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.msf_history = MSFHistory.objects.create(job_id=1)
    
    def test_ps_data_creation(self):
        ps_data = PortService.objects.create(
            port = 8080,
            port_status = False,
            service = 'HTTP',
            job = self.msf_history
        )
        self.assertTrue(isinstance(ps_data, PortService))