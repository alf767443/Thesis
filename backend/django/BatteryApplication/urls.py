from django.urls import re_path as url
from BatteryApplication import views

urlpatterns=[
    url(r'^battery/status$', views.statusApi),
    url(r'^battery/status/([0-9]+)$', views.statusApi),
    
    url(r'^battery/physical$', views.physicalApi),
    url(r'^battery/physical/([0-9]+)$', views.physicalApi),

    ## Get last battery status##
    url(r'^battery/status/last$', views.lastStatusApi),
    url(r'^battery/status/last/([0-9]+)$', views.lastStatusApi)
]