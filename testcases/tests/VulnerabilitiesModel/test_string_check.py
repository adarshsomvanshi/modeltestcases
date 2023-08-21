from django.test import TestCase
from django.contrib.auth.models import User
from testcases.models import *


class VulnerabilitiesModelTest(TestCase):
    def setUp(self):
        self.vul = Vulnerabilities.objects.create(
            unique_id='CVE-2023-1234',
            ip='192.168.1.1',
            port=80,
            location='Sample Location',
            org='Sample Org',
            rule_id='R123',
            source='Sample Source',
            rule_severity=3,
            rule_description='Sample rule description',
            rule_finding='Sample rule finding',
            info='Additional info',
            timestamp='2023-08-10',
            status='Open',
            assignee='John Doe',
            history='Initial finding',
            jira='Additional Jira',
            notes='some additional notes',
            creator='Alice',
            owner='Bob',
            vertical='Sample Vertical',
            service_owner='Service Owner',
        )
    
    def test_str_representation(self):
        self.assertEqual(str(self.vul.unique_id), self.vul.unique_id)
        self.assertEqual(str(self.vul.ip), self.vul.ip)
        self.assertEqual(str(self.vul.location), self.vul.location)
        self.assertEqual(str(self.vul.org), self.vul.org)
        self.assertEqual(str(self.vul.rule_id), self.vul.rule_id)
        self.assertEqual(str(self.vul.source), self.vul.source)
        self.assertEqual(str(self.vul.rule_description), self.vul.rule_description)
        self.assertEqual(str(self.vul.rule_finding), self.vul.rule_finding)
        self.assertEqual(str(self.vul.info), self.vul.info)
        self.assertEqual(str(self.vul.history), self.vul.history)
        self.assertEqual(str(self.vul.jira), self.vul.jira)
        self.assertEqual(str(self.vul.notes), self.vul.notes)
        self.assertEqual(str(self.vul.status), self.vul.status)
        self.assertEqual(str(self.vul.assignee), self.vul.assignee)
        self.assertEqual(str(self.vul.creator), self.vul.creator)
        self.assertEqual(str(self.vul.owner), self.vul.owner)
        self.assertEqual(str(self.vul.vertical), self.vul.vertical)
        self.assertEqual(str(self.vul.service_owner), self.vul.service_owner)
        self.assertEqual(int(self.vul.port), self.vul.port)
        self.assertEqual(int(self.vul.rule_severity), self.vul.rule_severity)
