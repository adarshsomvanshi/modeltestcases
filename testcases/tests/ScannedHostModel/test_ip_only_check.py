from django.test import TestCase
from testcases.models import *

class ScannedHostModelTest(TestCase):
    def test_scannedhost_ip_only(self):
        ip = '192.168.1.2'
        new_scanhost = ScannedHost.objects.create(ip=ip)
        self.assertEqual(new_scanhost.ip,ip)
        self.assertIsNone(new_scanhost.ipv6)
        self.assertIsNone(new_scanhost.mac)
        self.assertIsNone(new_scanhost.hostname)
        self.assertIsNone(new_scanhost.vendor)
        self.assertIsNone(new_scanhost.device_type)
        self.assertFalse(new_scanhost.status)