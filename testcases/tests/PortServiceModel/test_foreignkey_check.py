from django.test import TestCase
from testcases.models import *


class PortServiceModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.msf_history = MSFHistory.objects.create(job_id=1)
    

    def test_ps_data_foreign_key(self):
        new_ps_data = PortService.objects.create(
            port=8000,
            service = 'HTTP',
            # job = 'computer operator',
            job = self.msf_history
        )
        self.assertEqual(new_ps_data.job, self.msf_history)