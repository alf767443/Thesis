from django.urls import re_path as url
from TestApp import views

urlpatterns=[
    url(r'^status$', views.departmentApi),
    url(r'^status/([0-9]+)$', views.departmentApi),
    
    url(r'^employee$', views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi)
]