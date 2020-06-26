from django.conf.urls import re_path

from . import views # import views so we can use them in urls.

app_name = "titrologie"

urlpatterns = [
    re_path(r'^$', views.list_revue, name="revue"),
]