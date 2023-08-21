from django.test import TestCase
from testcases.models import *

class IntegrationConfigTestCase(TestCase):
    def setUp(self):
        self.config_data = {
            'type': IntegrationConfig.NotificationTypes.NOTIFICATION,
            'identifier': IntegrationConfig.SourceTypes.HTTPENDPOINT,
            'filters': {'key': 'value'},
            'config': {'key': 'value'},
            'extra': {'key': 'value'},
            'org_name': 'TestOrg',
            'description': 'Test description',
        }
        self.config = IntegrationConfig.objects.create(**self.config_data)

    def test_user_deletion(self):
        self.assertTrue(IntegrationConfig.objects.filter(org_name=self.config_data['org_name']).exists())
        self.config.delete()
        self.assertFalse(IntegrationConfig.objects.filter(org_name=self.config_data['org_name']).exists())
