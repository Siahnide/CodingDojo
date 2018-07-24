from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$',views.menu),
    url(r'^single$',views.single),
    url(r'^item$',views.item),
    url(r'^add_item$',views.add_item),
    url(r'^create_char$',views.create_char),
    url(r'^load_char$',views.load_char),
    url(r'^del_char$',views.del_char),
]