from django.urls import re_path as url
from BatteryApplication import views

urlpatterns=[
    url(r'^battery/table=sensor$', views.sensorApi),
    url(r'^battery/table=sensor/([0-9]+)$', views.sensorApi),
    
    url(r'^battery/table=calculate$', views.calculateApi),
    url(r'^battery/table=calculate/([0-9]+)$', views.calculateApi),

    url(r'^battery/battery$', views.batteryApi),
    url(r'^battery/battery/([0-9]+)$', views.batteryApi),

    #Querys
    url(r'^battery/query=(?P<query>[0-9]{1})$', views.queryApi)
    
]