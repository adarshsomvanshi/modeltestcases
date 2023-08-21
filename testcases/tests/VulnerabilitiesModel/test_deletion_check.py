from django.test import TestCase
from testcases.models import *

class VulnerabilitiesModelTest(TestCase):
    def setUp(self):
        self.vul = {
            'unique_id':'CVE-2023-1234',
            'ip':'192.168.1.1',
            'port':80,
            'location':'Sample Location',
            'org':'Sample Org',
            'rule_id':'R123',
            'source':'Sample Source',
            'rule_severity':3,
            'rule_description':'Sample rule description',
            'rule_finding':'Sample rule finding',
            'info':'Additional info',
            'timestamp':'2023-08-10',
            'status':'Open',
            'assignee':'John Doe',
            'history':'Initial finding',
            'jira':'Additional Jira',
            'notes':'some additional notes',
            'creator':'Alice',
            'owner':'Bob',
            'vertical':'Sample Vertical',
            'service_owner':'Service Owner',
        }
        self.vul_unique_id = Vulnerabilities.objects.create(**self.vul)
    def test_user_deletion(self):
        self.assertTrue(Vulnerabilities.objects.filter(unique_id=self.vul['unique_id']).exists())
        self.vul_unique_id.delete()
        self.assertFalse(Vulnerabilities.objects.filter(unique_id=self.vul['unique_id']).exists())