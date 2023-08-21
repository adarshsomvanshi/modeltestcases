from django.test import TestCase
from testcases.models import *

class GlobalConfigModelTest(TestCase):
    
    def test_gc_default_type(self):
        new_gc = GlobalConfig.objects.create(
            setting = 'TIMEOUT',
        )
        self.assertIsNone(new_gc.value)
        self.assertIsNone(new_gc.action)
        self.assertIsNone(new_gc.description)
        self.assertEqual(new_gc.extra, {})