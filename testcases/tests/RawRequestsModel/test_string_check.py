from django.test import TestCase
from django.contrib.auth.models import User
from testcases.models import *

class RawRequestModelTest(TestCase):
    def setUp(self):
        self.raw_request = RawRequests.objects.create(
            unique_id='123456',
            request='Sample request data',
            response='Sample response data'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.raw_request.unique_id), self.raw_request.unique_id)
        self.assertEqual(str(self.raw_request.request), self.raw_request.request)
        self.assertEqual(str(self.raw_request.response), self.raw_request.response)