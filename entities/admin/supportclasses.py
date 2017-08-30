from django.contrib import admin

from entities.forms.supportclasses import EventLocalClassesForm, PageLocalClassesForm, PromoActionLocalClassesForm, \
    PlaceLocalClassesForm, SchoolLocalClassesForm, OrganizationLocalClassesForm, TeacherLocalClassesForm, \
    PersonLocalClassesForm
from entities.models.supportclasses import EventLocalClasses, PageLocalClasses, PromoActionLocalClasses, \
    PlaceLocalClasses, SchoolLocalClasses, OrganizationLocalClasses, TeacherLocalClasses, PersonLocalClasses

LOCAL_CLASSES_LIST_DISPLAY = ['get_dance_styles', 'get_dance_directions', 'created', 'updated']


class EventLocalClassesAdmin(admin.ModelAdmin):
    list_display = LOCAL_CLASSES_LIST_DISPLAY
    form = EventLocalClassesForm

admin.site.register(EventLocalClasses, EventLocalClassesAdmin)


class PromoActionLocalClassesAdmin(admin.ModelAdmin):
    list_display = LOCAL_CLASSES_LIST_DISPLAY
    form = PromoActionLocalClassesForm

admin.site.register(PromoActionLocalClasses, PromoActionLocalClassesAdmin)


class PageLocalClassesAdmin(admin.ModelAdmin):
    list_display = LOCAL_CLASSES_LIST_DISPLAY
    form = PageLocalClassesForm

admin.site.register(PageLocalClasses, PageLocalClassesAdmin)


class PlaceLocalClassesAdmin(admin.ModelAdmin):
    list_display = LOCAL_CLASSES_LIST_DISPLAY
    form = PlaceLocalClassesForm

admin.site.register(PlaceLocalClasses, PlaceLocalClassesAdmin)


class SchoolLocalClassesAdmin(admin.ModelAdmin):
    list_display = LOCAL_CLASSES_LIST_DISPLAY
    form = SchoolLocalClassesForm

admin.site.register(SchoolLocalClasses, SchoolLocalClassesAdmin)


class OrganizationLocalClassesAdmin(admin.ModelAdmin):
    list_display = LOCAL_CLASSES_LIST_DISPLAY
    form = OrganizationLocalClassesForm

admin.site.register(OrganizationLocalClasses, OrganizationLocalClassesAdmin)


class TeacherLocalClassesAdmin(admin.ModelAdmin):
    list_display = LOCAL_CLASSES_LIST_DISPLAY
    form = TeacherLocalClassesForm

admin.site.register(TeacherLocalClasses, TeacherLocalClassesAdmin)


class PersonLocalClassesAdmin(admin.ModelAdmin):
    list_display = LOCAL_CLASSES_LIST_DISPLAY
    form = PersonLocalClassesForm

admin.site.register(PersonLocalClasses, PersonLocalClassesAdmin)
