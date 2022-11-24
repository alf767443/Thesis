#from django.conf.urls import url
from django.urls import include,re_path as url
from PositionApplication import views



urlpatterns=[
    url(r'^position/odometry$', views.odometryApi),
    url(r'^position/odometry/([0-9]+)$', views.odometryApi),
    
    url(r'^position/fiducial$', views.fiducialApi),
    url(r'^position/fiducial/([0-9]+)$', views.fiducialApi),

    url(r'^position/gyroscope$', views.gyroscopeApi),
    url(r'^position/gyroscope/([0-9]+)$', views.gyroscopeApi),

    url(r'^position/globalposition$', views.globalpositionApi),
    url(r'^position/globalposition/([0-9]+)$', views.globalpositionApi)
]