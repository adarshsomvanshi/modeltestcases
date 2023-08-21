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

    def test_string_representation(self):
            self.assertEqual(str(self.gc.setting), self.gc.setting)
            self.assertEqual(str(self.gc.value), self.gc.value)
            self.assertEqual(str(self.gc.action), self.gc.action)
            self.assertEqual(dict(self.gc.extra), self.gc.extra)
            self.assertEqual(str(self.gc.description), self.gc.description)
            # self.assertTrue(str(self.gc.action))
