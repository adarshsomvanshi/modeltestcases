from django.test import TestCase
from testcases.models import *
from django.core.exceptions import ValidationError

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
    def test_src_creation(self):
        self.assertEqual(self.src.source, '192.168.1.1')
        self.assertEqual(self.src.type, Sources.SourceTypes.IP)
        self.assertFalse(self.src.is_excluded)
        self.assertFalse(self.src.is_sensitive)
        self.assertEqual(self.src.included_rules, 'Rule1, Rule 2')
        self.assertEqual(self.src.exclude_rules,'Rule 3')
        self.assertEqual(self.src.org_name,'Sample Organiztion')
        self.assertEqual(self.src.description,'Sample description')
        self.assertEqual(self.src.identifier,'ABC123')

    # def test_source_uniqueness(self):
    #     Sources.objects.create(source = '192.168.1.6')
    #     with self.assertRaises(Exception):
    #         Sources.objects.create(source = '192.168.1.6')

    def test_included_rules_exceeding_max_length(self):
        long_included_rules = 'a' * 65536
        with self.assertRaises(Exception):
            Sources.objects.create(included_rules = long_included_rules)

    def test_identifier_exceeding_max_length(self):
        long_identifier = 'a' * 256
        with self.assertRaises(Exception):
            Sources.objects.create(identifier=long_identifier)