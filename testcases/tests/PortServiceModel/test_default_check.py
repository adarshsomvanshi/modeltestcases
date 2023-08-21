from django.test import TestCase
from testcases.models import *

class PortServiceModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.msf_history = MSFHistory.objects.create(job_id=1)


    def test_ps_data_default(self):
        new_ps_data = PortService.objects.create(
            port=8000,
            service = 'HTTP',
            job = self.msf_history
        )
        self.assertFalse(new_ps_data.port_status)
        # self.assertTrue(new_ps_data.port_status)  # wrong value inserted for checking purpose