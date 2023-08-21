from django.test import TestCase
from testcases.models import *

class SourceModelTest(TestCase):
    def setUp(self):
        self.src = Sources.objects.create(
            source ='192.168.1.1',
            type = Sources.SourceTypes.IP,
            is_excluded = False,
            is_sensitive = False,
            included_rules = 'Rule1, Rule 2',
            exclude_rules = 'Rule 3',
            org_name = 'Sample Organiztion',
            description = 'Sample description',
            identifier = 'ABC123',
        )
    def test_string_representation(self):
        self.assertEqual(str(self.src.source), self.src.source)
        self.assertEqual(str(self.src.type), self.src.type)
        self.assertEqual(bool(self.src.is_excluded), self.src.is_excluded)
        self.assertEqual(bool(self.src.is_sensitive), self.src.is_sensitive)
        self.assertEqual(str(self.src.included_rules), self.src.included_rules)
        self.assertEqual(str(self.src.exclude_rules),self.src.exclude_rules)
        self.assertEqual(str(self.src.org_name),self.src.org_name)
        self.assertEqual(str(self.src.description),self.src.description)
        self.assertEqual(str(self.src.identifier),self.src.identifier)