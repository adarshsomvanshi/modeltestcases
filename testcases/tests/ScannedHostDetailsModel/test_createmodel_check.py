from django.test import TestCase
from testcases.models import *

class ScannedHostDetailModelTest(TestCase):
    def setUp(self):
        self.new_scanned_host = ScannedHost.objects.create(ip='192.168.1.1')
        self.new_sh_details = ScannedHostDetails.objects.create(
            scanned_host = self.new_scanned_host,
            port = '80',
            service = 'HTTP',
            version = '2.0',
            additional_data = {'key':'value'},
        )
    def test_model_creation(self):
        self.assertTrue(isinstance(self.new_sh_details, ScannedHostDetails))
