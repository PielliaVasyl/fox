from django.contrib import admin

from entities.forms import AbstractTypeForm, EventTypeForm, PriceTypeForm, ExperienceLevelForm, RepeatsTypeForm, \
    DayOfTheWeekForm, ShopTypeForm, PlaceTypeForm
from entities.models import AbstractType, EventType, PriceType, ExperienceLevel, RepeatsType, DayOfTheWeek, \
    ShopType, PlaceType


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


class PlaceTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']
    form = PlaceTypeForm

admin.site.register(PlaceType, PlaceTypeAdmin)


class ShopTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']
    form = ShopTypeForm

admin.site.register(ShopType, ShopTypeAdmin)
