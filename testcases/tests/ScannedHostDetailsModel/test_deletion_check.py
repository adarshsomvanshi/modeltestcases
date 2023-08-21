from django.test import TestCase
from testcases.models import *

class ScannedHostDetailsTestCase(TestCase):
    def setUp(self):
        self.scanned_host_data = {
            'ip' : '192.168.1.1',
            'ipv6' : '2001:db8::1',
            'mac' : '00:1A:2B:3C:4D:5E',
            'hostname' : 'example.com',
            'vendor' : 'Vendor Inc.',
            'os' : 'Linux',
            'device_type' : 'Server',
            'status' : False
        }
        self.scanned_host = ScannedHost.objects.create(**self.scanned_host_data)

        self.scanned_host_details_data = {
            'scanned_host': self.scanned_host,
            'port': '8080',
            'service': 'HTTP',
            'version': '1.0',
            'additional_data': {'key': 'value'},
        }
        self.scanned_host_details = ScannedHostDetails.objects.create(**self.scanned_host_details_data)

    def test_user_deletion(self):
        self.assertTrue(ScannedHost.objects.filter(ip=self.scanned_host.ip).exists())
        self.assertTrue(
            ScannedHostDetails.objects.filter( port=self.scanned_host_details_data['port']).exists()
        )
        self.scanned_host.delete()
        self.assertFalse(ScannedHost.objects.filter(ip=self.scanned_host.ip).exists())
        self.assertFalse(ScannedHostDetails.objects.filter( port=self.scanned_host_details_data['port']).exists())