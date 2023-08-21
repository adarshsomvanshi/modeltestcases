from django.test import TestCase
from testcases.models import *

class GlobalConfigModelTest(TestCase):
    def setUp(self):
        self.gc = GlobalConfig.objects.create(
            setting = 'Max_Connections',
            value = '100',
            action = 'increase',
            extra = {'param1': 'value1'},
            description = 'Sample description'
        )
    
    def test_gc_creation(self):
        self.assertEqual(self.gc.setting,'Max_Connections')
        self.assertEqual(self.gc.value,'100')
        self.assertEqual(self.gc.action,'increase')
        self.assertEqual(self.gc.extra,{'param1': 'value1'})
        self.assertEqual(self.gc.description,'Sample description')
