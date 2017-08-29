from django.contrib import admin

from entities.forms.posts import ChapterForm, AlbumForm, PlaylistForm, TracklistForm, \
    ArticleForm, PhotoForm, VideoForm, AudioForm, DanceDirectionForm, DanceStyleForm
from entities.models.posts import Chapter, Album, Playlist, Tracklist, Article, Photo, \
    Video, Audio, DanceDirection, DanceStyle


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


class DanceDirectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'get_tags', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = DanceDirectionForm

admin.site.register(DanceDirection, DanceDirectionAdmin)


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


class DanceStyleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'get_tags', 'image', 'author_of_post',
                    'link_to_author', 'group', 'get_count_types', 'get_distance_types', 'get_owners',
                    'get_contributors', 'author', 'created', 'updated']
    form = DanceStyleForm

admin.site.register(DanceStyle, DanceStyleAdmin)
