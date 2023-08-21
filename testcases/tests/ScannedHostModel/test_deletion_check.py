from django.test import TestCase
from testcases.models import *

class ScannedHostModelTest(TestCase):
    def setUp(self):
        self.host_name = {
            'ip' : '192.168.1.1',
            'ipv6' : '2001:db8::1',
            'mac' : '00:1A:2B:3C:4D:5E',
            'hostname' : 'example.com',
            'vendor' : 'Vendor Inc.',
            'os' : 'Linux',
            'device_type' : 'Server',
            'status' : False
        }
        self.user = ScannedHost.objects.create(**self.host_name)

    def test_deletion(self):
        self.assertTrue(ScannedHost.objects.filter(ip = self.host_name['ip']).exists())
        self.user.delete()
        self.assertFalse(ScannedHost.objects.filter(ip = self.host_name['ip']).exists())