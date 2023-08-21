from django.test import TestCase
from testcases.models import *

class CVEDataModelTest(TestCase):
    def setUp(self):
        self.cve_data = CVEData.objects.create(
            id="CVE-2023-1234",
            status="ENTRY",
            description="Sample description",
            references="Sample references",
            phase="Sample phase",
            votes="Sample votes",
            comments="Sample comments",
            added_by="Sample user"    #for checking purpose put integer instead of string
        )
    def test_cve_data_creation(self):
        self.assertTrue(isinstance(self.cve_data,CVEData))