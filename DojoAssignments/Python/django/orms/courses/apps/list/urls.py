from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^process$',views.process),
    url(r'^remove/(?P<ids>\d+)$',views.remove),
    url(r'^read/(?P<ids>\d+)$',views.read),
    url(r'^comment/(?P<ids>\d+)$',views.comment),
    url(r'^really/(?P<ids>\d+)$',views.really),
]
