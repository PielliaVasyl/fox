"""fox_knows URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from home_page import views as home_page_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include([
        url(r'^$', home_page_views.index),
        url(r'^(?:city-(?P<city_title>[\w-]+)/)?', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?$', home_page_views.index),
        ])),
        url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?$', home_page_views.index),

    ])),
    url(r'^feed/', include([
        url(r'^$', home_page_views.index),
        url(r'^(?:city-(?P<city_title>[\w-]+)/)?', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?$', home_page_views.index),
        ])),
        url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?$', home_page_views.index),

    ])),
    url(r'^map/', include([
        url(r'^$', home_page_views.index),
        url(r'^(?:city-(?P<city_title>[\w-]+)/)?', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?$', home_page_views.index),
        ])),
        url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?$', home_page_views.index),

    ])),
    url(r'^events/', include([
        url(r'^$', home_page_views.index),
        url(r'^(?:city-(?P<city_title>[\w-]+)/)?', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?$', home_page_views.index),
        ])),
        url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?$', home_page_views.index),

    ])),
    url(r'^ratings/', include([
        url(r'^$', home_page_views.index),
        url(r'^(?:city-(?P<city_title>[\w-]+)/)?', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?$', home_page_views.index),
        ])),
        url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?$', home_page_views.index),

    ])),

]
