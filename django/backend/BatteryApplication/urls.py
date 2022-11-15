from django.urls import re_path as url
from BatteryApplication import views

urlpatterns=[
    url(r'^status$', views.statusApi),
    url(r'^status/([0-9]+)$', views.statusApi),
    
    url(r'^charge$', views.physicalApi),
    url(r'^charge/([0-9]+)$', views.physicalApi)
]