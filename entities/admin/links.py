from django.contrib import admin

from entities.forms.links import AbstractLinkForm, ArticleLinkForm, \
    AudioLinkForm, PhotoLinkForm, PlaylistLinkForm, VideoLinkForm, PlaceLinkForm, SchoolLinkForm, OrganizationLinkForm, \
    TeacherLinkForm, PersonLinkForm, ShopLinkForm, CustomerServicesLinkForm, HallLinkForm, ResourceLinkForm, \
    EventLinkForm, PromoActionLinkForm

from entities.models.links import AbstractLink, ArticleLink, AudioLink, \
    PhotoLink, PlaylistLink, VideoLink, PlaceLink, SchoolLink, OrganizationLink, TeacherLink, PersonLink, ShopLink, \
    CustomerServicesLink, HallLink, ResourceLink, EventLink, PromoActionLink


# class AbstractLinkAdmin(admin.ModelAdmin):
#     list_display = ['link', 'created', 'updated']
#     form = AbstractLinkForm
#
# admin.site.register(AbstractLink, AbstractLinkAdmin)


class EventLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = EventLinkForm

admin.site.register(EventLink, EventLinkAdmin)


class PromoActionLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = PromoActionLinkForm

admin.site.register(PromoActionLink, PromoActionLinkAdmin)

# class AbstractPageLinkAdmin(admin.ModelAdmin):
#     list_display = ['link', 'created', 'updated']
#     form = AbstractPageLinkForm
#
# admin.site.register(AbstractPageLink, AbstractPageLinkAdmin)


class PlaceLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = PlaceLinkForm

admin.site.register(PlaceLink, PlaceLinkAdmin)


class SchoolLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = SchoolLinkForm

admin.site.register(SchoolLink, SchoolLinkAdmin)


class OrganizationLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = OrganizationLinkForm

admin.site.register(OrganizationLink, OrganizationLinkAdmin)


class TeacherLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = TeacherLinkForm

admin.site.register(TeacherLink, TeacherLinkAdmin)


class PersonLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = PersonLinkForm

admin.site.register(PersonLink, PersonLinkAdmin)


class ShopLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = ShopLinkForm

admin.site.register(ShopLink, ShopLinkAdmin)


class CustomerServicesLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = CustomerServicesLinkForm

admin.site.register(CustomerServicesLink, CustomerServicesLinkAdmin)


class HallLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = HallLinkForm

admin.site.register(HallLink, HallLinkAdmin)


class ResourceLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = ResourceLinkForm

admin.site.register(ResourceLink, ResourceLinkAdmin)


class PlaylistLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = PlaylistLinkForm

admin.site.register(PlaylistLink, PlaylistLinkAdmin)


class ArticleLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = ArticleLinkForm

admin.site.register(ArticleLink, ArticleLinkAdmin)


class PhotoLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = PhotoLinkForm

admin.site.register(PhotoLink, PhotoLinkAdmin)


class VideoLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = VideoLinkForm

admin.site.register(VideoLink, VideoLinkAdmin)


class AudioLinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'created', 'updated']
    form = AudioLinkForm

admin.site.register(AudioLink, AudioLinkAdmin)
