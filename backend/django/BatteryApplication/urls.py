from django.urls import re_path as url
from BatteryApplication import views

urlpatterns=[
    url(r'^battery/status$', views.statusApi),
    url(r'^battery/status/([0-9]+)$', views.statusApi),
    
    url(r'^battery/physical$', views.physicalApi),
    url(r'^battery/physical/([0-9]+)$', views.physicalApi),

    ## Get last battery status##
    url(r'^battery/status/last$', views.lastStatusApi),
    url(r'^battery/status/last/([0-9]+)$', views.lastStatusApi),

    url(r'^battery/sensor$', views.sensorApi),
    url(r'^battery/sensor/([0-9]+)$', views.sensorApi),
    
    url(r'^battery/calculate$', views.calculateApi),
    url(r'^battery/calculate/([0-9]+)$', views.calculateApi),

    url(r'^battery/battery$', views.batteryApi),
    url(r'^battery/battery/([0-9]+)$', views.batteryApi)
]