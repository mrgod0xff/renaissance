from django.conf.urls import re_path
from django.contrib import admin

from .views import poster_auth, poster_reg, post_list, post_create, post_detail, post_update, post_delete

app_name = "posts"

urlpatterns = [
	re_path(r'^$', post_list, name='list'),
	re_path(r'^create/$', post_create, name='create'),
    re_path(r'^je-me-connecte/$', poster_auth, name='authentification'),
    re_path(r'^je-m-inscris/$', poster_reg, name="registration"),
    re_path(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name="delete"),
]