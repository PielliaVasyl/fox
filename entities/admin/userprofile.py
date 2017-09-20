from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from entities.forms.userprofile import UserSettingsForm
from entities.models.userprofile import UserProfile, UserSettings


class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ['city', 'direction', 'created', 'updated']
    form = UserSettingsForm

admin.site.register(UserSettings, UserSettingsAdmin)


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(UserAdmin):
    list_display = ('username', "first_name", "last_name", "email", 'get_role', 'get_settings', "is_staff")
    inlines = (UserProfileInline, )

    def get_role(self, instance):
        return instance.userprofile.role
    get_role.short_description = 'Role'

    def get_settings(self, instance):
        return instance.userprofile.settings
    get_settings.short_description = 'Settings'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserProfileAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
