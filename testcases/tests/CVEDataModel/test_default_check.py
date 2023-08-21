import unittest
from django.test import TestCase
from testcases.models import *

class TestCVEDataModelTest(TestCase):
    def test_default_type_cvedata(self):
        new_cvedata = CVEData.objects.create(
            id='CVE-2097-56',
        )
        self.assertEqual(new_cvedata.description,"")
        self.assertEqual(new_cvedata.references,"")
        self.assertEqual(new_cvedata.phase,"")
        self.assertEqual(new_cvedata.votes,"")
        self.assertEqual(new_cvedata.comments,"")
        self.assertEqual(new_cvedata.added_by,"")
        #self.assertEqual(new_cvedata.status,"")   #this is for checking default value of status
        self.assertEqual(new_cvedata.status,"ENTRY")

# if __name__=='__main__':
#     unittest.main()