from django.contrib import admin

from entities.forms import EventForm
from entities.forms import PromoActionForm
from entities.models import AbstractEvent
from entities.models import Event
from entities.models import PromoAction


# class AbstractEventAdmin(admin.ModelAdmin):
#     list_display = ['title', 'get_directions', 'get_cities', 'local_classes', 'short_description', 'note', 'image',
#                     'video', 'start_date', 'end_date', 'status', 'get_links', 'get_owners', 'get_contributors',
#                     'author', 'created', 'updated']
#     form = AbstractEventForm
#
# admin.site.register(AbstractEvent, AbstractEventAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'local_classes', 'get_types', 'short_description', 'note',
                    'image', 'video', 'start_date', 'end_date', 'status', 'get_locations', 'get_price_types',
                    'get_experience_levels', 'repeats_type', 'get_schedule', 'get_links', 'get_owners',
                    'get_contributors', 'author', 'created', 'updated']
    form = EventForm

admin.site.register(Event, EventAdmin)


class PromoActionAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'local_classes', 'short_description', 'note', 'image',
                    'video', 'start_date', 'end_date', 'status', 'get_links', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = PromoActionForm

admin.site.register(PromoAction, PromoActionAdmin)
