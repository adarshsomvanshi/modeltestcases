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
        self.assertEqual(int(ps_data.port), ps_data.port)
        self.assertEqual(bool(ps_data.port_status), ps_data.port_status)
        self.assertEqual(str(ps_data.service), ps_data.service)