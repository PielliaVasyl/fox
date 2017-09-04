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
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from fox_knows import settings
from home_page import views as home_page_views
from events import views as events_views
from map import views as map_views
from entities.views import common as common_views
from feed import views as feed_views
from create import views as create_views

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
            url(r'^$', feed_views.articles, name='feed_articles'),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', feed_views.articles, name='feed_articles_direction'),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', feed_views.articles,
                    name='feed_articles_direction_city'),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', feed_views.articles,
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

        url(r'^links/', include([
            url(r'^$', feed_views.links),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', feed_views.links),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', feed_views.links),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', feed_views.links),
        ])),

        url(r'^organizations/', include([
            url(r'^$', feed_views.organizations),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', feed_views.organizations),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', feed_views.organizations),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', feed_views.organizations),
        ])),

        url(r'^persons/', include([
            url(r'^$', feed_views.persons),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', feed_views.persons),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', feed_views.persons),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', feed_views.persons),
        ])),

        url(r'^dance-styles/', include([
            url(r'^$', feed_views.dance_styles),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', feed_views.dance_styles),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', feed_views.dance_styles),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', feed_views.dance_styles),

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

        url(r'^schools/', include([
            url(r'^$', map_views.schools, name='map_schools'),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', map_views.schools, name='map_schools_direction'),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', map_views.schools,
                    name='map_schools_direction_city'),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', map_views.schools,
                name='map_schools_city'),
        ])),

        url(r'^shops/', include([
            url(r'^$', map_views.shops, name='map_shops'),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', map_views.shops, name='map_shops_direction'),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', map_views.shops,
                    name='map_shops_direction_city'),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', map_views.shops,
                name='map_shops_city'),
        ])),

        url(r'^services/', include([
            url(r'^$', map_views.services, name='map_services'),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', map_views.services, name='map_services_direction'),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', map_views.services,
                    name='map_services_direction_city'),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', map_views.services,
                name='map_services_city'),
        ])),

        url(r'^halls/', include([
            url(r'^$', map_views.halls, name='map_halls'),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', map_views.halls, name='map_halls_direction'),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', map_views.halls,
                    name='map_halls_direction_city'),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', map_views.halls,
                name='map_halls_city'),
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

        url(r'^calendar/', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', home_page_views.index),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
        ])),

        url(r'^promo-actions/', include([
            url(r'^$', home_page_views.index),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', home_page_views.index),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', home_page_views.index),
        ])),

        url(r'^past/', include([
            url(r'^$', events_views.past),
            url(r'^(?:direction-(?P<direction_title>[\w-]+)/)?', include([
                url(r'^$', events_views.past),
                url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', events_views.past),
            ])),
            url(r'^(?:city-(?P<city_title>[\w-]+)/)?$', events_views.past),
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

    # url(r'^profiles/', include([
    #     url(r'^$', RedirectView.as_view(pattern_name='profiles_profile', permanent=True)),
    #     url(r'^(?:direction-(?P<direction_title>[\w-]+)/)', include([
    #         url(r'^$', RedirectView.as_view(pattern_name='profiles_profile_direction', permanent=True)),
    #         url(r'^(?:city-(?P<city_title>[\w-]+)/)$',
    #             RedirectView.as_view(pattern_name='profiles_profile_direction_city', permanent=True)),
    #     ])),
    #     url(r'^(?:city-(?P<city_title>[\w-]+)/)?$',
    #         RedirectView.as_view(pattern_name='profiles_profile_city', permanent=True)),
    # ])),

    url(r'^create/', include([
        url(r'^$', create_views.create),
        url(r'^(?P<instance>[\w-]+)/', include([
            url(r'^$', create_views.create_instance),
            url(r'^(?P<attribute>[\w-]+)/$', create_views.create_attr)
        ]))
    ])),

    url(r'^(?P<entity>[\w-]+)-(?P<instance_id>\d+)/', include([
        url(r'^$', common_views.show_instance),
        url(r'^edit/$', common_views.edit_instance),
        # url(r'^delete/$', common_views.delete_instance),
        url(r'^(?P<attribute>[\w-]+)-(?P<attribute_id>\d+)/', include([
            # url(r'^$', common_views.show_instance_attr),
            url(r'^edit/$', common_views.edit_instance_attr),
            # url(r'^delete/$', common_views.delete_instance_attr),
        ])),
    ])),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
