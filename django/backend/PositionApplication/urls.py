#from django.conf.urls import url
from django.urls import include,re_path as url
from PositionApplication import views



urlpatterns=[
    url(r'^odometry$', views.odometryApi),
    url(r'^odometry/([0-9]+)$', views.odometryApi),
    
    url(r'^fiducial$', views.fiducialApi),
    url(r'^fiducial/([0-9]+)$', views.fiducialApi)

    url(r'^gyroscope$', views.gyroscopeApi),
    url(r'^gyroscope/([0-9]+)$', views.gyroscopeApi)
]