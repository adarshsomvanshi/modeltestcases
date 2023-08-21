from rest_framework import serializers
from .models import *


class VulnerabilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerabilities
        fields = '__all__'


class RawRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawRequests
        fields = '__all__'


class CVEDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVEData
        fields = '__all__'

class IntegrationConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationConfig
        fields = '__all__'

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'

class SourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sources
        fields = '__all__'

class GlobalConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalConfig
        fields = '__all__'

class  PortServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortService
        fields = '__all__'

class  MSFHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MSFHistory
        fields = '__all__'

class  ScannedHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScannedHost
        fields = '__all__'

class  ScannedHostDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScannedHostDetails
        fields = '__all__'

