from django.contrib import admin

from entities.forms.owns import SchoolOwnsForm, OrganizationOwnsForm, TeacherOwnsForm, PersonOwnsForm, ShopOwnsForm, \
    CustomerServicesOwnsForm, HallOwnsForm, ResourceOwnsForm, PlaceOwnsForm
from entities.models.owns import SchoolOwns, OrganizationOwns, TeacherOwns, PersonOwns, ShopOwns, \
    CustomerServicesOwns, HallOwns, ResourceOwns, PlaceOwns

OWNS_LIST_DISPLAY = ['events', 'promo_actions', 'articles', 'chapters', 'photos', 'albums', 'videos', 'playlists',
                     'audios', 'tracklists', 'created', 'updated']


class PlaceOwnsAdmin(admin.ModelAdmin):
    list_display = OWNS_LIST_DISPLAY
    form = PlaceOwnsForm

admin.site.register(PlaceOwns, PlaceOwnsAdmin)


class SchoolOwnsAdmin(admin.ModelAdmin):
    list_display = OWNS_LIST_DISPLAY
    form = SchoolOwnsForm

admin.site.register(SchoolOwns, SchoolOwnsAdmin)


class OrganizationOwnsAdmin(admin.ModelAdmin):
    list_display = OWNS_LIST_DISPLAY
    form = OrganizationOwnsForm

admin.site.register(OrganizationOwns, OrganizationOwnsAdmin)


class TeacherOwnsAdmin(admin.ModelAdmin):
    list_display = OWNS_LIST_DISPLAY
    form = TeacherOwnsForm

admin.site.register(TeacherOwns, TeacherOwnsAdmin)


class PersonOwnsAdmin(admin.ModelAdmin):
    list_display = OWNS_LIST_DISPLAY
    form = PersonOwnsForm

admin.site.register(PersonOwns, PersonOwnsAdmin)


class ShopOwnsAdmin(admin.ModelAdmin):
    list_display = OWNS_LIST_DISPLAY
    form = ShopOwnsForm

admin.site.register(ShopOwns, ShopOwnsAdmin)


class CustomerServicesOwnsAdmin(admin.ModelAdmin):
    list_display = OWNS_LIST_DISPLAY
    form = CustomerServicesOwnsForm

admin.site.register(CustomerServicesOwns, CustomerServicesOwnsAdmin)


class HallOwnsAdmin(admin.ModelAdmin):
    list_display = OWNS_LIST_DISPLAY
    form = HallOwnsForm

admin.site.register(HallOwns, HallOwnsAdmin)


class ResourceOwnsAdmin(admin.ModelAdmin):
    list_display = OWNS_LIST_DISPLAY
    form = ResourceOwnsForm

admin.site.register(ResourceOwns, ResourceOwnsAdmin)
