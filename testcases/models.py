# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _
import hashlib
from binascii import hexlify
from django.core.files.storage import FileSystemStorage
import time
import uuid
import random
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
import os
import csv


def _createHash():
    """This function generate 100 character long hash"""
    return hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ServicesFeJira(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    updated_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'buffercode_vul_fe_jira'


class RawRequests(models.Model):
    unique_id = models.CharField(max_length=50, null=False)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vulnerabilities(models.Model):
    unique_id = models.CharField(max_length=50, null=False)
    ip = models.TextField()
    port = models.IntegerField()
    location = models.TextField()
    org = models.TextField(blank=True, null=True)
    rule_id = models.TextField()
    source = models.TextField()
    rule_severity = models.IntegerField()
    rule_description = models.TextField(blank=True, null=True)
    rule_finding = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=30, default='Open')
    assignee = models.CharField(max_length=100, default='Unassigned')
    history = models.TextField(blank=True, null=True, default='')
    jira = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    vertical = models.CharField(max_length=255, blank=True, null=True)
    service_owner = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sources(models.Model):

    class SourceTypes(models.TextChoices):
        IP = 'ip', _('Ip')
        ADDRESS = 'address', _('Address')

    source = models.CharField(max_length=255, null=False)
    type = models.CharField(
        max_length=50, choices=SourceTypes.choices, default=SourceTypes.IP)
    is_excluded = models.BooleanField(default=False)
    is_sensitive = models.BooleanField(default=False)
    included_rules = models.TextField(max_length=65535, blank=True, null=True)
    exclude_rules = models.TextField(max_length=65535, blank=True, null=True)
    org_name = models.TextField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    identifier = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Notification Module table


class IntegrationConfig(models.Model):

    class NotificationTypes(models.TextChoices):
        NOTIFICATION = 'notification', _('Notification')
        LOGSEXPORTER = 'logs_exporter', _('logs_exporter')
        TICKETS = 'tickets', _('Tickets')
        REPORT = 'report', _('report')

    class SourceTypes(models.TextChoices):
        SLACK = 'slack', _('Slack')
        EMAIL = 'email', _('Email')
        HTTPENDPOINT = 'http', _('HTTP')
        ELK = 'elk', _('ELK')
        SUMOLOGIC = 'sumologic', _('SumoLogic')
        GENERICSIEM = 'generic_siem', _('GerericSIEM')
        JIRA = 'jira', _('Jira')
        PDFXLS = 'pdf_xls', _('Pdf_xls')

    type = models.CharField(
        max_length=100, choices=NotificationTypes.choices, default=NotificationTypes.NOTIFICATION)
    identifier = models.CharField(
        max_length=100, choices=SourceTypes.choices, default=SourceTypes.HTTPENDPOINT)
    filters = models.JSONField(default={})
    config = models.JSONField(default={})
    extra = models.JSONField(default={})
    org_name = models.TextField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GlobalConfig(models.Model):

    setting = models.TextField(max_length=65535, blank=True, null=True)
    value = models.TextField(max_length=65535, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    extra = models.JSONField(default={})
    description = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ScannedHost(models.Model):   #NetworkHost
    ip = models.CharField(max_length=255, unique=True)
    ipv6 = models.CharField(max_length=255, default=None, null=True)
    mac = models.CharField(max_length=255, default=None, null=True)
    hostname = models.CharField(max_length=255, default=None, null=True)
    vendor = models.CharField(max_length=255, default=None, null=True)
    os = models.CharField(max_length=255, default=None, null=True)
    device_type = models.CharField(max_length=255, default=None, null=True)
    status = models.BooleanField(default=0)


class ScannedHostDetails(models.Model):
    scanned_host = models.ForeignKey(ScannedHost, on_delete=models.CASCADE)
    port = models.CharField(max_length=10)
    service = models.CharField(max_length=255, default='Unknown')
    version = models.CharField(max_length=255, default=None, null=True)
    additional_data = JSONField(blank=True, null=True)


class MSFHistory(models.Model):  #instant jobs
    command = models.CharField(max_length=255)
    job_id = models.CharField(max_length=255, unique=True, default=None, null=True)
    user = models.CharField(max_length=255)
    # 0 means pending, 1 means completed
    status = models.BooleanField(default=0)
    output = models.TextField(default="")
    type = models.TextField(default=None, null=True)
    initiated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    failed = models.BooleanField(default=0)


class PortService(models.Model):   #Ports
    port = models.IntegerField()
    port_status = models.BooleanField(default=0)
    service = models.CharField(max_length=255)
    # Foreign key relationship
    job = models.ForeignKey(
        MSFHistory, on_delete=models.CASCADE, to_field='job_id')


class CVEData(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True)
    status = models.CharField(max_length=255, choices=(
        ('ENTRY', 'entry'),
        ('CANDIDATE', 'candidate'),
    ), default='ENTRY')
    description = models.TextField(default="")
    references = models.TextField(default="")
    phase = models.TextField(default="")
    votes = models.TextField(default="")
    comments = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    added_by = models.TextField(max_length=255, default="")


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', blank=False,
                                      null=False)
    filename = models.TextField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.TextField(max_length=255, null=True)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        super(UploadedFile, self).delete(*args, **kwargs)

