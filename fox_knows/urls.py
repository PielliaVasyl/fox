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
from django.views.generic.base import RedirectView

from home_page import views as home_page_views
from events import views as events_views
from map import views as map_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include([
        url(r'^$', home_page_views.index),
        url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
        ])),
        url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),

    ])),
    url(r'^feed/', include([
        url(r'^articles/', include([
            url(r'^$', home_page_views.index, name='feed_articles'),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', home_page_views.index, name='feed_articles_direction'),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index,
                    name='feed_articles_direction_city'),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index,
                name='feed_articles_city'),
        ])),

        url(r'^videos/', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', home_page_views.index),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
        ])),

        url(r'^audios/', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', home_page_views.index),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
        ])),

        url(r'^photos/', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', home_page_views.index),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
        ])),

        url(r'^should-know/', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', home_page_views.index),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
        ])),

        url(r'^dance-styles/', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', home_page_views.index),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
        ])),


        url(r'^$', RedirectView.as_view(pattern_name='feed_articles', permanent=True)),
        url(r'^(?:direction-(?P<direction_title>[\w-]+)/)', include([
            url(r'^$', RedirectView.as_view(pattern_name='feed_articles_direction', permanent=True)),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)$',
                RedirectView.as_view(pattern_name='feed_articles_direction_city', permanent=True)),
        ])),
        url(r'^(?:city-(?P<city_title>[\w-]+)/)?$',
            RedirectView.as_view(pattern_name='feed_articles_city', permanent=True)),

    ])),

    url(r'^map/', include([
        url(r'^places/', include([
            url(r'^$', map_views.places, name='map_places'),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', map_views.places, name='map_places_direction'),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', map_views.places,
                    name='map_places_direction_city'),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', map_views.places,
                name='map_places_city'),
        ])),


        url(r'^$', RedirectView.as_view(pattern_name='map_places', permanent=True)),
        url(r'^(?:direction-(?P<direction_title>[\w-]+)/)', include([
            url(r'^$', RedirectView.as_view(pattern_name='map_places_direction', permanent=True)),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)$',
                RedirectView.as_view(pattern_name='map_places_direction_city', permanent=True)),
        ])),
        url(r'^(?:city-(?P<city_title>[\w-]+)/)?$',
            RedirectView.as_view(pattern_name='map_places_city', permanent=True)),
    ])),

    url(r'^events/', include([
        url(r'^upcoming/', include([
            url(r'^$', events_views.upcoming, name='events_upcoming'),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', events_views.upcoming, name='events_upcoming_direction'),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', events_views.upcoming,
                    name='events_upcoming_direction_city'),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', events_views.upcoming,
                name='events_upcoming_city'),
        ])),

        url(r'^past/', include([
            url(r'^$', events_views.past),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', events_views.past),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', events_views.past),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', events_views.past),
        ])),

        url(r'^calendar/', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', home_page_views.index),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
        ])),

        url(r'^(?:event-(?P<event_id>\d+)/)', include([
            url(r'^$', events_views.event),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', events_views.event),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', events_views.event),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', events_views.event),
        ])),

        url(r'^$', RedirectView.as_view(pattern_name='events_upcoming', permanent=True)),
        url(r'^(?:direction-(?P<direction_title>[\w-]+)/)', include([
            url(r'^$', RedirectView.as_view(pattern_name='events_upcoming_direction', permanent=True)),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)$',
                RedirectView.as_view(pattern_name='events_upcoming_direction_city', permanent=True)),
        ])),
        url(r'^(?:city-(?P<city_title>[\w-]+)/)?$',
            RedirectView.as_view(pattern_name='events_upcoming_city', permanent=True)),

    ])),
    url(r'^ratings/', include([
        url(r'^$', home_page_views.index),
        url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
            url(r'^$', RedirectView.as_view(url='upcoming', permanent=True)),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
        ])),
        url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),

    ])),

]
