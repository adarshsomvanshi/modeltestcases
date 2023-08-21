from django.test import TestCase
from testcases.models import *

class RawRequestModelTest(TestCase):

    def test_null_fields(self):
        new_raw_request = RawRequests.objects.create(
            unique_id='789',
            # request= '',
            # response=''
        )
        self.assertIsNone(new_raw_request.request)
        self.assertIsNone(new_raw_request.response)
