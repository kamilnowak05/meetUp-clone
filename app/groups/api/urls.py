from django.urls import path, include

from groups.api.views import AppGroupViewSet

from rest_framework.routers import DefaultRouter

app_name = 'groups'

router = DefaultRouter()
router.register(r'groups', AppGroupViewSet, base_name='groups')

urlpatterns = [
    path('', include(router.urls)),
]
