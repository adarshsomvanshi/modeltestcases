from django.test import TestCase
from django.contrib.auth.models import User
from testcases.models import *

class VulnerabilitiesModelTest(TestCase):

    def test_default_status(self):
            new_vulnerability = Vulnerabilities.objects.create(
                unique_id='CVE-2023-5678',
                ip='192.168.1.2',
                port=443,
                location='Another Location',
                org='Another Org',
                rule_id='R567',
                source='Another Source',
                rule_severity=2,
                rule_description='Another rule description',
                rule_finding='Another rule finding',
                info='Additional info',
                timestamp='2023-08-11',
                # history = None      #for checking purpose set history is none.
            )
            self.assertEqual(new_vulnerability.status, 'Open')
            self.assertEqual(new_vulnerability.assignee, 'Unassigned')
            self.assertEqual(new_vulnerability.history, '')