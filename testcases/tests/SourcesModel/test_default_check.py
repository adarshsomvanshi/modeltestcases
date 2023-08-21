from django.test import TestCase
from testcases.models import *

class SourceModelTest(TestCase):
    def test_src_default_type(self):
        new_src = Sources.objects.create(
            source='hostname.example.com',
            # is_excluded=True,
        )
        self.assertEqual(new_src.type, Sources.SourceTypes.IP)
        self.assertFalse(new_src.is_excluded)
        self.assertFalse(new_src.is_sensitive)