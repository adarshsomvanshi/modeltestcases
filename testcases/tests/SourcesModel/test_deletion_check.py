from django.test import TestCase
from testcases.models import *

class SourceModelTest(TestCase):
    def setUp(self):
        self.src = {
            'source' :'192.168.1.1',
            'type' : Sources.SourceTypes.IP,
            'is_excluded' : False,
            'is_sensitive' : False,
            'included_rules' : 'Rule1, Rule 2',
            'exclude_rules' : 'Rule 3',
            'org_name' : 'Sample Organiztion',
            'description' : 'Sample description',
            'identifier' : 'ABC123',
        }
        self.source = Sources.objects.create(**self.src)

    def test_user_deletion(self):
        self.assertTrue(Sources.objects.filter(source=self.src['source']).exists())
        self.source.delete()
        self.assertFalse(Sources.objects.filter(source=self.src['source']).exists())