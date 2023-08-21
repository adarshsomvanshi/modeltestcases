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
    def test_string_representation(self):
        self.assertEqual(str(self.host_name.ip), self.host_name.ip)
        self.assertEqual(str(self.host_name.ipv6), self.host_name.ipv6)
        self.assertEqual(str(self.host_name.mac), self.host_name.mac)
        self.assertEqual(str(self.host_name.hostname), self.host_name.hostname)
        self.assertEqual(str(self.host_name.vendor), self.host_name.vendor)
        self.assertEqual(str(self.host_name.os), self.host_name.os)
        self.assertEqual(str(self.host_name.device_type), self.host_name.device_type)
        self.assertEqual(bool(self.host_name.status), self.host_name.status)