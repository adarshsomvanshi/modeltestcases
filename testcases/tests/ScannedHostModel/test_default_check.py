from django.test import TestCase
from testcases.models import *

class ScannedHostModelTest(TestCase):
    def test_shost_default_value_type(self):
        new_host = ScannedHost.objects.create(ip='192.168.1.2')  # Put status=True to check error.
        self.assertFalse(new_host.status)
        self.assertIsNone(new_host.ipv6)
        self.assertIsNone(new_host.mac)
        self.assertIsNone(new_host.hostname)
        self.assertIsNone(new_host.vendor)
        self.assertIsNone(new_host.os)
        self.assertIsNone(new_host.device_type)