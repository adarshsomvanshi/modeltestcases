from django.test import TestCase
from testcases.models import *

class GlobalConfigTestCase(TestCase):
    def setUp(self):
        self.config_data = {
            'setting': 'test_setting',
            'value': 'test_value',
            'action': 'test_action',
            'extra': {'key': 'value'},
            'description': 'Test description',
        }
        self.config = GlobalConfig.objects.create(**self.config_data)

    def test_user_deletion(self):
        self.assertTrue(GlobalConfig.objects.filter(setting= self.config_data['setting']).exists())
        self.config.delete()
        self.assertFalse(GlobalConfig.objects.filter(setting= self.config_data['setting']).exists())