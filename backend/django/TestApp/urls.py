#from django.conf.urls import url
from django.urls import include,re_path as url
from TestApp import views



urlpatterns=[
    url(r'^department$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),
    
    url(r'^employee$', views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi)
]