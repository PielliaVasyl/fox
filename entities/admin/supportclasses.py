from django.contrib import admin

from entities.forms.supportclasses import EventLocalClassesForm, PageLocalClassesForm
from entities.models.supportclasses import EventLocalClasses, PageLocalClasses


class EventLocalClassesAdmin(admin.ModelAdmin):
    list_display = ['get_dance_styles', 'get_dance_directions', 'created', 'updated']
    form = EventLocalClassesForm

admin.site.register(EventLocalClasses, EventLocalClassesAdmin)


class PageLocalClassesAdmin(admin.ModelAdmin):
    list_display = ['get_dance_styles', 'get_dance_directions', 'created', 'updated']
    form = PageLocalClassesForm

admin.site.register(PageLocalClasses, PageLocalClassesAdmin)
