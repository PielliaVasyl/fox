from django.contrib import admin

from entities.forms import AbstractLocationForm
from entities.forms import AbstractMapCoordinatesForm, PlaceMapCoordinatesForm, SchoolMapCoordinatesForm, \
    OrganizationMapCoordinatesForm, ShopMapCoordinatesForm, HallMapCoordinatesForm, EventLocationForm, \
    PlaceLocationForm, SchoolLocationForm, OrganizationLocationForm, ShopLocationForm, HallLocationForm
from entities.models import AbstractMapCoordinates, PlaceMapCoordinates, SchoolMapCoordinates, \
    OrganizationMapCoordinates, ShopMapCoordinates, HallMapCoordinates, AbstractLocation, \
    EventLocation, PlaceLocation, SchoolLocation, OrganizationLocation, ShopLocation, HallLocation


class AbstractMapCoordinatesAdmin(admin.ModelAdmin):
    list_display = ['lat', 'lng', 'author', 'created', 'updated']
    form = AbstractMapCoordinatesForm

admin.site.register(AbstractMapCoordinates, AbstractMapCoordinatesAdmin)


class PlaceMapCoordinatesAdmin(admin.ModelAdmin):
    list_display = ['lat', 'lng', 'author', 'created', 'updated']
    form = PlaceMapCoordinatesForm

admin.site.register(PlaceMapCoordinates, PlaceMapCoordinatesAdmin)


class SchoolMapCoordinatesAdmin(admin.ModelAdmin):
    list_display = ['lat', 'lng', 'author', 'created', 'updated']
    form = SchoolMapCoordinatesForm

admin.site.register(SchoolMapCoordinates, SchoolMapCoordinatesAdmin)


class OrganizationMapCoordinatesAdmin(admin.ModelAdmin):
    list_display = ['lat', 'lng', 'author', 'created', 'updated']
    form = OrganizationMapCoordinatesForm

admin.site.register(OrganizationMapCoordinates, OrganizationMapCoordinatesAdmin)


class ShopMapCoordinatesAdmin(admin.ModelAdmin):
    list_display = ['lat', 'lng', 'author', 'created', 'updated']
    form = ShopMapCoordinatesForm

admin.site.register(ShopMapCoordinates, ShopMapCoordinatesAdmin)


class HallMapCoordinatesAdmin(admin.ModelAdmin):
    list_display = ['lat', 'lng', 'author', 'created', 'updated']
    form = HallMapCoordinatesForm

admin.site.register(HallMapCoordinates, HallMapCoordinatesAdmin)


class AbstractLocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'note', 'author', 'created', 'updated']
    form = AbstractLocationForm

admin.site.register(AbstractLocation, AbstractLocationAdmin)


class EventLocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'note', 'author', 'created', 'updated']
    form = EventLocationForm

admin.site.register(EventLocation, EventLocationAdmin)


class PlaceLocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'note', 'coordinates', 'author', 'created', 'updated']
    form = PlaceLocationForm

admin.site.register(PlaceLocation, PlaceLocationAdmin)


class SchoolLocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'note', 'coordinates', 'author', 'created', 'updated']
    form = SchoolLocationForm

admin.site.register(SchoolLocation, SchoolLocationAdmin)


class OrganizationLocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'note', 'coordinates', 'author', 'created', 'updated']
    form = OrganizationLocationForm

admin.site.register(OrganizationLocation, OrganizationLocationAdmin)


class ShopLocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'note', 'coordinates', 'author', 'created', 'updated']
    form = ShopLocationForm

admin.site.register(ShopLocation, ShopLocationAdmin)


class HallLocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'note', 'coordinates', 'author', 'created', 'updated']
    form = HallLocationForm

admin.site.register(HallLocation, HallLocationAdmin)
