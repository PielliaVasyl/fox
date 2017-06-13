from django.contrib import admin

from entities.forms import AbstractLinkForm, AbstractEventLinkForm, EventLocalClassesForm, AbstractPageLinkForm, \
    PageLocalClassesForm
from entities.models import AbstractEventLink
from entities.models import AbstractLink
from entities.models import EventLocalClasses
from entities.models import AbstractPageLink
from entities.models import PageLocalClasses


class AbstractLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = AbstractLinkForm

admin.site.register(AbstractLink, AbstractLinkAdmin)


class AbstractEventLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = AbstractEventLinkForm

admin.site.register(AbstractEventLink, AbstractEventLinkAdmin)


class AbstractPageLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = AbstractPageLinkForm

admin.site.register(AbstractPageLink, AbstractPageLinkAdmin)


class EventLocalClassesAdmin(admin.ModelAdmin):
    list_display = ['get_dance_styles', 'get_dance_directions', 'created', 'updated']
    form = EventLocalClassesForm

admin.site.register(EventLocalClasses, EventLocalClassesAdmin)


class PageLocalClassesAdmin(admin.ModelAdmin):
    list_display = ['get_dance_styles', 'get_dance_directions', 'created', 'updated']
    form = PageLocalClassesForm

admin.site.register(PageLocalClasses, PageLocalClassesAdmin)
