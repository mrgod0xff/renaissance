from django.conf.urls import re_path

from . import views # import views so we can use them in urls.

app_name = "contact_us"

urlpatterns = [
    re_path(r'^$', views.contactUs, name="contact"), # "/product" will call the method "index" in "views.py"
    #re_path(r'^(?P<product_id>[0-9]+)/$', views.detail, name="detail"),
]