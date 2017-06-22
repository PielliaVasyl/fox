from django.contrib import admin

from entities.forms.classes import AbstractClassForm, AbstractGlobalClassForm, AbstractLocalClassForm, CityForm, \
    DirectionForm, DanceDirectionClassForm, DanceStyleClassForm
from entities.models.classes import AbstractClass, AbstractGlobalClass, AbstractLocalClass, City, \
    DanceDirectionClass, DanceStyleClass, Direction


class AbstractClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    form = AbstractClassForm

admin.site.register(AbstractClass, AbstractClassAdmin)


class AbstractGlobalClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    form = AbstractGlobalClassForm

admin.site.register(AbstractGlobalClass, AbstractGlobalClassAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    form = CityForm

admin.site.register(City, CityAdmin)


class DirectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    form = DirectionForm

admin.site.register(Direction, DirectionAdmin)


class AbstractLocalClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'created', 'updated']
    form = AbstractLocalClassForm

admin.site.register(AbstractLocalClass, AbstractLocalClassAdmin)


class DanceDirectionClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'created', 'updated']
    form = DanceDirectionClassForm

admin.site.register(DanceDirectionClass, DanceDirectionClassAdmin)


class DanceStyleClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'dance_direction', 'created', 'updated']
    form = DanceStyleClassForm

admin.site.register(DanceStyleClass, DanceStyleClassAdmin)
