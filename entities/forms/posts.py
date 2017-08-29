# coding: utf-8

from django import forms

from entities.models.posts import AbstractPost, AbstractPostGroup, Album, Article, Audio, Chapter, Photo, Playlist, \
    Tracklist, Video, DanceDirection, DanceStyle


CUT_FORM_FIELDS = ['title', 'author']


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'directions', 'description', 'tags', 'owners', 'contributors', 'author']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'directions', 'description', 'tags', 'owners', 'contributors', 'author']


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['title', 'directions', 'description', 'tags', 'owners', 'contributors', 'author']


class TracklistForm(forms.ModelForm):
    class Meta:
        model = Tracklist
        fields = ['title', 'directions', 'description', 'tags', 'owners', 'contributors', 'author']


class DanceDirectionForm(forms.ModelForm):
    class Meta:
        model = DanceDirection
        fields = ['title', 'direction', 'description', 'tags', 'owners', 'contributors', 'author']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'directions', 'description', 'tags', 'link', 'image', 'is_linked_article', 'owners',
                  'author_of_post', 'groups', 'contributors', 'author']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'directions', 'description', 'tags', 'link', 'image', 'groups',
                  'owners', 'contributors', 'author']


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'directions', 'description', 'tags', 'link', 'groups', 'owners', 'contributors', 'author']


class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title', 'directions', 'description', 'tags', 'link', 'groups', 'owners', 'contributors', 'author']


class DanceStyleForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['title', 'direction', 'description', 'tags', 'image', 'author_of_post', 'link_to_author', 'group',
                  'count_types', 'distance_types', 'owners', 'contributors', 'author']


class CutArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = CUT_FORM_FIELDS


class CutChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = CUT_FORM_FIELDS


class CutPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = CUT_FORM_FIELDS


class CutAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = CUT_FORM_FIELDS


class CutVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = CUT_FORM_FIELDS


class CutPlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = CUT_FORM_FIELDS


class CutAudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = CUT_FORM_FIELDS


class CutTracklistForm(forms.ModelForm):
    class Meta:
        model = Tracklist
        fields = CUT_FORM_FIELDS


class CutDanceStyleForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['title', 'group', 'author']


class CutDanceDirectionForm(forms.ModelForm):
    class Meta:
        model = DanceDirection
        fields = CUT_FORM_FIELDS
