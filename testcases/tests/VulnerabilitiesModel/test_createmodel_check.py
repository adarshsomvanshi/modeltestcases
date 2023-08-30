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
            status='Openashdlashfalhfdfhodifhaoide',
            assignee='John Doe',
            history='Initial finding',
            jira='Additional Jira',
            notes='some additional notes',
            creator='Alice',
            owner='Bob',
            vertical='Sample Vertical',
            service_owner='Service Owner',
        )
    def test_vulnerabilities_creation(self):
        self.assertEqual(self.vul.unique_id, 'CVE-2023-1234')
        self.assertEqual(self.vul.ip,'192.168.1.1')
        self.assertEqual(self.vul.port,80)
        self.assertEqual(self.vul.location,"Sample Location")
        self.assertEqual(self.vul.org,"Sample Org")
        self.assertEqual(self.vul.rule_id,"R123")
        self.assertEqual(self.vul.source,"Sample Source")
        self.assertEqual(self.vul.rule_severity,3)
        self.assertEqual(self.vul.rule_description,"Sample rule description")
        self.assertEqual(self.vul.rule_finding,"Sample rule finding")
        self.assertEqual(self.vul.info,"Additional info")
        self.assertEqual(str(self.vul.timestamp),"2023-08-10")
        self.assertEqual(self.vul.status,"Openashdlashfalhfdfhodifhaoide")
        self.assertEqual(self.vul.assignee,"John Doe")
        self.assertEqual(self.vul.history,"Initial finding")
        self.assertEqual(self.vul.jira,"Additional Jira")
        self.assertEqual(self.vul.notes,"some additional notes")
        self.assertEqual(self.vul.creator,"Alice")
        self.assertEqual(self.vul.owner,"Bob")
        self.assertEqual(self.vul.vertical,"Sample Vertical")
        self.assertEqual(self.vul.service_owner,"Service Owner")


    # def test_unique_id_uniqueness(self):
    #     Vulnerabilities.objects.create(unique_id = 'CVE-2023-1234',rule_severity=4,port=800)
    #     with self.assertRaises(Exception):
    #         Vulnerabilities.objects.create(unique_id = 'CVE-2023-1234',rule_severity=24,port=80)

    def test_unique_id_length(self):
        with self.assertRaises(Exception):
            Vulnerabilities.objects.create(unique_id = 'a' * 51)
    
    def test_status_length(self):
        with self.assertRaises(Exception):
            Vulnerabilities.objects.create(status = 'a'*31)

    def test_assignee_length(self):
        with self.assertRaises(Exception):
            Vulnerabilities.objects.create(assignee = 'a'*101)
