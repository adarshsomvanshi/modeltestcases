from django.test import TestCase
from testcases.models import *

class SourceModelTest(TestCase):
    def test_src_null_type(self):
        new_src = Sources.objects.create(
            source = 'hostname.exapmple.com',
            type = Sources.SourceTypes.IP,
            is_excluded = False,
            is_sensitive = False
        )
        # self.assertIsNotNone(new_src.source)
        self.assertIsNone(new_src.included_rules)
        self.assertIsNone(new_src.exclude_rules)
        self.assertIsNone(new_src.org_name)
        self.assertIsNone(new_src.description)
        self.assertIsNone(new_src.identifier)
