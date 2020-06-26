"""renaissance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.utils.translation import ugettext_lazy as _

from django.conf.urls.static import static
from django.views.generic import TemplateView

from actualite import views
from adhesion import views
from contact_us import views
from galerie import views
from newsletter import views
from titrologie import views
from forum_accounts.views import (login_view, register_view, logout_view)
from .views import home_page

app_name = "renaissance"
admin.site.site_header = _("Rénaissance")
admin.site.site_title = _("Building Craftsmen")

urlpatterns = [
    re_path(r'^$', home_page, name='home'),
    re_path(r'^actualites/', include('actualite.urls', namespace='actualite')),
    re_path(r'^adhesion/', include('adhesion.urls', namespace='adhesion')),
    re_path(r'^contactez-nous/', include('contact_us.urls', namespace='contact_us')),
    re_path(r'^nos-photos/', include('galerie.urls', namespace='galerie')),
    re_path(r'^notifications/', include('newsletter.urls', namespace='newsletter')),
    re_path(r'^revues-de-presse/', include('titrologie.urls', namespace='titrologie')),
    re_path(r'^forum-comments/', include('forum_comments.urls', namespace='comments')),
    re_path(r'^forum/', include('forum_post.urls', namespace='posts')),
    #re_path(r'^login/', login_view, name='login'),
    re_path(r'^jet/', include('jet.urls', 'jet')),
    re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('ad-website/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
