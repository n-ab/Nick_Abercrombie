from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^logging_in/(?P<user_id>\d+)/success$', views.success),
    url(r'^adduser', views.adduser),
    url(r'^login', views.login)
]


