from django.contrib import admin

from entities.forms import AbstractClassForm
from entities.forms import AbstractGlobalClassForm
from entities.forms import AbstractLocalClassForm
from entities.forms import CityForm
from entities.forms import DanceDirectionForm
from entities.forms import DanceStyleForm
from entities.forms import DirectionForm
from entities.models import AbstractClass
from entities.models import AbstractGlobalClass
from entities.models import AbstractLocalClass
from entities.models import City
from entities.models import DanceDirection
from entities.models import DanceStyle
from entities.models import Direction


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


class DanceDirectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'created', 'updated']
    form = DanceDirectionForm

admin.site.register(DanceDirection, DanceDirectionAdmin)


class DanceStyleAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'dance_direction', 'created', 'updated']
    form = DanceStyleForm

admin.site.register(DanceStyle, DanceStyleAdmin)
