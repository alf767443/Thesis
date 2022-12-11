#from django.conf.urls import url
from django.urls import include,re_path as url
from PositionApplication import views



urlpatterns=[
    url(r'^position/table=odometry$', views.odometryApi),
    url(r'^position/table=odometry/([0-9]+)$', views.odometryApi),
    
    url(r'^position/table=fiducialmark$', views.fiducialApi),
    url(r'^position/table=fiducialmark/([0-9]+)$', views.fiducialApi),

    url(r'^position/table=gyroscope$', views.gyroscopeApi),
    url(r'^position/table=gyroscope/([0-9]+)$', views.gyroscopeApi),

    url(r'^position/table=globalposition$', views.globalpositionApi),
    url(r'^position/table=globalposition/([0-9]+)$', views.globalpositionApi),

    url(r'^position/position$', views.positionApi),
    url(r'^position/position/([0-9]+)$', views.positionApi)

]