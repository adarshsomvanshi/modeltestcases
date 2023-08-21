"""
from django.test import TestCase
from testcases.models import *
from unittest import mock
from datetime import datetime
import pytz
from django.contrib.auth.models import User

class RawRequestModelTest(TestCase):
    def setUp(self):
        self.raw_request = RawRequests.objects.create(
            unique_id='123456',
            request='Sample request data',
            response='Sample response data'
        )

    def test_raw_request_creation(self):
        self.assertEqual(self.raw_request.unique_id, '123456')
        self.assertEqual(self.raw_request.request, 'Sample request data')
        self.assertEqual(self.raw_request.response, 'Sample response data')

    def test_string_representation(self):
        self.assertEqual(str(self.raw_request.unique_id), self.raw_request.unique_id)
        self.assertEqual(str(self.raw_request.request), self.raw_request.request)
        self.assertEqual(str(self.raw_request.response), self.raw_request.response)

    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            raw_data = RawRequests.objects.create(
                unique_id = '12478'
            )
            self.assertEqual(raw_data.unique_id, '12478')
            self.assertEqual(raw_data.request, None)
            self.assertEqual(raw_data.response, None)
            self.assertEqual(raw_data.created_at, mock_date)
            self.assertEqual(raw_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            raw_data = RawRequests.objects.create(unique_id='12478')

        self.assertEquals(raw_data.created_at, mock_date)
        self.assertEquals(raw_data.updated_at, mock_date)
        self.assertEquals(raw_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            raw_data.request = None
            raw_data.save()

        self.assertEqual(raw_data.created_at, mock_date)
        self.assertEqual(raw_data.updated_at, mock_update_date)
        self.assertEqual(raw_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')

    def test_default_blank_fields(self):
        new_raw_request = RawRequests.objects.create(
            unique_id='789',
            # request= '',
            # response=''
        )
        self.assertIsNone(new_raw_request.request)
        self.assertIsNone(new_raw_request.response)


# All the testcases for this model is done.
class VulnerabilitiesModelTest(TestCase):
    def setUp(self):
        self.vul = Vulnerabilities.objects.create(
            unique_id='CVE-2023-1234',
            ip='192.168.1.1',
            port=80,
            location='Sample Location',
            org='Sample Org',
            rule_id='R123',
            source='Sample Source',
            rule_severity=3,
            rule_description='Sample rule description',
            rule_finding='Sample rule finding',
            info='Additional info',
            timestamp='2023-08-10',
            status='Open',
            assignee='John Doe',
            history='Initial finding',
            jira='Additional Jira',
            notes='some additional notes',
            creator='Alice',
            owner='Bob',
            vertical='Sample Vertical',
            service_owner='Service Owner',
        )
    def test_vulnerabilities_creation(self):
        self.assertEqual(self.vul.unique_id, 'CVE-2023-1234')
        self.assertEqual(self.vul.ip,'192.168.1.1')
        self.assertEqual(self.vul.port,80)
        self.assertEqual(self.vul.location,"Sample Location")
        self.assertEqual(self.vul.org,"Sample Org")
        self.assertEqual(self.vul.rule_id,"R123")
        self.assertEqual(self.vul.source,"Sample Source")
        self.assertEqual(self.vul.rule_severity,3)
        self.assertEqual(self.vul.rule_description,"Sample rule description")
        self.assertEqual(self.vul.rule_finding,"Sample rule finding")
        self.assertEqual(self.vul.info,"Additional info")
        self.assertEqual(str(self.vul.timestamp),"2023-08-10")
        self.assertEqual(self.vul.status,"Open")
        self.assertEqual(self.vul.assignee,"John Doe")
        self.assertEqual(self.vul.history,"Initial finding")
        self.assertEqual(self.vul.jira,"Additional Jira")
        self.assertEqual(self.vul.notes,"some additional notes")
        self.assertEqual(self.vul.creator,"Alice")
        self.assertEqual(self.vul.owner,"Bob")
        self.assertEqual(self.vul.vertical,"Sample Vertical")
        self.assertEqual(self.vul.service_owner,"Service Owner")

    def test_default_status(self):
        new_vulnerability = Vulnerabilities.objects.create(
            unique_id='CVE-2023-5678',
            ip='192.168.1.2',
            port=443,
            location='Another Location',
            org='Another Org',
            rule_id='R567',
            source='Another Source',
            rule_severity=2,
            rule_description='Another rule description',
            rule_finding='Another rule finding',
            info='Additional info',
            timestamp='2023-08-11',
            # history = None      #for checking purpose set history is none.
        )
        self.assertEqual(new_vulnerability.status, 'Open')
        self.assertEqual(new_vulnerability.assignee, 'Unassigned')
        self.assertEqual(new_vulnerability.history, '')

    def test_vul_null_type(self):
        new_vul = Vulnerabilities.objects.create(
            unique_id="CVE-2023-12",
            ip='192.168.1.4',
            port=443,     # it cannot be null.
            # rule_id='R597',
            # location='Another Locations',
            # source='Another Sources',
            rule_severity=8,   #it cannot be null
            # history = ''     #For checking purpose put history value to empty string.
        )
        self.assertIsNone(new_vul.org)
        self.assertIsNone(new_vul.rule_description)
        self.assertIsNone(new_vul.rule_finding)
        self.assertIsNone(new_vul.info)
        self.assertIsNone(new_vul.timestamp)
        # self.assertEqual(new_vul.history, None)
        self.assertIsNone(new_vul.jira)
        self.assertIsNone(new_vul.notes)
        self.assertIsNone(new_vul.creator)
        self.assertIsNone(new_vul.owner)
        self.assertIsNone(new_vul.vertical)
        self.assertIsNone(new_vul.service_owner)

    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            vul_data = Vulnerabilities.objects.create(
                unique_id = 'CVE-2023-1245',
                ip = '192.168.1.6',
                port = 448,
                location = 'Another Sample Location',
                rule_id='R504',
                source='Another Sample Sources',
                rule_severity=6,
            )

            self.assertEqual(vul_data.unique_id, 'CVE-2023-1245')
            self.assertEqual(vul_data.ip, '192.168.1.6')
            self.assertEqual(vul_data.port, 448)
            self.assertEqual(vul_data.location, 'Another Sample Location')
            self.assertEqual(vul_data.rule_id, 'R504')
            self.assertEqual(vul_data.source, 'Another Sample Sources')
            self.assertEqual(vul_data.rule_severity, 6)
            self.assertEqual(vul_data.status, 'Open')
            self.assertEqual(vul_data.assignee, 'Unassigned')
            self.assertEqual(vul_data.history, '')
            self.assertIsNone(vul_data.org)
            self.assertIsNone(vul_data.rule_description)
            self.assertIsNone(vul_data.rule_finding)
            self.assertIsNone(vul_data.info)
            self.assertIsNone(vul_data.timestamp)
            self.assertIsNone(vul_data.jira)
            self.assertIsNone(vul_data.notes)
            self.assertIsNone(vul_data.creator)
            self.assertIsNone(vul_data.owner)
            self.assertIsNone(vul_data.creator)
            self.assertIsNone(vul_data.service_owner)
            self.assertEqual(vul_data.created_at, mock_date)
            self.assertEqual(vul_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            vul_data = Vulnerabilities.objects.create(
                unique_id = 'CVE-2023-1245',
                ip = '192.168.1.6',
                port = 448,
                location = 'Another Sample Location',
                rule_id='R504',
                source='Another Sample Sources',
                rule_severity=6,
            )

        self.assertEqual(vul_data.created_at, mock_date)
        self.assertEqual(vul_data.updated_at, mock_date)
        self.assertEqual(vul_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            vul_data.unique_id = True
            vul_data.save()

        self.assertEquals(vul_data.created_at, mock_date)
        self.assertEquals(vul_data.updated_at, mock_update_date)
        self.assertEquals(vul_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')    


    def test_str_representation(self):
        self.assertEqual(str(self.vul.unique_id), self.vul.unique_id)
        self.assertEqual(str(self.vul.ip), self.vul.ip)
        self.assertEqual(str(self.vul.location), self.vul.location)
        self.assertEqual(str(self.vul.org), self.vul.org)
        self.assertEqual(str(self.vul.rule_id), self.vul.rule_id)
        self.assertEqual(str(self.vul.source), self.vul.source)
        self.assertEqual(str(self.vul.rule_description), self.vul.rule_description)
        self.assertEqual(str(self.vul.rule_finding), self.vul.rule_finding)
        self.assertEqual(str(self.vul.info), self.vul.info)
        self.assertEqual(str(self.vul.history), self.vul.history)
        self.assertEqual(str(self.vul.jira), self.vul.jira)
        self.assertEqual(str(self.vul.notes), self.vul.notes)
        self.assertEqual(str(self.vul.status), self.vul.status)
        self.assertEqual(str(self.vul.assignee), self.vul.assignee)
        self.assertEqual(str(self.vul.creator), self.vul.creator)
        self.assertEqual(str(self.vul.owner), self.vul.owner)
        self.assertEqual(str(self.vul.vertical), self.vul.vertical)
        self.assertEqual(str(self.vul.service_owner), self.vul.service_owner)
        self.assertEqual(int(self.vul.port), self.vul.port)
        self.assertEqual(int(self.vul.rule_severity), self.vul.rule_severity)


# All the testcases for this model is done.
class SourceModelTest(TestCase):
    def setUp(self):
        self.src = Sources.objects.create(
            source ='192.168.1.1',
            type = Sources.SourceTypes.IP,
            is_excluded = False,
            is_sensitive = False,
            included_rules = 'Rule1, Rule 2',
            exclude_rules = 'Rule 3',
            org_name = 'Sample Organiztion',
            description = 'Sample description',
            identifier = 'ABC123',
        )
    def test_src_creation(self):
        self.assertEqual(self.src.source, '192.168.1.1')
        self.assertEqual(self.src.type, Sources.SourceTypes.IP)
        self.assertFalse(self.src.is_excluded)
        self.assertFalse(self.src.is_sensitive)
        self.assertEqual(self.src.included_rules, 'Rule1, Rule 2')
        self.assertEqual(self.src.exclude_rules,'Rule 3')
        self.assertEqual(self.src.org_name,'Sample Organiztion')
        self.assertEqual(self.src.description,'Sample description')
        self.assertEqual(self.src.identifier,'ABC123')

    def test_string_representation(self):
        self.assertEqual(str(self.src.source), self.src.source)
        self.assertEqual(str(self.src.type), self.src.type)
        self.assertEqual(bool(self.src.is_excluded), self.src.is_excluded)
        self.assertEqual(bool(self.src.is_sensitive), self.src.is_sensitive)
        self.assertEqual(str(self.src.included_rules), self.src.included_rules)
        self.assertEqual(str(self.src.exclude_rules),self.src.exclude_rules)
        self.assertEqual(str(self.src.org_name),self.src.org_name)
        self.assertEqual(str(self.src.description),self.src.description)
        self.assertEqual(str(self.src.identifier),self.src.identifier)
    
    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            src_data = Sources.objects.create(
                source = 'name.examples.com',
                type = Sources.SourceTypes.IP,
            )

            self.assertEqual(src_data.source, 'name.examples.com')
            self.assertEqual(src_data.type, Sources.SourceTypes.IP)
            self.assertFalse(src_data.is_excluded)
            self.assertFalse(src_data.is_sensitive)
            self.assertIsNone(src_data.included_rules)
            self.assertIsNone(src_data.exclude_rules)
            self.assertIsNone(src_data.org_name)
            self.assertIsNone(src_data.description)
            self.assertIsNone(src_data.identifier)
            self.assertEqual(src_data.created_at, mock_date)
            self.assertEqual(src_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            src_data = Sources.objects.create(source='name.examples.com', type = Sources.SourceTypes.IP)

        self.assertEqual(src_data.created_at, mock_date)
        self.assertEqual(src_data.updated_at, mock_date)
        self.assertEqual(src_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            src_data.is_sensitive = True
            src_data.save()

        self.assertEquals(src_data.created_at, mock_date)
        self.assertEquals(src_data.updated_at, mock_update_date)
        self.assertEquals(src_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')


    def test_src_default_type(self):
        new_src = Sources.objects.create(
            source='hostname.example.com',
            # is_excluded=True,
        )
        self.assertEqual(new_src.type, Sources.SourceTypes.IP)
        self.assertFalse(new_src.is_excluded)
        self.assertFalse(new_src.is_sensitive)

    def test_src_null_type(self):
        new_src = Sources.objects.create(
            source = 'hostname.exapmple.com',
            type = Sources.SourceTypes.IP,
            is_excluded = False,
            is_sensitive = False
        )
        # self.assertIsNotNone(new_src.source)
        self.assertIsNone(new_src.included_rules)
        self.assertIsNone(new_src.exclude_rules)
        self.assertIsNone(new_src.org_name)
        self.assertIsNone(new_src.description)
        self.assertIsNone(new_src.identifier)

    def test_valid_sources_type(self):
        valid_choices = [choice[0] for choice in Sources.SourceTypes.choices ]
        src_instance = Sources.objects.create(type=valid_choices[0])
        self.assertIn(src_instance.type, valid_choices)

    # def test_updated_timestamp(self):
    #     # Test that updated_at field is updated on modification.
    #     initial_updated_at = self.src.updated_at
    #     self.src.response = 'Updated response data'
    #     self.src.save()
    #     updated_src = Sources.objects.get(id=self.src.id)
    #     self.assertNotEqual(updated_src.updated_at, initial_updated_at)

#All the testcases for this model is done.
class IntegrationConfigModelTest(TestCase):
    def setUp(self):
        self.ic = IntegrationConfig.objects.create(
            type = IntegrationConfig.NotificationTypes.NOTIFICATION,
            identifier = IntegrationConfig.SourceTypes.HTTPENDPOINT,
            filters = {'severity': 'high'},
            config = {'url':'https://example.com/'},
            extra = {'param':'value1'},
            org_name = 'sample org',
            description = 'Sample description',
        )
    def test_ic_creation(self):
        self.assertEqual(self.ic.type,IntegrationConfig.NotificationTypes.NOTIFICATION)
        self.assertEqual(self.ic.identifier, IntegrationConfig.SourceTypes.HTTPENDPOINT)
        self.assertEqual(self.ic.filters, {'severity': 'high'})
        self.assertEqual(self.ic.config, {'url':'https://example.com/'})
        self.assertEqual(self.ic.extra ,{'param':'value1'})
        self.assertEqual(self.ic.org_name ,'sample org')
        self.assertEqual(self.ic.description, 'Sample description')

    def test_string_representation(self):
        self.assertEqual(str(self.ic.type), self.ic.type)
        self.assertEqual(str(self.ic.identifier), self.ic.identifier)
        self.assertEqual(dict(self.ic.filters), self.ic.filters)
        self.assertEqual(dict(self.ic.config), self.ic.config)
        self.assertEqual(dict(self.ic.extra) ,self.ic.extra)
        self.assertEqual(str(self.ic.org_name) ,self.ic.org_name)
        self.assertEqual(str(self.ic.description), self.ic.description)

    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            ic_data = IntegrationConfig.objects.create(
                org_name = 'Sample_org'
            )

            self.assertEqual(ic_data.org_name, 'Sample_org')
            self.assertEqual(ic_data.type, IntegrationConfig.NotificationTypes.NOTIFICATION)
            self.assertEqual(ic_data.identifier, IntegrationConfig.SourceTypes.HTTPENDPOINT)
            self.assertIsNone(ic_data.description)
            self.assertEqual(ic_data.filters, {})
            self.assertEqual(ic_data.config, {})
            self.assertEqual(ic_data.extra, {})
            self.assertEqual(ic_data.created_at, mock_date)
            self.assertEqual(ic_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            ic_data = IntegrationConfig.objects.create(org_name='Sample_org')

        self.assertEqual(ic_data.created_at, mock_date)
        self.assertEqual(ic_data.updated_at, mock_date)
        self.assertEqual(ic_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            ic_data.org_name = None
            ic_data.save()

        self.assertEquals(ic_data.created_at, mock_date)
        self.assertEquals(ic_data.updated_at, mock_update_date)
        self.assertEquals(ic_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')


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

    # def test_updated_timestamp(self):
    #     # Test that updated_at field is updated on modification.
    #     initial_updated_at = self.ic.updated_at
    #     self.ic.response = 'Updated response data'
    #     self.ic.save()
    #     updated_ic = IntegrationConfig.objects.get(id=self.ic.id)
    #     self.assertNotEqual(updated_ic.updated_at, initial_updated_at)
    

#All testcases for this model is done.
class GlobalConfigModelTest(TestCase):
    def setUp(self):
        self.gc = GlobalConfig.objects.create(
            setting = 'Max_Connections',
            value = '100',
            action = 'increase',
            extra = {'param1': 'value1'},
            description = 'Sample description'
        )
    
    def test_gc_creation(self):
        self.assertEqual(self.gc.setting,'Max_Connections')
        self.assertEqual(self.gc.value,'100')
        self.assertEqual(self.gc.action,'increase')
        self.assertEqual(self.gc.extra,{'param1': 'value1'})
        self.assertEqual(self.gc.description,'Sample description')
    def test_string_representation(self):
        self.assertEqual(str(self.gc.setting), self.gc.setting)
        self.assertEqual(str(self.gc.value), self.gc.value)
        self.assertEqual(str(self.gc.action), self.gc.action)
        self.assertEqual(dict(self.gc.extra), self.gc.extra)
        self.assertEqual(str(self.gc.description), self.gc.description)
        # self.assertTrue(str(self.gc.action))


    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            gc_data = GlobalConfig.objects.create(
                action = 'increase'
            )

            self.assertEqual(gc_data.action, 'increase')
            self.assertIsNone(gc_data.value)
            self.assertIsNone(gc_data.setting)
            self.assertIsNone(gc_data.description)
            self.assertEqual(gc_data.extra, {})
            self.assertEqual(gc_data.created_at, mock_date)
            self.assertEqual(gc_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            gc_data = GlobalConfig.objects.create(action='increase')

        self.assertEquals(gc_data.created_at, mock_date)
        self.assertEquals(gc_data.updated_at, mock_date)
        self.assertEquals(gc_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            gc_data.setting = None
            gc_data.save()

        self.assertEquals(gc_data.created_at, mock_date)
        self.assertEquals(gc_data.updated_at, mock_update_date)
        self.assertEquals(gc_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')


    def test_gc_default_type(self):
        new_gc = GlobalConfig.objects.create(
            setting = 'TIMEOUT',
        )
        self.assertIsNone(new_gc.value)
        self.assertIsNone(new_gc.action)
        self.assertIsNone(new_gc.description)
        self.assertEqual(new_gc.extra, {})

    
# class UserSettingModelTest(TestCase):
#     @staticmethod
#     def _createHash():
#         return hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username = 'testuser',
#             password = 'testpassword'
#         )

#         self.us = UserSetting.objects.create(
#             user = self.user,
#             company = 'Sample Company',
#             license_exists = 'Yes',
#             role = 'Admin',
#             api_key = self._createHash()
#         )
    
#     def test_us_creation(self):
#         self.assertEqual(self.us.user, self.user)
#         self.assertEqual(self.us.company,'Sample Company')
#         self.assertEqual(self.us.license_exists, 'Yes')
#         self.assertEqual(self.us.role, 'Admin')
    
#     def test_api_key_uniqueness(self):
#         with self.assertRaises(ValueError):
#             UserSetting.objects.create(
#                 user=self.user,
#                 company='Another Company',
#                 license_exists='No',
#                 role='User',
#                 api_key=self.us.api_key
#             )
#     def test_api_key_generation(self):
#         self.assertEqual(self.us.api_key, hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest())

#     def test_us_blank_type(self):
#         new_us = UserSetting.objects.create(
#             user = self.user,
#             company = '',
#             license_exists='',
#             role= '',
#         )
#         self.assertIsNone(new_us.company)
#         self.assertIsNone(new_us.license_exists)
#         self.assertIsNone(new_us.role)


# All testcases for this model is done.
class ScannedHostModelTest(TestCase):
    def setUp(self):
        self.host_name = ScannedHost.objects.create(
            ip = '192.168.1.1',
            ipv6 = '2001:db8::1',
            mac = '00:1A:2B:3C:4D:5E',
            hostname = 'example.com',
            vendor = 'Vendor Inc.',
            os = 'Linux',
            device_type = 'Server',
            status = False
        )
        self.assertTrue(isinstance(self.host_name, ScannedHost))
        self.assertEqual(str(self.host_name.ip), self.host_name.ip)
        self.assertEqual(str(self.host_name.ipv6), self.host_name.ipv6)
        self.assertEqual(str(self.host_name.mac), self.host_name.mac)
        self.assertEqual(str(self.host_name.hostname), self.host_name.hostname)
        self.assertEqual(str(self.host_name.vendor), self.host_name.vendor)
        self.assertEqual(str(self.host_name.os), self.host_name.os)
        self.assertEqual(str(self.host_name.device_type), self.host_name.device_type)
        self.assertEqual(bool(self.host_name.status), self.host_name.status)


    def test_scannedhost_ip_only(self):
        ip = '192.168.1.2'
        new_scanhost = ScannedHost.objects.create(ip=ip)
        self.assertEqual(new_scanhost.ip,ip)
        self.assertIsNone(new_scanhost.ipv6)
        self.assertIsNone(new_scanhost.mac)
        self.assertIsNone(new_scanhost.hostname)
        self.assertIsNone(new_scanhost.vendor)
        self.assertIsNone(new_scanhost.device_type)
        self.assertFalse(new_scanhost.status)

    # To check unique ip of scanned host
    # def test_shost_unique_ip(self):
    #     with self.assertRaises(ValueError):
    #         ScannedHost.objects.create(ip = '192.168.1.1')

        
    def test_shost_default_value_type(self):
        new_host = ScannedHost.objects.create(ip='192.168.1.2')  # Put status=True to check error.
        self.assertFalse(new_host.status)
        self.assertIsNone(new_host.ipv6)
        self.assertIsNone(new_host.mac)
        self.assertIsNone(new_host.hostname)
        self.assertIsNone(new_host.vendor)
        self.assertIsNone(new_host.os)
        self.assertIsNone(new_host.device_type)



# All the testcases for this model is done.
class ScannedHostDetailModelTest(TestCase):
    def setUp(self):
        self.new_scanned_host = ScannedHost.objects.create(ip='192.168.1.1')
        self.new_sh_details = ScannedHostDetails.objects.create(
            scanned_host = self.new_scanned_host,
            port = '80',
            service = 'HTTP',
            version = '2.0',
            additional_data = {'key':'value'},
        )
        self.assertTrue(isinstance(self.new_sh_details, ScannedHostDetails))
        self.assertEqual(str(self.new_sh_details.port), self.new_sh_details.port)
        self.assertEqual(str(self.new_sh_details.service), self.new_sh_details.service)
        self.assertEqual(str(self.new_sh_details.version), self.new_sh_details.version)
        # self.assertEqual(dict(self.new_sh_details.additional_data), self.new_sh_details.additional_data)


    def test_unknown_null_value(self):
        new_host_type = ScannedHostDetails.objects.create(
            scanned_host = self.new_scanned_host,
            port = '443',
            # version = '3.0' #for checking purpose put version = 3 it shows error
        )
        self.assertEqual(new_host_type.service, 'Unknown')
        self.assertIsNone(new_host_type.version)
        self.assertIsNone(new_host_type.additional_data)

    def test_additional_data(self):
        additional_data = {'key1': 'value1', 'key2': 'value2'}
        new_host_details = ScannedHostDetails.objects.create(
            scanned_host=self.new_scanned_host,
            port='8080',
            service='Custom',
            additional_data=additional_data
        )
        self.assertEqual(new_host_details.additional_data, additional_data)

    def test_scannedhostdetail_data_foreign_key(self):
        new_shdetails_data = ScannedHostDetails.objects.create(
            port='8000',
            service = 'HTTP',
            scanned_host = self.new_scanned_host
        )
        self.assertEqual(new_shdetails_data.scanned_host, self.new_scanned_host)


# All the testcases for this model is done.
class MSFHistoryModelTest(TestCase):
    def setUp(self):
        self.history_data = MSFHistory.objects.create(
            command='exploit/windows/smb/ms17_010_eternalblue',
            job_id='12346789',
            user='admin',
            status=True,
            output='Exploit Completed successfully',
            type='expliot',
            failed= False
        )
        self.assertTrue(isinstance(self.history_data,MSFHistory))
        self.assertEqual(str(self.history_data.command), self.history_data.command)
        self.assertEqual(str(self.history_data.job_id), self.history_data.job_id)
        self.assertEqual(str(self.history_data.user), self.history_data.user)
        self.assertEqual(bool(self.history_data.status), self.history_data.status)
        self.assertEqual(str(self.history_data.output), self.history_data.output)
        self.assertEqual(str(self.history_data.type), self.history_data.type)
        self.assertEqual(bool(self.history_data.failed), self.history_data.failed)


    # def test_msf_data_creations(self):
    #     for field, value in self.history_data.items():
    #         self.assertEqual(getattr(self.msf_entry_data,field), value)

    def test_default_values(self):
        new_history_entry = MSFHistory.objects.create(
            command='post/multi/manage/shell_to_meterpreter',
            job_id='987654321',
            user='user1',
            type = 'post',
        )
        self.assertEqual(new_history_entry.output,"")
        self.assertFalse(new_history_entry.status)
        self.assertFalse(new_history_entry.failed)

    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            history_data = MSFHistory.objects.create(
                command = 'post/multi/manage/shell_to_meterpreters',
                job_id = '1254',
                user = 'admin',
            )

            self.assertEquals(history_data.job_id, '1254')
            self.assertEquals(history_data.user, 'admin')
            self.assertEquals(history_data.status, False)
            self.assertEquals(history_data.output, "")
            self.assertEquals(history_data.type, None)
            self.assertEquals(history_data.failed, False)
            self.assertEquals(history_data.initiated_at, mock_date)
            self.assertEquals(history_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            history_data = MSFHistory.objects.create(job_id='1254')

        self.assertEquals(history_data.initiated_at, mock_date)
        self.assertEquals(history_data.updated_at, mock_date)
        self.assertEquals(history_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            history_data.type = None
            history_data.save()

        self.assertEquals(history_data.initiated_at, mock_date)
        self.assertEquals(history_data.updated_at, mock_update_date)
        self.assertEquals(history_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')


    def test_nullable_type_field(self):
        history_entry = MSFHistory.objects.create(
            command='use auxiliary/scanner/smb/smb_version',
            # job_id='246813579',
            user='user2',
            status=True,
            output='Scanning completed',
            failed=False
        )
        self.assertIsNone(history_entry.job_id)
        self.assertIsNone(history_entry.type)

# All the testcases of this model is done.
class PortServiceModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.msf_history = MSFHistory.objects.create(job_id=1)
    
    def test_ps_data_creation(self):
        ps_data = PortService.objects.create(
            port = 8080,
            port_status = False,
            service = 'HTTP',
            job = self.msf_history
        )
        self.assertTrue(isinstance(ps_data, PortService))
        self.assertEqual(int(ps_data.port), ps_data.port)
        self.assertEqual(bool(ps_data.port_status), ps_data.port_status)
        self.assertEqual(str(ps_data.service), ps_data.service)

    def test_ps_data_default(self):
        new_ps_data = PortService.objects.create(
            port=8000,
            service = 'HTTP',
            job = self.msf_history
        )
        self.assertFalse(new_ps_data.port_status)
        # self.assertTrue(new_ps_data.port_status)  # wrong value inserted for checking purpose


    def test_ps_data_foreign_key(self):
        new_ps_data = PortService.objects.create(
            port=8000,
            service = 'HTTP',
            # job = 'computer operator',
            job = self.msf_history
        )
        self.assertEqual(new_ps_data.job, self.msf_history)


# All the testcases of this model is done.
class CVEDataModelTest(TestCase):
    def test_cve_data_creation(self):
        cve_data = CVEData.objects.create(
            id="CVE-2023-1234",
            status="ENTRY",
            description="Sample description",
            references="Sample references",
            phase="Sample phase",
            votes="Sample votes",
            comments="Sample comments",
            added_by="Sample user"    #for checking purpose put integer instead of string
        )
        self.assertTrue(isinstance(cve_data,CVEData))
        self.assertEqual(str(cve_data.id), cve_data.id)
        self.assertEqual(str(cve_data.status), cve_data.status)
        self.assertEqual(str(cve_data.description), cve_data.description)
        self.assertEqual(str(cve_data.references), cve_data.references)
        self.assertEqual(str(cve_data.phase), cve_data.phase)
        self.assertEqual(str(cve_data.votes), cve_data.votes)
        self.assertEqual(str(cve_data.comments), cve_data.comments)
        self.assertEqual(str(cve_data.added_by), cve_data.added_by)


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

    #Checking for null value in these fields but it shows error.
    # def test_null_value(self):
    #     cve_data_new = CVEData.objects.create(
    #         id = 'CVE-2023-169'
    #     )
    #     self.assertIsNone(cve_data_new.created_at)
    #     self.assertIsNone(cve_data_new.updated_at)

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
    
    def test_created_at_default_values(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            cve_data = CVEData.objects.create(
                id = 'CVE-2021-147'
            )

            self.assertEqual(cve_data.id, 'CVE-2021-147')
            self.assertEqual(cve_data.status, 'ENTRY')
            self.assertEqual(cve_data.description, '')
            self.assertEqual(cve_data.references, '')
            self.assertEqual(cve_data.phase, '')
            self.assertEqual(cve_data.votes, '')
            self.assertEqual(cve_data.comments, '')
            self.assertEqual(cve_data.added_by, '')
            self.assertEqual(cve_data.created_at, mock_date)
            self.assertEqual(cve_data.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2023, 8, 4, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            cve_data = CVEData.objects.create(id = 'CVE-2021-147')

        self.assertEqual(cve_data.created_at, mock_date)
        self.assertEqual(cve_data.updated_at, mock_date)
        self.assertEqual(cve_data.updated_at.strftime("%Y-%m-%d"), '2023-08-04')

        mock_update_date = datetime(2023, 8, 5, 14, 57, 11, 703055, tzinfo=pytz.UTC)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            cve_data.votes = ""
            cve_data.save()

        self.assertEqual(cve_data.created_at, mock_date)
        self.assertEqual(cve_data.updated_at, mock_update_date)
        self.assertEqual(cve_data.updated_at.strftime("%Y-%m-%d"), '2023-08-05')

"""