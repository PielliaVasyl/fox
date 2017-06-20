from django.contrib import admin

from entities.forms.links import AbstractLinkForm, AbstractEventLinkForm, AbstractPageLinkForm, ArticleLinkForm, \
    AudioLinkForm, PhotoLinkForm, PlaylistLinkForm, VideoLinkForm

from entities.models.links import AbstractEventLink, AbstractLink, AbstractPageLink, ArticleLink, AudioLink, \
    PhotoLink, PlaylistLink, VideoLink


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
