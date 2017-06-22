from django.contrib import admin

from entities.forms import AbstractTypeForm, EventTypeForm, PriceTypeForm, ExperienceLevelForm, RepeatsTypeForm, \
    DayOfTheWeekForm, ShopTypeForm, PlaceTypeForm
from entities.forms.types import CustomerServicesTypeForm, DanceStyleCountTypeForm, DanceStyleDistanceTypeForm
from entities.models import AbstractType, EventType, PriceType, ExperienceLevel, RepeatsType, DayOfTheWeek, \
    ShopType, PlaceType
from entities.models.types import CustomerServicesType, DanceStyleCountType, DanceStyleDistanceType


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


class CustomerServicesTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']
    form = CustomerServicesTypeForm

admin.site.register(CustomerServicesType, CustomerServicesTypeAdmin)


class DanceStyleCountTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']
    form = DanceStyleCountTypeForm

admin.site.register(DanceStyleCountType, DanceStyleCountTypeAdmin)


class DanceStyleDistanceTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']
    form = DanceStyleDistanceTypeForm

admin.site.register(DanceStyleDistanceType, DanceStyleDistanceTypeAdmin)
