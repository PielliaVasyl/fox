from django.contrib import admin

from entities.forms.supportclasses import AbstractLinkForm, AbstractEventLinkForm, EventLocalClassesForm, \
    AbstractTypeForm, EventTypeForm, PriceTypeForm, ExperienceLevelForm, RepeatsTypeForm, DayOfTheWeekForm, \
    AbstractLocationForm, EventLocationForm
from entities.models import AbstractEventLink
from entities.models import AbstractLink
from entities.models import AbstractLocation
from entities.models import AbstractType
from entities.models import DayOfTheWeek
from entities.models import EventLocalClasses
from entities.models import EventLocation
from entities.models import EventType
from entities.models import ExperienceLevel
from entities.models import PriceType
from entities.models import RepeatsType


class AbstractLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = AbstractLinkForm

admin.site.register(AbstractLink, AbstractLinkAdmin)


class AbstractEventLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = AbstractEventLinkForm

admin.site.register(AbstractEventLink, AbstractEventLinkAdmin)


class EventLocalClassesAdmin(admin.ModelAdmin):
    list_display = ['get_dance_styles', 'get_dance_directions', 'created', 'updated']
    form = EventLocalClassesForm

admin.site.register(EventLocalClasses, EventLocalClassesAdmin)


class AbstractTypeAdmin(admin.ModelAdmin):
    list_display = ['description', 'created', 'updated']
    form = AbstractTypeForm

admin.site.register(AbstractType, AbstractTypeAdmin)


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']
    form = EventTypeForm

admin.site.register(EventType, EventTypeAdmin)


class PriceTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']
    form = PriceTypeForm

admin.site.register(PriceType, PriceTypeAdmin)


class ExperienceLevelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']
    form = ExperienceLevelForm

admin.site.register(ExperienceLevel, ExperienceLevelAdmin)


class RepeatsTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']
    form = RepeatsTypeForm

admin.site.register(RepeatsType, RepeatsTypeAdmin)


class DayOfTheWeekAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']
    form = DayOfTheWeekForm

admin.site.register(DayOfTheWeek, DayOfTheWeekAdmin)


class AbstractLocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'note', 'author', 'created', 'updated']
    form = AbstractLocationForm

admin.site.register(AbstractLocation, AbstractLocationAdmin)


class EventLocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'note', 'author', 'created', 'updated']
    form = EventLocationForm

admin.site.register(EventLocation, EventLocationAdmin)
