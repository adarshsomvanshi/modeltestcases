from django.test import TestCase
from testcases.models import *

class ScannedHostModelTest(TestCase):
    def setUp(self):
        self.host_name = ScannedHost.objects.create(
            ip = '192.168.1.1',
            ipv6 = '2001:db8::1',
            mac = '00:1A:2B:3C:4D:5E',
            hostname = 'example.com',
            vendor = 'Vendor Inc.',
            os = 'Linux',
            device_type = 'Server',
            status = False
        )
    def test_model_creation(self):
        self.assertTrue(isinstance(self.host_name, ScannedHost))