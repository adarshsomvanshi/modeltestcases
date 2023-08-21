from django.test import TestCase
from testcases.models import *


class ScannedHostDetailModelTest(TestCase):
    def setUp(self):
        self.new_scanned_host = ScannedHost.objects.create(ip='192.168.1.1')

    def test_scannedhostdetail_data_foreign_key(self):
        new_shdetails_data = ScannedHostDetails.objects.create(
            port='8000',
            service = 'HTTP',
            scanned_host = self.new_scanned_host
        )
        self.assertEqual(new_shdetails_data.scanned_host, self.new_scanned_host)