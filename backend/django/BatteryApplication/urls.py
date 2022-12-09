from django.urls import re_path as url
from BatteryApplication import views

urlpatterns=[
    url(r'^battery/sensor$', views.sensorApi),
    url(r'^battery/sensor/([0-9]+)$', views.sensorApi),
    
    url(r'^battery/calculate$', views.calculateApi),
    url(r'^battery/calculate/([0-9]+)$', views.calculateApi),

    url(r'^battery/battery$', views.batteryApi),
    url(r'^battery/battery/([0-9]+)$', views.batteryApi)
]