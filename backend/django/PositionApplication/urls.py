#from django.conf.urls import url
from django.urls import include,re_path as url
from PositionApplication import views



urlpatterns=[
    # Full database
    url(r'^position/position$', views.positionApi),                     # type: ignore 
    url(r'^position/position/([0-9]+)$', views.positionApi),            # type: ignore 

    # Query a table
    url(r'^position/table=(?P<query>[0-9A-Za-z]+)$', views.tableApi)    # type: ignore 
]