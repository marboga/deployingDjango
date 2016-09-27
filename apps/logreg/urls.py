from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='log_index'),
	url(r'^process$', views.process, name='log_process'),
	url(r'^logout$', views.logout, name='log_logout'),
]