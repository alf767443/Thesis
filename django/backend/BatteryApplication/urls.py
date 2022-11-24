from django.urls import re_path as url
from BatteryApplication import views

urlpatterns=[
    url(r'^battery/status$', views.statusApi),
    url(r'^battery/status/([0-9]+)$', views.statusApi),
    
    url(r'^battery/charge$', views.physicalApi),
    url(r'^battery/charge/([0-9]+)$', views.physicalApi)
]