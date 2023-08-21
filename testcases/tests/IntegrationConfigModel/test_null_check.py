from django.test import TestCase
from testcases.models import *

class IntegrationConfigModelTest(TestCase):

    def test_ic_null_type(self):
        new_ic = IntegrationConfig.objects.create(
            filters = {},
            config = {},
            extra={},
        )
        # self.assertEqual(new_ic.type, IntegrationConfig.NotificationTypes.NOTIFICATION)
        # self.assertEqual(new_ic.identifier, IntegrationConfig.SourceTypes.HTTPENDPOINT)
        self.assertIsNone(new_ic.org_name)
        self.assertIsNone(new_ic.description)