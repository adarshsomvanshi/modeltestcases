from django.test import TestCase
from testcases.models import *

class ScannedHostDetailModelTest(TestCase):
    def setUp(self):
        self.new_scanned_host = ScannedHost.objects.create(ip='192.168.1.1')

    def test_additional_data(self):
        additional_data = {'key1': 'value1', 'key2': 'value2'}
        new_host_details = ScannedHostDetails.objects.create(
            scanned_host=self.new_scanned_host,
            port='8080',
            service='Custom',
            additional_data=additional_data
        )
        self.assertEqual(new_host_details.additional_data, additional_data)