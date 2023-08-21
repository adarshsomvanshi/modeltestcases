from django.test import TestCase
from testcases.models import *

class SourceModelTest(TestCase):
    def test_valid_sources_type(self):
        valid_choices = [choice[0] for choice in Sources.SourceTypes.choices ]
        src_instance = Sources.objects.create(type=valid_choices[0])
        self.assertIn(src_instance.type, valid_choices)