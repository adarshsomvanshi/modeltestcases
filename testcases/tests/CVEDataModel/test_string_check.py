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
    def test_string_representation(self):
        self.assertEqual(str(self.cve_data.id), self.cve_data.id)
        self.assertEqual(str(self.cve_data.status), self.cve_data.status)
        self.assertEqual(str(self.cve_data.description), self.cve_data.description)
        self.assertEqual(str(self.cve_data.references), self.cve_data.references)
        self.assertEqual(str(self.cve_data.phase), self.cve_data.phase)
        self.assertEqual(str(self.cve_data.votes), self.cve_data.votes)
        self.assertEqual(str(self.cve_data.comments), self.cve_data.comments)
        self.assertEqual(str(self.cve_data.added_by), self.cve_data.added_by)