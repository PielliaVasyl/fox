from django.contrib import admin

from entities.forms import AbstractSocialLinkForm, SocialLinkFBForm, SocialLinkVKForm, SocialLinkInstagramForm, \
    SocialLinkTwitterForm, SocialsForm, PhoneNumberForm, AbstractContactsForm, SchoolContactsForm, \
    OrganizationContactsForm, TeacherContactsForm, PersonContactsForm, ShopContactsForm, HallContactsForm, \
    ResourceContactsForm
from entities.models import AbstractSocialLink, SocialLinkFB, SocialLinkVK, SocialLinkInstagram, \
    SocialLinkTwitter, Socials, PhoneNumber, AbstractContacts, SchoolContacts, OrganizationContacts, TeacherContacts, \
    PersonContacts, ShopContacts, HallContacts, ResourceContacts


# class AbstractSocialLinkAdmin(admin.ModelAdmin):
#     list_display = ['link', 'author', 'created', 'updated']
#     form = AbstractSocialLinkForm
#
# admin.site.register(AbstractSocialLink, AbstractSocialLinkAdmin)


class SocialLinkFBAdmin(admin.ModelAdmin):
    list_display = ['link', 'author', 'created', 'updated']
    form = SocialLinkFBForm

admin.site.register(SocialLinkFB, SocialLinkFBAdmin)


class SocialLinkVKAdmin(admin.ModelAdmin):
    list_display = ['link', 'author', 'created', 'updated']
    form = SocialLinkVKForm

admin.site.register(SocialLinkVK, SocialLinkVKAdmin)


class SocialLinkInstagramAdmin(admin.ModelAdmin):
    list_display = ['link', 'author', 'created', 'updated']
    form = SocialLinkInstagramForm

admin.site.register(SocialLinkInstagram, SocialLinkInstagramAdmin)


class SocialLinkTwitterAdmin(admin.ModelAdmin):
    list_display = ['link', 'author', 'created', 'updated']
    form = SocialLinkTwitterForm

admin.site.register(SocialLinkTwitter, SocialLinkTwitterAdmin)


class SocialsAdmin(admin.ModelAdmin):
    list_display = ['get_fbs', 'get_vks', 'get_instagrams', 'get_twitters', 'author', 'created', 'updated']
    form = SocialsForm

admin.site.register(Socials, SocialsAdmin)


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'author', 'created', 'updated']
    form = PhoneNumberForm

admin.site.register(PhoneNumber, PhoneNumberAdmin)


# class AbstractContactsAdmin(admin.ModelAdmin):
#     list_display = ['get_phone_numbers', 'socials', 'author', 'created', 'updated']
#     form = AbstractContactsForm
#
# admin.site.register(AbstractContacts, AbstractContactsAdmin)


class SchoolContactsAdmin(admin.ModelAdmin):
    list_display = ['get_phone_numbers', 'socials', 'author', 'created', 'updated']
    form = SchoolContactsForm

admin.site.register(SchoolContacts, SchoolContactsAdmin)


class OrganizationContactsAdmin(admin.ModelAdmin):
    list_display = ['get_phone_numbers', 'socials', 'author', 'created', 'updated']
    form = OrganizationContactsForm

admin.site.register(OrganizationContacts, OrganizationContactsAdmin)


class TeacherContactsAdmin(admin.ModelAdmin):
    list_display = ['get_phone_numbers', 'socials', 'author', 'created', 'updated']
    form = TeacherContactsForm

admin.site.register(TeacherContacts, TeacherContactsAdmin)


class PersonContactsAdmin(admin.ModelAdmin):
    list_display = ['get_phone_numbers', 'socials', 'author', 'created', 'updated']
    form = PersonContactsForm

admin.site.register(PersonContacts, PersonContactsAdmin)


class ShopContactsAdmin(admin.ModelAdmin):
    list_display = ['get_phone_numbers', 'socials', 'author', 'created', 'updated']
    form = ShopContactsForm

admin.site.register(ShopContacts, ShopContactsAdmin)


class HallContactsAdmin(admin.ModelAdmin):
    list_display = ['get_phone_numbers', 'socials', 'author', 'created', 'updated']
    form = HallContactsForm

admin.site.register(HallContacts, HallContactsAdmin)


class ResourceContactsAdmin(admin.ModelAdmin):
    list_display = ['get_phone_numbers', 'socials', 'author', 'created', 'updated']
    form = ResourceContactsForm

admin.site.register(ResourceContacts, ResourceContactsAdmin)
