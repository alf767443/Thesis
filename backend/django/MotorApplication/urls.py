from django.urls import include,re_path as url
from MotorApplication import views

urlpatterns=[
    # Full database
    url(r'^motor/motor$', views.motorApi),                          # type: ignore 
    url(r'^motor/motor/([0-9]+)$', views.motorApi),                 # type: ignore 

    # Query a table
    url(r'^motor/table=(?P<query>[0-9A-Za-z]+)$', views.tableApi)    # type: ignore 
]