"""woit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from items.views import ItemView, OfferView, UploadView
from accounts.views import AccountView, UserView

urlpatterns = [
    url(r'^items', ItemView.as_view()),
    url(r'^upload', UploadView.as_view(), name="upload"),
    url(r'^accounts', AccountView.as_view()),
    url(r'^login', AccountView.as_view()),
    url(r'^users', UserView.as_view()),
    url(r'^signup', UserView.as_view()),
    url(r'^admin/', admin.site.urls)
]

from django.conf import settings
from django.views.static import serve

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]