#from django.conf.urls import url
from django.urls import include,re_path as url
from DecisionsApplication import views

urlpatterns=[
    url(r'^decisions/administrator$', views.administratorApi),
    url(r'^decisions/administrator/([0-9]+)$', views.administratorApi),

    url(r'^decisions/remote$', views.remoteApi),
    url(r'^decisions/remote/([0-9]+)$', views.remoteApi),
        
    url(r'^decisions/robot$', views.robotApi),
    url(r'^decisions/robot/([0-9]+)$', views.robotApi),
]