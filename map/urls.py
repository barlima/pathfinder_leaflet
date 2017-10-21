from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^multi_point/$', views.multi_point_path, name='multi_point_path'),
]
