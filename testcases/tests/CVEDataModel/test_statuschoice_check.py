from django.test import TestCase
from testcases.models import *

class CVEDataModelTest(TestCase):

    def test_cvedata_default_status_choices(self):
            status_field = CVEData._meta.get_field('status')
            choices = status_field.choices
            valid_choices = [choice[0] for choice in choices]    #Mapping Function is used.

            for choice in valid_choices:
                cve_data= CVEData.objects.create(
                    id='CVE-2034-1979'+ choice,
                    status= choice,
                    description="Sample description",
                    references="Sample references",
                    phase="Sample phase",
                    votes="Sample votes",
                    comments="Sample comments",
                    added_by="Sample user"
                )
                self.assertEqual(cve_data.status, choice)