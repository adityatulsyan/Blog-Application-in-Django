#from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^blogs/$', views.index2, name = 'index'),
	url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),]