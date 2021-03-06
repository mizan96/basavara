"""app_root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from app_home.views import index, detail, profile, postTolet, postToletEdit, deleteTolet, toletOpen

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import (
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete)


urlpatterns = [
    url(r'^$', index),
    url(r'^profile/$', profile, name='profile'),
    url(r'^(?P<id>[0-9]+)/$', detail, name='detail'),
    url(r'^post/$', postTolet, name='postTolet'),
    url(r'^post/(?P<id>[0-9]+)/$', postToletEdit, name='postToletEdit'),
    url(r'^delete/(?P<id>[0-9]+)/$', deleteTolet, name='deleteTolet'),
    url(r'^open/(?P<id>[0-9]+)/$', toletOpen, name='toletOpen'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('app_account.urls')),
    url(r'^reset-password/$', password_reset, name='password_reset'),
    url(r'reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'reset-password/complete/$', password_reset_complete,
        name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + \
    [url(r'^.*$', TemplateView.as_view(template_name='404.html'))]
