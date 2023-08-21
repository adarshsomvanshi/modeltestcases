from django.contrib import admin
from django.urls import path
from testcases import views
from rest_framework import routers
from django.urls import include


router = routers.DefaultRouter()
router.register('IntegrationConfig',views.IntegrationConfigViewSet)
router.register('RawRequests',views.RawRequestsViewSet)
router.register('Vulnerabilities',views.VulnerabilitiesViewSet)
router.register('CVEData',views.CVEDataViewSet)
router.register('UploadedFile',views.UploadedFileViewSet)
router.register('GlobalConfig',views.GlobalConfigViewSet)
router.register('PortService',views.PortServiceViewSet)
router.register('MSFHistory',views.MSFHistoryViewSet)
router.register('ScannedHost',views.ScannedHostViewSet)
router.register('ScannedHostDetails',views.ScannedHostDetailsViewSet)
router.register('Sources',views.SourcesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
