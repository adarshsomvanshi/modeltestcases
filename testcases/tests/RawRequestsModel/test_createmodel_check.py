from django.test import TestCase
from testcases.models import *

class RawRequestModelTest(TestCase):
    def setUp(self):
        self.raw_request = RawRequests.objects.create(
            unique_id='12345',
            request='Sample request data',
            response='Sample response data'
        )

    def test_raw_request_creation(self):
        self.assertEqual(self.raw_request.unique_id, '12345')
        self.assertEqual(self.raw_request.request, 'Sample request data')
        self.assertEqual(self.raw_request.response, 'Sample response data')

    # def test_unique_id_uniqueness(self):
    #     RawRequests.objects.create(unique_id='12345')
    #     with self.assertRaises(Exception):
    #         RawRequests.objects.create(unique_id='12345')
        
    def test_unique_id_max_length(self):
            with self.assertRaises(Exception):
                RawRequests.objects.create(unique_id = 'a' * 51)  
