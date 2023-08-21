from django.test import TestCase
from testcases.models import *

class ScannedHostDetailModelTest(TestCase):
    def setUp(self):
        self.new_scanned_host = ScannedHost.objects.create(ip='192.168.1.1')

    def test_default_value(self):
        new_host_type = ScannedHostDetails.objects.create(
            scanned_host = self.new_scanned_host,
            port = '443',
            # version = '3.0' #for checking purpose put version = 3 it shows error
        )
        self.assertEqual(new_host_type.service, 'Unknown')
        