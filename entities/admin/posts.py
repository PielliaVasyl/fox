from django.contrib import admin

from entities.forms.posts import AbstractPostGroupForm, ChapterForm, AlbumForm, PlaylistForm, TracklistForm, \
    AbstractPostForm, ArticleForm, PhotoForm, VideoForm, AudioForm
from entities.models.posts import AbstractPostGroup, Chapter, Album, Playlist, Tracklist, AbstractPost, Article, Photo, \
    Video, Audio


class AbstractPostGroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'description', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = AbstractPostGroupForm

admin.site.register(AbstractPostGroup, AbstractPostGroupAdmin)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'description', 'get_tags', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = ChapterForm

admin.site.register(Chapter, ChapterAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'description', 'get_tags', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = AlbumForm

admin.site.register(Album, AlbumAdmin)


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'description', 'get_tags', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = PlaylistForm

admin.site.register(Playlist, PlaylistAdmin)


class TracklistAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'description', 'get_tags', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = TracklistForm

admin.site.register(Tracklist, TracklistAdmin)


class AbstractPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'description', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = AbstractPostForm

admin.site.register(AbstractPost, AbstractPostAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'description', 'get_tags', 'link', 'image', 'is_linked_article',
                    'get_owners', 'author_of_post', 'get_groups', 'get_contributors', 'author', 'created', 'updated']
    form = ArticleForm

admin.site.register(Article, ArticleAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'description', 'get_tags', 'link', 'image', 'get_groups',
                    'get_owners', 'get_contributors', 'author', 'created', 'updated']
    form = PhotoForm

admin.site.register(Photo, PhotoAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'description', 'get_tags', 'link', 'get_groups', 'get_owners',
                    'get_contributors', 'author', 'created', 'updated']
    form = VideoForm

admin.site.register(Video, VideoAdmin)


class AudioAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'description', 'get_tags', 'link', 'get_groups', 'get_owners',
                    'get_contributors', 'author', 'created', 'updated']
    form = AudioForm

admin.site.register(Audio, AudioAdmin)
