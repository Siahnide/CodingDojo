from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'add$',views.add),
    url(r'redirect$',views.show),
    url(r'process$',views.process),
    url(r'delete/(?P<ids>\d+)$',views.delete),
    url(r'review/(?P<ids>\d+)$',views.review),
    url(r'show$',views.show),
    url(r'user/(?P<ids>\w+)$',views.user),
    url(r'(?P<ids>\w+)$',views.book),
]