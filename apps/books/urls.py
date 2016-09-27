from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='book_index'),
	url(r'^newBook$', views.newBook, name='book_new'),
	url(r'^createBook$', views.addBook, name='book_add'),
	url(r'^user/(?P<id>\d)$', views.userBook, name='book_user'),
	url(r'^book/(?P<id>\d)$', views.show, name='book_show'),
]