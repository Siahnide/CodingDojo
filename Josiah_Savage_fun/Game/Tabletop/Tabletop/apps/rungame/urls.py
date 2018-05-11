from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^choose$', views.choose),
    url(r'^choose/char', views.choosechar),
]