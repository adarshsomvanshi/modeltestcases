from django.test import TestCase
from django.contrib.auth.models import User
from testcases.models import *


class VulnerabilitiesModelTest(TestCase):

    def test_vul_null_type(self):
        new_vul = Vulnerabilities.objects.create(
            unique_id="CVE-2023-12",
            ip='192.168.1.4',
            port=443,     # it cannot be null.
            # rule_id='R597',
            # location='Another Locations',
            # source='Another Sources',
            rule_severity=8,   #it cannot be null
            # history = ''     #For checking purpose put history value to empty string.
        )
        self.assertIsNone(new_vul.org)
        self.assertIsNone(new_vul.rule_description)
        self.assertIsNone(new_vul.rule_finding)
        self.assertIsNone(new_vul.info)
        self.assertIsNone(new_vul.timestamp)
        # self.assertEqual(new_vul.history, None)
        self.assertIsNone(new_vul.jira)
        self.assertIsNone(new_vul.notes)
        self.assertIsNone(new_vul.creator)
        self.assertIsNone(new_vul.owner)
        self.assertIsNone(new_vul.vertical)
        self.assertIsNone(new_vul.service_owner)