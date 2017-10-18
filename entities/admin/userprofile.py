from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from entities.forms.userprofile import UserSettingsForm
from entities.models.userprofile import UserProfile, UserSettings


class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ['city', 'direction', 'created', 'updated']
    form = UserSettingsForm

admin.site.register(UserSettings, UserSettingsAdmin)


admin.site.register(UserProfile, UserAdmin)
