from django.test import TestCase
from testcases.models import *

class IntegrationConfigModelTest(TestCase):

    def test_ic_default_type(self):
        new_ic = IntegrationConfig.objects.create(
            org_name = 'Sample Org',
            description = 'Sample_Description',
        )
        self.assertEqual(new_ic.type, IntegrationConfig.NotificationTypes.NOTIFICATION)
        self.assertEqual(new_ic.identifier, IntegrationConfig.SourceTypes.HTTPENDPOINT)
        self.assertEqual(new_ic.filters, {})
        self.assertEqual(new_ic.config, {})
        self.assertEqual(new_ic.extra, {})
        # self.assertIsNone(new_ic.org_name)
        # self.assertIsNone(new_ic.description)