from django.urls import re_path as url
from BatteryApplication import views

urlpatterns=[
    # Full table
    url(r'^battery/battery$', views.batteryApi),                    # type: ignore 
    url(r'^battery/battery/([0-9]+)$', views.batteryApi),           # type: ignore 

    #Querys
    url(r'^battery/query=(?P<query>[0-9]{1})$', views.queryApi),    # type: ignore 
    
    # Query a table
    url(r'^battery/table=(?P<query>[0-9A-Za-z]+)$', views.tableApi) # type: ignore 
    
]