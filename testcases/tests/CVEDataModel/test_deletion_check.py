from django.test import TestCase
from testcases.models import *

class CVEDataModelTest(TestCase):
    def setUp(self):
        self.cve_data = {
            'id': 'CVE-2023-1234',
            'status': 'ENTRY',
            'description': 'A test description.',
            'references': 'Test references.',
            'phase': 'Test phase.',
            'votes': 'Test votes.',
            'comments': 'Test comments.',
            'added_by': 'TestUser',
        }
        self.user = CVEData.objects.create(**self.cve_data)
    def test_user_deletion(self):
        # Ensure the user exists before deletion
        self.assertTrue(CVEData.objects.filter(id=self.cve_data['id']).exists())

        # Delete the user
        self.user.delete()

        # Ensure the user no longer exists after deletion
        self.assertFalse(CVEData.objects.filter(id=self.cve_data['id']).exists())