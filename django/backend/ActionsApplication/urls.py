#from django.conf.urls import url
from django.urls import include,re_path as url
from ActionsApplication import views

urlpatterns=[
    url(r'^actions/actions$', views.actionsApi),
    url(r'^actions/actions/([0-9]+)$', views.actionsApi),
]