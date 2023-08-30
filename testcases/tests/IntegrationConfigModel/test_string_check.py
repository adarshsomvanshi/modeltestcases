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

    def test_string_representation(self):
        self.assertEqual(str(self.ic.type), self.ic.type)
        self.assertEqual(str(self.ic.identifier), self.ic.identifier)
        self.assertEqual(dict(self.ic.filters), self.ic.filters)
        self.assertEqual(dict(self.ic.config), self.ic.config)
        self.assertEqual(dict(self.ic.extra) ,self.ic.extra)
        self.assertEqual(str(self.ic.org_name) ,self.ic.org_name)
        self.assertEqual(str(self.ic.description), self.ic.description)

