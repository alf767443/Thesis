#from django.conf.urls import url
from django.urls import include,re_path as url
from RouteApplication import views

urlpatterns=[
    url(r'^route/table=route$', views.routeApi),
    url(r'^route/table=route([0-9]+)$', views.routeApi),

    url(r'^route/route$', views.routeApi),
    url(r'^route/route([0-9]+)$', views.routeApi),
]