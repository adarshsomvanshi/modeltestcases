from django.test import TestCase
from testcases.models import *

class IntegrationConfigModelTest(TestCase):
    def setUp(self):
        self.ic = IntegrationConfig.objects.create(
            type = IntegrationConfig.NotificationTypes.NOTIFICATION,
            identifier = IntegrationConfig.SourceTypes.HTTPENDPOINT,
            filters = {'severity': 'high'},
            config = {'url':'https://example.com/'},
            extra = {'param':'value1'},
            org_name = 'sample org',
            description = 'Sample description',
        )
    def test_ic_creation(self):
        self.assertEqual(self.ic.type,IntegrationConfig.NotificationTypes.NOTIFICATION)
        self.assertEqual(self.ic.identifier, IntegrationConfig.SourceTypes.HTTPENDPOINT)
        self.assertEqual(self.ic.filters, {'severity': 'high'})
        self.assertEqual(self.ic.config, {'url':'https://example.com/'})
        self.assertEqual(self.ic.extra ,{'param':'value1'})
        self.assertEqual(self.ic.org_name ,'sample org')
        self.assertEqual(self.ic.description, 'Sample description')