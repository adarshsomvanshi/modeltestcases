from django.test import TestCase
from testcases.models import *

#Checking for null value in these fields but it shows error.
class CVEDataModelTest(TestCase):
    def test_null_value(self):
        cve_data_new = CVEData.objects.create(
            id = 'CVE-2023-169'
        )
        # self.assertIsNone(cve_data_new.created_at)
        # self.assertIsNone(cve_data_new.updated_at)