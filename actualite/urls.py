from django.conf.urls import re_path

from . import views # import views so we can use them in urls.

app_name = "actualite"

urlpatterns = [
    re_path(r'^$', views.actualites, name="articles"), # "/product" will call the method "index" in "views.py"
    re_path(r'^(?P<article_id>[0-9a-f-]+)/$', views.see_more, name="detail"),
]