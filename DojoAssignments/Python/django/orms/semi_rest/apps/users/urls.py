from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^show$', views.show),
    url(r'^delete/(?P<ids>\d+)$', views.delete),
    url(r'^edit/(?P<ids>\d+)$', views.edit),
    url(r'^process/(?P<ids>\d+)$', views.processids),
    url(r'^show/(?P<ids>\d+)$', views.user),
]
