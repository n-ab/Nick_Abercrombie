from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_adduser$', views.process_adduser),
    url(r'^process_login$', views.process_login),
    url(r'^books$', views.books),
    url(r'^books/(?P<id>\d+)/$', views.process_addbook),
    url(r'^addnew$', views.addnew),
    url(r'^process_addbook$', views.process_addbook),
]
