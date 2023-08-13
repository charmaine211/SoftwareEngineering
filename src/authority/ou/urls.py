"""
This module holds the URL endpoints of the application.

API-endpoints are defined in the router.
GUI-endpoints are defined in the urlpatterns.
"""

from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'signatures', views.SignaturesViewSet)
router.register(r'keys', views.KeysViewSet)

app_name = 'ou'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('signature_list/', views.IndexView.as_view(), name='index'),
    path('verify_result/', views.verify_signature, name='verify_result'),
    path('verify/', views.VerifyView.as_view(), name='verify'),
    path('sign/', views.upload_file, name='sign'),
    path('keys2/', views.Keys_View, name='keys2'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
]
