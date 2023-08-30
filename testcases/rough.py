# from django.test import TestCase
# from .models import ScannedHost, ScannedHostDetails

# class ScannedHostDetailsModelTestCase(TestCase):
#     def setUp(self):
#         self.scanned_host = ScannedHost.objects.create(ip='192.168.1.1')
#         self.host_details_data = {
#             'scanned_host': self.scanned_host,
#             'port': '80',
#             'service': 'HTTP',
#             'version': '1.0',
#             'additional_data': {'key': 'value'}
#         }

#         self.host_details = ScannedHostDetails.objects.create(**self.host_details_data)

#     def test_host_details_creation(self):
#         """Test that a ScannedHostDetails instance was created correctly."""
#         for field, value in self.host_details_data.items():
#             self.assertEqual(getattr(self.host_details, field), value)

#     def test_default_service_value(self):
#         """Test that the service field defaults to 'Unknown'."""
#         new_host_details = ScannedHostDetails.objects.create(
#             scanned_host=self.scanned_host,
#             port='443'
#         )
#         self.assertEqual(new_host_details.service, 'Unknown')

#     def test_nullable_version_field(self):
#         """Test that the version field can be NULL."""
#         host_details_without_version = ScannedHostDetails.objects.create(
#             scanned_host=self.scanned_host,
#             port='22',
#             service='SSH'
#         )
#         self.assertIsNone(host_details_without_version.version)

#     def test_str_representation(self):
#         """Test the string representation of the ScannedHostDetails."""
#         expected_str = f'ScannedHostDetails {self.scanned_host.ip} - Port 80'
#         self.assertEqual(str(self.host_details), expected_str)

#     def test_additional_data(self):
#         """Test that additional_data field can store JSON data."""
#         additional_data = {'key1': 'value1', 'key2': 'value2'}
#         new_host_details = ScannedHostDetails.objects.create(
#             scanned_host=self.scanned_host,
#             port='8080',
#             service='Custom',
#             additional_data=additional_data
#         )
#         self.assertEqual(new_host_details.additional_data, additional_data)

# from django.test import TestCase
# from .models import MSFHistory

# class MSFHistoryModelTestCase(TestCase):
#     def setUp(self):
#         self.history_data = {
#             'command': 'exploit/windows/smb/ms17_010_eternalblue',
#             'job_id': '123456789',
#             'user': 'admin',
#             'status': True,
#             'output': 'Exploit completed successfully',
#             'type': 'exploit',
#             'failed': False
#         }

#         self.history_entry = MSFHistory.objects.create(**self.history_data)

#     def test_history_creation(self):
#         """Test that an MSFHistory instance was created correctly."""
#         for field, value in self.history_data.items():
#             self.assertEqual(getattr(self.history_entry, field), value)

#     def test_default_output_value(self):
#         """Test that the output field defaults to an empty string."""
#         new_history_entry = MSFHistory.objects.create(
#             command='post/multi/manage/shell_to_meterpreter',
#             job_id='987654321',
#             user='user1',
#             status=False,
#             type='post'
#         )
#         self.assertEqual(new_history_entry.output, '')

#     def test_nullable_type_field(self):
#         """Test that the type field can be NULL."""
#         history_entry_without_type = MSFHistory.objects.create(
#             command='use auxiliary/scanner/smb/smb_version',
#             job_id='246813579',
#             user='user2',
#             status=True,
#             output='Scanning completed',
#             failed=False
#         )
#         self.assertIsNone(history_entry_without_type.type)

#     def test_str_representation(self):
#         """Test the string representation of the MSFHistory."""
#         expected_str = f'MSFHistory - Job ID: {self.history_data["job_id"]}'
#         self.assertEqual(str(self.history_entry), expected_str)

#     def test_failed_status(self):
#         """Test that the failed field defaults to False."""
#         new_history_entry = MSFHistory.objects.create(
#             command='use auxiliary/scanner/http/joomla_http_header',
#             job_id='135792468',
#             user='user3',
#             status=True,
#             output='Scan completed',
#             type='auxiliary'
#         )
#         self.assertFalse(new_history_entry.failed)

# from django.test import TestCase
# from .models import ScannedHost

# class ScannedHostModelTestCase(TestCase):
#     def test_create_with_ip_only(self):
#         """Test that a ScannedHost instance can be created with only the 'ip' field."""
#         ip = '192.168.1.1'
#         scanned_host = ScannedHost.objects.create(ip=ip)

#         self.assertEqual(scanned_host.ip, ip)
#         self.assertIsNone(scanned_host.ipv6)
#         self.assertIsNone(scanned_host.mac)
#         self.assertIsNone(scanned_host.hostname)
#         self.assertIsNone(scanned_host.vendor)
#         self.assertIsNone(scanned_host.os)
#         self.assertIsNone(scanned_host.device_type)
#         self.assertFalse(scanned_host.status)

#     def test_create_with_ip_and_status(self):
#         """Test that a ScannedHost instance can be created with 'ip' and 'status' fields."""
#         ip = '192.168.1.2'
#         status = True
#         scanned_host = ScannedHost.objects.create(ip=ip, status=status)

#         self.assertEqual(scanned_host.ip, ip)
#         self.assertIsNone(scanned_host.ipv6)
#         self.assertIsNone(scanned_host.mac)
#         self.assertIsNone(scanned_host.hostname)
#         self.assertIsNone(scanned_host.vendor)
#         self.assertIsNone(scanned_host.os)
#         self.assertIsNone(scanned_host.device_type)
#         self.assertEqual(scanned_host.status, status)

# import os
# from django.test import TestCase
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.conf import settings
# from your_app.models import CVEData, UploadedFile

# class CVEDataModelTestCase(TestCase):

#     def setUp(self):
#         self.cve_data = CVEData.objects.create(
#             id="CVE-2023-1234",
#             status="ENTRY",
#             description="Sample description",
#             references="Sample references",
#             phase="Sample phase",
#             votes="Sample votes",
#             comments="Sample comments",
#             added_by="Sample user"
#         )

#     def test_cve_data_creation(self):
#         self.assertTrue(isinstance(self.cve_data, CVEData))
#         self.assertEqual(str(self.cve_data), self.cve_data.id)

#     def test_status_choices(self):
#         valid_choices = dict(CVEData.STATUS_CHOICES)
#         self.assertIn(self.cve_data.status, valid_choices.keys())

# class UploadedFileModelTestCase(TestCase):

#     def setUp(self):
#         self.uploaded_file = SimpleUploadedFile(
#             "test_file.txt",
#             b"file_content",
#             content_type="text/plain"
#         )
#         self.uploaded_file_instance = UploadedFile.objects.create(
#             file=self.uploaded_file,
#             filename="test_file.txt",
#             user="Sample user"
#         )

#     def tearDown(self):
#         self.uploaded_file_instance.delete()

#     def test_uploaded_file_creation(self):
#         self.assertTrue(isinstance(self.uploaded_file_instance, UploadedFile))
#         self.assertEqual(str(self.uploaded_file_instance), self.uploaded_file_instance.filename)

#     def test_file_deletion(self):
#         file_path = os.path.join(settings.MEDIA_ROOT, self.uploaded_file_instance.file.name)
#         self.assertTrue(os.path.exists(file_path))
#         self.uploaded_file_instance.delete()
#         self.assertFalse(os.path.exists(file_path))

# if __name__ == '__main__':
#     unittest.main()

# from django.test import TestCase
# from your_app.models import PortService, MSFHistory

# class PortServiceTestCase(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         # Create a sample MSFHistory instance for the ForeignKey
#         cls.msf_history = MSFHistory.objects.create(job_id=1, other_field="Sample data")

#     def test_port_service_creation(self):
#         port_service = PortService.objects.create(
#             port=8080,
#             port_status=True,
#             service="HTTP",
#             job=self.msf_history
#         )
#         self.assertTrue(isinstance(port_service, PortService))
#         self.assertEqual(port_service.__str__(), f"Port: {port_service.port}, Service: {port_service.service}")

#     def test_port_service_default_status(self):
#         port_service = PortService.objects.create(
#             port=22,
#             service="SSH",
#             job=self.msf_history
#         )
#         self.assertTrue(port_service.port_status)

#     def test_port_service_foreign_key(self):
#         port_service = PortService.objects.create(
#             port=3306,
#             port_status=False,
#             service="MySQL",
#             job=self.msf_history
#         )
#         self.assertEqual(port_service.job, self.msf_history)

#     # Add more test cases as needed

# if __name__ == '__main__':
#     unittest.main()


# from django.test import TestCase
# from your_app.models import CVEData

# class CVEDataModelTestCase(TestCase):

#     def test_cve_data_creation(self):
#         cve_data = CVEData.objects.create(
#             id="CVE-2023-1234",
#             status="ENTRY",
#             description="Sample description",
#             references="Sample references",
#             phase="Sample phase",
#             votes="Sample votes",
#             comments="Sample comments",
#             added_by="Sample user"
#         )
#         self.assertTrue(isinstance(cve_data, CVEData))
#         self.assertEqual(cve_data.__str__(), "CVE-2023-1234")

#     def test_default_status(self):
#         cve_data = CVEData.objects.create(
#             id="CVE-2023-5678",
#             description="Another sample description"
#         )
#         self.assertEqual(cve_data.status, "ENTRY")

#     def test_status_choices(self):
#         cve_data = CVEData.objects.create(
#             id="CVE-2023-9999",
#             status="CANDIDATE",
#             description="Yet another description"
#         )
#         valid_choices = dict(CVEData.STATUS_CHOICES)
#         self.assertIn(cve_data.status, valid_choices.keys())

# if __name__ == '__main__':
#     unittest.main()



# status_field = CVEData._meta.get_field('status')
# choices = status_field.choices

# # Create a list of valid choice values
# valid_choices = [choice[0] for choice in choices]

# from django.test import TestCase
# from your_app.models import CVEData

# class CVEDataModelTestCase(TestCase):

#     def test_status_choices(self):
#         valid_choices = [choice[0] for choice in CVEData._meta.get_field('status').choices]
#         for choice in valid_choices:
#             cve_data = CVEData.objects.create(
#                 id=f"CVE-2023-{choice}",
#                 status=choice,
#                 description="Sample description",
#                 references="Sample references",
#                 phase="Sample phase",
#                 votes="Sample votes",
#                 comments="Sample comments",
#                 added_by="Sample user"
#             )
#             self.assertEqual(cve_data.status, choice)

# if __name__ == '__main__':
#     unittest.main()

# # class VulnerabilitiesModelTest(TestCase):
# #     def test_Vul(self):
# #         unique_id='CVE-2023-1234'
# #         ip='192.168.1.1'
# #         port=80
# #         location='Sample Location'
# #         org='Sample Org'
# #         rule_id='R123'
# #         source='Sample Source'
# #         rule_severity=3
# #         rule_description='Sample rule description'
# #         rule_finding='Sample rule finding'
# #         info='Additional info'
# #         timestamp='2023-08-10'
# #         status='Open'
# #         assignee='John Doe'
# #         history='Initial finding'
# #         creator='Alice'
# #         owner='Bob'
# #         vertical='Sample Vertical'
# #         service_owner='Service Owner'

# #         Vul = Vulnerabilities.objects.create(
# #             unique_id=unique_id,
# #             ip=ip,
# #             port=port,
# #             location=location,
# #             org=org,
# #             rule_id=rule_id,
# #             source=source,
# #             rule_severity=rule_severity,
# #             rule_description=rule_description,
# #             rule_finding=rule_finding,
# #             info=info,
# #             timestamp=timestamp,
# #             status=status,
# #             assignee=assignee,
# #             history=history,
# #             creator=creator,
# #             owner=owner,
# #             vertical = vertical,
# #             service_owner=service_owner,
# #         )
# #         self.assertEqual(Vul.unique_id, unique_id)
# #         self.assertEqual(Vul.ip, ip)
# #         self.assertEqual(Vul.unique_id, unique_id)
# #         self.assertEqual(Vul.port, port)
# #         self.assertEqual(Vul.location, location)
# #         self.assertEqual(Vul.org, org)
# #         self.assertEqual(Vul.rule_id, rule_id)
# #         self.assertEqual(Vul.source, source)
# #         self.assertEqual(Vul.rule_severity, rule_severity)
# #         self.assertEqual(Vul.rule_description, rule_description)
# #         self.assertEqual(Vul.rule_finding, rule_finding)
# #         self.assertEqual(Vul.info, info)
# #         self.assertEqual(Vul.timestamp, timestamp)
# #         self.assertEqual(Vul.status, status)
# #         self.assertEqual(Vul.assignee, assignee)
# #         self.assertEqual(Vul.history, history)
# #         self.assertEqual(Vul.creator, creator)
# #         self.assertEqual(Vul.owner, owner)
# #         self.assertEqual(Vul.vertical, vertical)
# #         self.assertEqual(Vul.service_owner, service_owner)

#     # def test_Src(self):
#     #     source = ''
#     #     type = ''
#     #     is_excluded = False
#     #     is_sensitive = False
#     #     included_rules = ''
#     #     exclude_rules = ''
#     #     org_name = ''
#     #     description = ''
#     #     identifier = ''
#     #     created_at = ''
#     #     updated_at = ''

#     #     Src = Sources.objects.create(
#     #         source = source,
#     #         type = type,
#     #         is_excluded = is_excluded,
#     #         is_sensitive = is_sensitive,
#     #         included_rules = included_rules,
#     #         exclude_rules = exclude_rules,
#     #         org_name = org_name,
#     #         description = description,
#     #         identifier = identifier,
#     #         created_at=created_at,
#     #         updated_at=updated_at
#     #     )
#     #     self.assertEqual(Src.source, source)
#     #     self.assertEqual(Src.type, type)
#     #     self.assertFalse(Src.is_excluded)
#     #     self.assertFalse(Src.is_sensitive)
#     #     self.assertEqual(Src.included_rules, included_rules)
#     #     self.assertEqual(Src.exclude_rules, exclude_rules)
#     #     self.assertEqual(Src.org_name, org_name)
#     #     self.assertEqual(Src.description, description)
#     #     self.assertEqual(Src.identifier, identifier)
#     #     # self.assertEqual(Src.created_at,'')
#     #     # self.assertEqual(Src.updated_at,'')

# from django.test import TestCase
# from .models import Vulnerabilities

# class VulnerabilitiesModelTestCase(TestCase):
#     def setUp(self):
#         # Create a test vulnerability instance
#         self.vulnerability = Vulnerabilities.objects.create(
#             unique_id='CVE-2023-1234',
#             ip='192.168.1.1',
#             port=80,
#             location='Sample Location',
#             org='Sample Org',
#             rule_id='R123',
#             source='Sample Source',
#             rule_severity=3,
#             rule_description='Sample rule description',
#             rule_finding='Sample rule finding',
#             info='Additional info',
#             timestamp='2023-08-10',
#             status='Open',
#             assignee='John Doe',
#             history='Initial finding',
#             creator='Alice',
#             owner='Bob',
#             vertical='Sample Vertical',
#             service_owner='Service Owner',
#         )

#     def test_vulnerability_creation(self):
#         """Test that a vulnerability was created correctly."""
#         self.assertEqual(self.vulnerability.unique_id, 'CVE-2023-1234')
#         self.assertEqual(self.vulnerability.ip, '192.168.1.1')
#         self.assertEqual(self.vulnerability.port, 80)
#         self.assertEqual(self.vulnerability.location, 'Sample Location')
#         self.assertEqual(self.vulnerability.org, 'Sample Org')
#         self.assertEqual(self.vulnerability.rule_id, 'R123')
#         self.assertEqual(self.vulnerability.source, 'Sample Source')
#         self.assertEqual(self.vulnerability.rule_severity, 3)
#         self.assertEqual(self.vulnerability.rule_description, 'Sample rule description')
#         self.assertEqual(self.vulnerability.rule_finding, 'Sample rule finding')
#         self.assertEqual(self.vulnerability.info, 'Additional info')
#         self.assertEqual(str(self.vulnerability.timestamp), '2023-08-10')
#         self.assertEqual(self.vulnerability.status, 'Open')
#         self.assertEqual(self.vulnerability.assignee, 'John Doe')
#         self.assertEqual(self.vulnerability.history, 'Initial finding')
#         self.assertEqual(self.vulnerability.creator, 'Alice')
#         self.assertEqual(self.vulnerability.owner, 'Bob')
#         self.assertEqual(self.vulnerability.vertical, 'Sample Vertical')
#         self.assertEqual(self.vulnerability.service_owner, 'Service Owner')

#     def test_default_status(self):
#         """Test that status defaults to 'Open'."""
#         new_vulnerability = Vulnerabilities.objects.create(
#             unique_id='CVE-2023-5678',
#             ip='192.168.1.2',
#             port=443,
#             location='Another Location',
#             org='Another Org',
#             rule_id='R567',
#             source='Another Source',
#             rule_severity=2,
#             rule_description='Another rule description',
#             rule_finding='Another rule finding',
#             info='Additional info',
#             timestamp='2023-08-11',
#         )
#         self.assertEqual(new_vulnerability.status, 'Open')

#     def test_updated_timestamp(self):
#         """Test that updated_at field is updated on modification."""
#         initial_updated_at = self.vulnerability.updated_at
#         self.vulnerability.assignee = 'Jane Doe'
#         self.vulnerability.save()
#         updated_vulnerability = Vulnerabilities.objects.get(id=self.vulnerability.id)
#         self.assertNotEqual(updated_vulnerability.updated_at, initial_updated_at)


# from django.test import TestCase
# from .models import Sources

# class SourcesModelTestCase(TestCase):
#     def setUp(self):
#         # Create a test source instance
#         self.source = Sources.objects.create(
#             source='192.168.1.1',
#             type=Sources.SourceTypes.IP,
#             is_excluded=False,
#             is_sensitive=True,
#             included_rules='Rule1, Rule2',
#             exclude_rules='Rule3',
#             org_name='Sample Org',
#             description='Sample Description',
#             identifier='ABC123'
#         )

#     def test_source_creation(self):
#         """Test that a source was created correctly."""
#         self.assertEqual(self.source.source, '192.168.1.1')
#         self.assertEqual(self.source.type, Sources.SourceTypes.IP)
#         self.assertFalse(self.source.is_excluded)
#         self.assertTrue(self.source.is_sensitive)
#         self.assertEqual(self.source.included_rules, 'Rule1, Rule2')
#         self.assertEqual(self.source.exclude_rules, 'Rule3')
#         self.assertEqual(self.source.org_name, 'Sample Org')
#         self.assertEqual(self.source.description, 'Sample Description')
#         self.assertEqual(self.source.identifier, 'ABC123')

#     def test_default_type(self):
#         """Test that type defaults to SourceTypes.IP."""
#         new_source = Sources.objects.create(
#             source='hostname.example.com',
#             is_excluded=True,
#         )
#         self.assertEqual(new_source.type, Sources.SourceTypes.IP)

#     def test_updated_timestamp(self):
#         """Test that updated_at field is updated on modification."""
#         initial_updated_at = self.source.updated_at
#         self.source.org_name = 'Updated Org'
#         self.source.save()
#         updated_source = Sources.objects.get(id=self.source.id)
#         self.assertNotEqual(updated_source.updated_at, initial_updated_at)

#     def test_str_representation(self):
#         """Test the string representation of the source."""
#         self.assertEqual(str(self.source), '192.168.1.1')

# from django.test import TestCase
# from your_app.models import Sources

# class SourcesModelTestCase(TestCase):

#     def test_source_types_choices(self):
#         # Get the valid choices for the source_type field
#         valid_choices = [choice[0] for choice in Sources.SourceTypes.choices]

#         # Create a Source instance with a valid source_type
#         source = Sources.objects.create(source_type=valid_choices[0], other_field="Sample data")

#         # Check that the created source instance has a valid source_type
#         self.assertIn(source.source_type, valid_choices)

# if __name__ == '__main__':
#     unittest.main()


    # def test_source_types_choices(self):
    #     """Test that the source type field uses valid choices."""
    #     choices = [choice[0] for choice in Sources.SourceTypes.choices]
    #     self.assertIn(self.source.type, choices)

# from django.test import TestCase
# from .models import IntegrationConfig

# class IntegrationConfigModelTestCase(TestCase):
#     def setUp(self):
#         # Create a test IntegrationConfig instance
#         self.integration_config = IntegrationConfig.objects.create(
#             type=IntegrationConfig.NotificationTypes.NOTIFICATION,
#             identifier=IntegrationConfig.SourceTypes.HTTPENDPOINT,
#             filters={'severity': 'high'},
#             config={'url': 'https://example.com/webhook'},
#             extra={'param1': 'value1'},
#             org_name='Sample Org',
#             description='Sample Description'
#         )

#     def test_integration_config_creation(self):
#         """Test that an IntegrationConfig was created correctly."""
#         self.assertEqual(self.integration_config.type, IntegrationConfig.NotificationTypes.NOTIFICATION)
#         self.assertEqual(self.integration_config.identifier, IntegrationConfig.SourceTypes.HTTPENDPOINT)
#         self.assertEqual(self.integration_config.filters, {'severity': 'high'})
#         self.assertEqual(self.integration_config.config, {'url': 'https://example.com/webhook'})
#         self.assertEqual(self.integration_config.extra, {'param1': 'value1'})
#         self.assertEqual(self.integration_config.org_name, 'Sample Org')
#         self.assertEqual(self.integration_config.description, 'Sample Description')

#     def test_default_values(self):
#         """Test default values for type and identifier."""
#         new_integration_config = IntegrationConfig.objects.create(
#             filters={},
#             config={},
#             extra={},
#             org_name='Another Org'
#         )
#         self.assertEqual(new_integration_config.type, IntegrationConfig.NotificationTypes.NOTIFICATION)
#         self.assertEqual(new_integration_config.identifier, IntegrationConfig.SourceTypes.HTTPENDPOINT)

#     def test_updated_timestamp(self):
#         """Test that updated_at field is updated on modification."""
#         initial_updated_at = self.integration_config.updated_at
#         self.integration_config.description = 'Updated Description'
#         self.integration_config.save()
#         updated_integration_config = IntegrationConfig.objects.get(id=self.integration_config.id)
#         self.assertNotEqual(updated_integration_config.updated_at, initial_updated_at)

#     def test_str_representation(self):
#         """Test the string representation of the IntegrationConfig."""
#         self.assertEqual(str(self.integration_config), 'IntegrationConfig HTTPENDPOINT Sample Org')

# from django.test import TestCase
# from .models import GlobalConfig

# class GlobalConfigModelTestCase(TestCase):
#     def setUp(self):
#         # Create a test GlobalConfig instance
#         self.global_config = GlobalConfig.objects.create(
#             setting='MAX_CONNECTIONS',
#             value='100',
#             action='increase',
#             extra={'param1': 'value1'},
#             description='Sample Description'
#         )

#     def test_global_config_creation(self):
#         """Test that a GlobalConfig was created correctly."""
#         self.assertEqual(self.global_config.setting, 'MAX_CONNECTIONS')
#         self.assertEqual(self.global_config.value, '100')
#         self.assertEqual(self.global_config.action, 'increase')
#         self.assertEqual(self.global_config.extra, {'param1': 'value1'})
#         self.assertEqual(self.global_config.description, 'Sample Description')

#     def test_default_blank_fields(self):
#         """Test that blank fields are stored as None."""
#         new_global_config = GlobalConfig.objects.create(
#             setting='TIMEOUT',
#             value='',
#             extra={}
#         )
#         self.assertIsNone(new_global_config.value)

#     def test_updated_timestamp(self):
#         """Test that updated_at field is updated on modification."""
#         initial_updated_at = self.global_config.updated_at
#         self.global_config.value = '200'
#         self.global_config.save()
#         updated_global_config = GlobalConfig.objects.get(id=self.global_config.id)
#         self.assertNotEqual(updated_global_config.updated_at, initial_updated_at)

#     def test_str_representation(self):
#         """Test the string representation of the GlobalConfig."""
#         self.assertEqual(str(self.global_config), 'GlobalConfig MAX_CONNECTIONS')

#     def test_default_created_at(self):
#         """Test that created_at is automatically set on creation."""
#         new_global_config = GlobalConfig.objects.create(
#             setting='LOG_LEVEL',
#             value='DEBUG'
#         )
#         self.assertIsNotNone(new_global_config.created_at)

# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import UserSetting

# class UserSettingModelTestCase(TestCase):
#     @staticmethod
#     def _createHash():
#         # Implement your hash creation logic here for testing purposes
#         return 'sample_api_key'

#     def setUp(self):
#         # Create a test User instance
#         self.user = User.objects.create_user(
#             username='testuser',
#             password='testpassword'
#         )

#         # Create a test UserSetting instance
#         self.user_setting = UserSetting.objects.create(
#             user=self.user,
#             company='Sample Company',
#             license_exists='Yes',
#             role='Admin',
#             api_key=self._createHash()
#         )

#     def test_user_setting_creation(self):
#         """Test that a UserSetting was created correctly."""
#         self.assertEqual(self.user_setting.user, self.user)
#         self.assertEqual(self.user_setting.company, 'Sample Company')
#         self.assertEqual(self.user_setting.license_exists, 'Yes')
#         self.assertEqual(self.user_setting.role, 'Admin')

#     def test_api_key_uniqueness(self):
#         """Test that api_key field is unique."""
#         with self.assertRaises(ValueError):
#             UserSetting.objects.create(
#                 user=self.user,
#                 company='Another Company',
#                 license_exists='No',
#                 role='User',
#                 api_key=self.user_setting.api_key
#             )

#     def test_api_key_generation(self):
#         """Test that api_key is generated using _createHash method."""
#         self.assertEqual(self.user_setting.api_key, 'sample_api_key')

#     def test_str_representation(self):
#         """Test the string representation of the UserSetting."""
#         self.assertEqual(str(self.user_setting), 'UserSetting for testuser')

#     def test_default_blank_fields(self):
#         """Test that blank fields are stored as None."""
#         new_user_setting = UserSetting.objects.create(
#             user=self.user,
#             company='',
#             license_exists='',
#             role=''
#         )
#         self.assertIsNone(new_user_setting.company)
#         self.assertIsNone(new_user_setting.license_exists)
#         self.assertIsNone(new_user_setting.role)

# from django.test import TestCase
# from .models import ScannedHost

# class ScannedHostModelTestCase(TestCase):
#     def setUp(self):
#         self.host_data = {
#             'ip': '192.168.1.1',
#             'ipv6': '2001:db8::1',
#             'mac': '00:1A:2B:3C:4D:5E',
#             'hostname': 'example.com',
#             'vendor': 'Vendor Inc.',
#             'os': 'Linux',
#             'device_type': 'Server',
#             'status': True
#         }

#         self.scanned_host = ScannedHost.objects.create(**self.host_data)

#     def test_host_creation(self):
#         """Test that a ScannedHost was created correctly."""
#         for field, value in self.host_data.items():
#             self.assertEqual(getattr(self.scanned_host, field), value)

#     def test_unique_ip(self):
#         """Test that the IP field is unique."""
#         with self.assertRaises(ValueError):
#             ScannedHost.objects.create(ip='192.168.1.1')

#     def test_default_status(self):
#         """Test that status defaults to False."""
#         new_host = ScannedHost.objects.create(ip='192.168.1.2')
#         self.assertFalse(new_host.status)

#     def test_str_representation(self):
#         """Test the string representation of the ScannedHost."""
#         self.assertEqual(str(self.scanned_host), 'ScannedHost 192.168.1.1')

#     def test_null_fields(self):
#         """Test that null fields are stored as None."""
#         null_fields = ['ipv6', 'mac', 'hostname', 'vendor', 'os', 'device_type']
#         for field in null_fields:
#             setattr(self.scanned_host, field, None)
#         self.scanned_host.save()
#         updated_host = ScannedHost.objects.get(id=self.scanned_host.id)
#         for field in null_fields:
#             self.assertIsNone(getattr(updated_host, field))

# class UserSetting(models.Model):
#     user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
#     company = models.CharField(max_length=254, blank=True, null=True)
#     license_exists = models.CharField(max_length=254, blank=True, null=True)
#     role = models.CharField(max_length=254, blank=True, null=True)
#     api_key = models.CharField(
#         max_length=254, unique=True, default=_createHash)

# from django.test import TestCase
# from your_app.models import Item

# class ItemModelTestCase(TestCase):

#     def test_item_string_representation(self):
#         item = Item.objects.create(name="Test Item", price=10.99)
#         self.assertEqual(str(item), "Test Item - $10.99")

# if __name__ == '__main__':
#     unittest.main()

# from django.test import TestCase
# from myapp.models import CVEData

# class CVEDataTestCase(TestCase):
#     def setUp(self):
#         self.user_data = {
#             'id': 'CVE-2023-1234',
#             'status': 'ENTRY',
#             'description': 'A test description.',
#             'references': 'Test references.',
#             'phase': 'Test phase.',
#             'votes': 'Test votes.',
#             'comments': 'Test comments.',
#             'added_by': 'TestUser',
#         }
#         self.user = CVEData.objects.create(**self.user_data)

#     def test_user_deletion(self):
#         # Ensure the user exists before deletion
#         self.assertTrue(CVEData.objects.filter(id=self.user_data['id']).exists())

#         # Delete the user
#         self.user.delete()

#         # Ensure the user no longer exists after deletion
#         self.assertFalse(CVEData.objects.filter(id=self.user_data['id']).exists())

# from django.test import TestCase
# from myapp.models import PortService, MSFHistory

# class PortServiceTestCase(TestCase):
#     def setUp(self):
#         self.user_data = {
#             'command': 'test-command',
#             'job_id': 'test-job-id',
#             'user': 'TestUser',
#             'status': True,
#             'output': 'Test output.',
#             'type': 'Test type',
#             'failed': False,
#         }
#         self.user = MSFHistory.objects.create(**self.user_data)

#         self.port_service_data = {
#             'port': 8080,
#             'port_status': True,
#             'service': 'HTTP',
#             'job': self.user,
#         }
#         self.port_service = PortService.objects.create(**self.port_service_data)

#     def test_user_deletion(self):
#         # Ensure the user and related PortService instance exist before deletion
#         self.assertTrue(MSFHistory.objects.filter(job_id=self.user_data['job_id']).exists())
#         self.assertTrue(PortService.objects.filter(port=8080, service='HTTP').exists())

#         # Delete the user
#         self.user.delete()

#         # Ensure the user and related PortService instance no longer exist after deletion
#         self.assertFalse(MSFHistory.objects.filter(job_id=self.user_data['job_id']).exists())
#         self.assertFalse(PortService.objects.filter(port=8080, service='HTTP').exists())

# from django.test import TestCase
# from myapp.models import ScannedHostDetails, ScannedHost

# class ScannedHostDetailsTestCase(TestCase):
#     def setUp(self):
#         self.scanned_host_data = {
#             # Define fields for ScannedHost here
#         }
#         self.scanned_host = ScannedHost.objects.create(**self.scanned_host_data)

#         self.scanned_host_details_data = {
#             'scanned_host': self.scanned_host,
#             'port': '8080',
#             'service': 'HTTP',
#             'version': '1.0',
#             'additional_data': {'key': 'value'},
#         }
#         self.scanned_host_details = ScannedHostDetails.objects.create(**self.scanned_host_details_data)

#     def test_user_deletion(self):
#         # Ensure the user and related ScannedHostDetails instance exist before deletion
#         self.assertTrue(ScannedHost.objects.filter(id=self.scanned_host.id).exists())
#         self.assertTrue(
#             ScannedHostDetails.objects.filter(scanned_host=self.scanned_host, port='8080').exists()
#         )

#         # Delete the user
#         self.scanned_host.delete()

#         # Ensure the user and related ScannedHostDetails instance no longer exist after deletion
#         self.assertFalse(ScannedHost.objects.filter(id=self.scanned_host.id).exists())
#         self.assertFalse(
#             ScannedHostDetails.objects.filter(scanned_host=self.scanned_host, port='8080').exists()
#         )

# from django.test import TestCase
# from myapp.models import GlobalConfig

# class GlobalConfigTestCase(TestCase):
#     def setUp(self):
#         self.config_data = {
#             'setting': 'test_setting',
#             'value': 'test_value',
#             'action': 'test_action',
#             'extra': {'key': 'value'},
#             'description': 'Test description',
#         }
#         self.config = GlobalConfig.objects.create(**self.config_data)

#     def test_user_deletion(self):
#         self.assertTrue(GlobalConfig.objects.filter(setting= self.config_data['setting']).exists())
#         self.config.delete()
#         self.assertFalse(GlobalConfig.objects.filter(setting= self.config_data['setting']).exists())

# from django.test import TestCase
# from myapp.models import IntegrationConfig

# class IntegrationConfigTestCase(TestCase):
#     def setUp(self):
#         self.config_data = {
#             'type': 'notification',
#             'identifier': 'slack',
#             'filters': {'key': 'value'},
#             'config': {'key': 'value'},
#             'extra': {'key': 'value'},
#             'org_name': 'TestOrg',
#             'description': 'Test description',
#         }
#         self.config = IntegrationConfig.objects.create(**self.config_data)

#     def test_user_deletion(self):
#         # Ensure the user exists before deletion
#         self.assertTrue(IntegrationConfig.objects.filter(org_name='TestOrg').exists())

#         # Delete the user
#         self.config.delete()

#         # Ensure the user no longer exists after deletion
#         self.assertFalse(IntegrationConfig.objects.filter(org_name='TestOrg').exists())

"""
For testing an api use the following code-:
Also install the particular package
$ pip install lxml==3.2.3
$ pip install defusedxml==0.4.1


from tastypie.test import ResourceTestCase

class EntryResourceTest(ResourceTestCase):

    def test_get_api_json(self):
        resp = self.api_client.get('/api/whatever/', format='json')
        self.assertValidJSONResponse(resp)

    def test_get_api_xml(self):
        resp = self.api_client.get('/api/whatever/', format='xml')
        self.assertValidXMLResponse(resp)
"""

# import pytest
# import re
# from your_module import is_valid_email

# def test_valid_email():
#     valid_emails = [
#         "test@example.com",
#         "user123@domain.net",
#         "another.email@gmail.com",
#     ]

#     for email in valid_emails:
#         assert is_valid_email(email) is True

# def test_invalid_email():
#     invalid_emails = [
#         "invalid-email",
#         "user@.com",
#         "@domain.com",
#         "user@domain",
#         "user@domain.",
#     ]

#     for email in invalid_emails:
#         assert is_valid_email(email) is False

# from django.test import TestCase
# from django.core.exceptions import ValidationError
# from your_app.models import IntegrationConfig

# class IntegrationConfigModelTestCase(TestCase):
#     def test_blank_fields(self):
#         # Try creating an instance with all fields blank
#         with self.assertRaises(ValidationError):
#             IntegrationConfig.objects.create()

#     def test_invalid_notification_type(self):
#         # Try creating an instance with an invalid notification type
#         with self.assertRaises(ValidationError):
#             IntegrationConfig.objects.create(type='invalid_type')

#     def test_invalid_identifier(self):
#         # Try creating an instance with an invalid identifier
#         with self.assertRaises(ValidationError):
#             IntegrationConfig.objects.create(identifier='invalid_identifier')

#     def test_long_org_name(self):
#         # Try creating an instance with an org_name that exceeds max length
#         long_name = 'a' * 256
#         with self.assertRaises(ValidationError):
#             IntegrationConfig.objects.create(org_name=long_name)

#     def test_long_description(self):
#         # Try creating an instance with a description that exceeds max length
#         long_description = 'a' * 256
#         with self.assertRaises(ValidationError):
#             IntegrationConfig.objects.create(description=long_description)

#     def test_invalid_json_fields(self):
#         # Try creating an instance with invalid JSON data in fields
#         invalid_filters = 'invalid_json'
#         invalid_config = 'invalid_json'
#         invalid_extra = 'invalid_json'
#         with self.assertRaises(ValidationError):
#             IntegrationConfig.objects.create(filters=invalid_filters, config=invalid_config, extra=invalid_extra)


import pytest
import requests

BASE_URL = 'http://your-api-url.com'  # Replace with your API URL

def test_get_users():
    response = requests.get(f'{BASE_URL}/users')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_user_by_id():
    user_id = 1  # Replace with a valid user ID
    response = requests.get(f'{BASE_URL}/users/{user_id}')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data.get('id') == user_id

def test_invalid_user_id():
    invalid_user_id = 9999  # An invalid user ID
    response = requests.get(f'{BASE_URL}/users/{invalid_user_id}')
    assert response.status_code == 404
    data = response.json()
    assert 'detail' in data

def test_create_user():
    user_data = {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        # Other required fields
    }
    response = requests.post(f'{BASE_URL}/users', json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert isinstance(data, dict)
    assert data.get('id') is not None

def test_missing_required_fields():
    invalid_user_data = {
        'name': 'Jane Smith'
        # Missing 'email' field
    }
    response = requests.post(f'{BASE_URL}/users', json=invalid_user_data)
    assert response.status_code == 400
    data = response.json()
    assert 'email' in data

def test_update_user():
    user_id = 1
    updated_user_data = {
        'name': 'Updated Name'
    }
    response = requests.put(f'{BASE_URL}/users/{user_id}', json=updated_user_data)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data.get('name') == updated_user_data['name']

def test_delete_user():
    user_id = 1
    response = requests.delete(f'{BASE_URL}/users/{user_id}')
    assert response.status_code == 204

def test_nonexistent_user_delete():
    invalid_user_id = 9999
    response = requests.delete(f'{BASE_URL}/users/{invalid_user_id}')
    assert response.status_code == 404


import re

def is_valid_email(email):
    regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex_pattern, email)

# Test cases
print(is_valid_email("user@example.com"))  # True
print(is_valid_email("invalid.email"))     # False

import unittest
import requests
import re

class TestAPIURLFieldWithRegex(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://your-api-base-url"

    def test_url_field_with_regex(self):
        response = requests.get(self.base_url + "/api-endpoint")
        self.assertEqual(response.status_code, 200)

        # Assuming the API response is in JSON format
        response_json = response.json()

        # Replace "url_field_name" with the actual URL field you want to test
        url_field_value = response_json.get("url_field_name", "")

        # Define the regex pattern for basic URL validation
        url_regex_pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/?'

        # Test the URL field value against the regex pattern
        self.assertTrue(re.match(url_regex_pattern, url_field_value))

if __name__ == "__main__":
    unittest.main()
