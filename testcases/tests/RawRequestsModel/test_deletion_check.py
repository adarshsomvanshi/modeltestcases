from django.test import TestCase
from testcases.models import *

class RawRequestModelTest(TestCase):
    def setUp(self):
        self.raw_request = {
            'unique_id':'123456',
            'request':'Sample request data',
            'response':'Sample response data'
        }
        self.raw_unique_id = RawRequests.objects.create(**self.raw_request)
    
    def test_user_deletion(self):
        self.assertTrue(RawRequests.objects.filter(unique_id=self.raw_request['unique_id']).exists())
        self.raw_unique_id.delete()
        self.assertFalse(RawRequests.objects.filter(unique_id=self.raw_request['unique_id']).exists())
