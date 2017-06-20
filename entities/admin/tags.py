from django.contrib import admin

from entities.forms.tags import AbstractTagForm, AlbumTagForm, ArticleTagForm, AudioTagForm, ChapterTagForm, \
    CityTagForm, DanceDirectionTagForm, DanceStyleCountTagForm, DanceStyleDistanceTagForm, DanceStyleTagForm, \
    DanceTagForm, DirectionTagForm, GlobalTagForm, LocalTagForm, PhotoTagForm, PlaylistTagForm, PostGroupTagForm, \
    PostTagForm, TracklistTagForm, VideoTagForm

from entities.models.tags import AbstractTag, AlbumTag, ArticleTag, AudioTag, ChapterTag, CityTag, DanceDirectionTag, \
    DanceStyleCountTag, DanceStyleDistanceTag, DanceStyleTag, DanceTag, DirectionTag, GlobalTag, LocalTag, PhotoTag, \
    PlaylistTag, PostGroupTag, PostTag, TracklistTag, VideoTag


class AbstractTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    form = AbstractTagForm

admin.site.register(AbstractTag, AbstractTagAdmin)


class GlobalTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    form = GlobalTagForm

admin.site.register(GlobalTag, GlobalTagAdmin)


class CityTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    form = CityTagForm

admin.site.register(CityTag, CityTagAdmin)


class DirectionTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'direction', 'created', 'updated']
    form = DirectionTagForm

admin.site.register(DirectionTag, DirectionTagAdmin)


class LocalTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    form = LocalTagForm

admin.site.register(LocalTag, LocalTagAdmin)


class DanceTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'direction', 'created', 'updated']
    form = DanceTagForm

admin.site.register(DanceTag, DanceTagAdmin)


class DanceStyleTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'direction', 'created', 'updated']
    form = DanceStyleTagForm

admin.site.register(DanceStyleTag, DanceStyleTagAdmin)


class DanceStyleCountTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'direction', 'created', 'updated']
    form = DanceStyleCountTagForm

admin.site.register(DanceStyleCountTag, DanceStyleCountTagAdmin)


class DanceStyleDistanceTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'direction', 'created', 'updated']
    form = DanceStyleDistanceTagForm

admin.site.register(DanceStyleDistanceTag, DanceStyleDistanceTagAdmin)


class DanceDirectionTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'direction', 'created', 'updated']
    form = DanceDirectionTagForm

admin.site.register(DanceDirectionTag, DanceDirectionTagAdmin)


class PostTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'is_all_directions', 'created', 'updated']
    form = PostTagForm

admin.site.register(PostTag, PostTagAdmin)


class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'is_all_directions', 'created', 'updated']
    form = ArticleTagForm

admin.site.register(ArticleTag, ArticleTagAdmin)


class VideoTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'is_all_directions', 'created', 'updated']
    form = VideoTagForm

admin.site.register(VideoTag, VideoTagAdmin)


class AudioTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'is_all_directions', 'created', 'updated']
    form = AudioTagForm

admin.site.register(AudioTag, AudioTagAdmin)


class PhotoTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'is_all_directions', 'created', 'updated']
    form = PhotoTagForm

admin.site.register(PhotoTag, PhotoTagAdmin)


class PostGroupTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'is_all_directions', 'created', 'updated']
    form = PostGroupTagForm

admin.site.register(PostGroupTag, PostGroupTagAdmin)


class ChapterTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'is_all_directions', 'created', 'updated']
    form = ChapterTagForm

admin.site.register(ChapterTag, ChapterTagAdmin)


class PlaylistTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'is_all_directions', 'created', 'updated']
    form = PlaylistTagForm

admin.site.register(PlaylistTag, PlaylistTagAdmin)


class TracklistTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'is_all_directions', 'created', 'updated']
    form = TracklistTagForm

admin.site.register(TracklistTag, TracklistTagAdmin)


class AlbumTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'is_all_directions', 'created', 'updated']
    form = AlbumTagForm

admin.site.register(AlbumTag, AlbumTagAdmin)
