from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import * 

class IntegrationConfigViewSet(viewsets.ModelViewSet):
    queryset = IntegrationConfig.objects.all()
    serializer_class = IntegrationConfigSerializer

class VulnerabilitiesViewSet(viewsets.ModelViewSet):
    queryset = Vulnerabilities.objects.all()
    serializer_class = VulnerabilitiesSerializer

class RawRequestsViewSet(viewsets.ModelViewSet):
    queryset = RawRequests.objects.all()
    serializer_class = RawRequestsSerializer

class CVEDataViewSet(viewsets.ModelViewSet):
    queryset = CVEData.objects.all()
    serializer_class = CVEDataSerializer

class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

class SourcesViewSet(viewsets.ModelViewSet):
    queryset = Sources.objects.all()
    serializer_class = SourcesSerializer

class GlobalConfigViewSet(viewsets.ModelViewSet):
    queryset = GlobalConfig.objects.all()
    serializer_class = GlobalConfigSerializer

class PortServiceViewSet(viewsets.ModelViewSet):
    queryset = PortService.objects.all()
    serializer_class = PortServiceSerializer

class MSFHistoryViewSet(viewsets.ModelViewSet):
    queryset = MSFHistory.objects.all()
    serializer_class = MSFHistorySerializer

class ScannedHostViewSet(viewsets.ModelViewSet):
    queryset = ScannedHost.objects.all()
    serializer_class = ScannedHostSerializer

class ScannedHostDetailsViewSet(viewsets.ModelViewSet):
    queryset = ScannedHostDetails.objects.all()
    serializer_class = ScannedHostDetailsSerializer
