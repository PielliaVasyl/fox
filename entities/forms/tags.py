# coding: utf-8

from django import forms

from entities.models.tags import AbstractTag, AlbumTag, ArticleTag, AudioTag, ChapterTag, CityTag, DanceDirectionTag, \
    DanceStyleCountTag, DanceStyleDistanceTag, DanceStyleTag, DanceTag, DirectionTag, GlobalTag, LocalTag, PhotoTag, \
    PlaylistTag, PostGroupTag, PostTag, TracklistTag, VideoTag


class AbstractTagForm(forms.ModelForm):
    class Meta:
        model = AbstractTag
        fields = ['title']


class GlobalTagForm(forms.ModelForm):
    class Meta:
        model = GlobalTag
        fields = ['title']


class CityTagForm(forms.ModelForm):
    class Meta:
        model = CityTag
        fields = ['title']


class DirectionTagForm(forms.ModelForm):
    class Meta:
        model = DirectionTag
        fields = ['title', 'direction']


class LocalTagForm(forms.ModelForm):
    class Meta:
        model = LocalTag
        fields = ['title']


class DanceTagForm(forms.ModelForm):
    class Meta:
        model = DanceTag
        fields = ['title', 'direction']


class DanceStyleTagForm(forms.ModelForm):
    class Meta:
        model = DanceStyleTag
        fields = ['title', 'direction']


class DanceStyleCountTagForm(forms.ModelForm):
    class Meta:
        model = DanceStyleCountTag
        fields = ['title', 'direction']


class DanceStyleDistanceTagForm(forms.ModelForm):
    class Meta:
        model = DanceStyleDistanceTag
        fields = ['title', 'direction']


class DanceDirectionTagForm(forms.ModelForm):
    class Meta:
        model = DanceDirectionTag
        fields = ['title', 'direction']


class PostTagForm(forms.ModelForm):
    class Meta:
        model = PostTag
        fields = ['title', 'directions', 'is_all_directions']


class ArticleTagForm(forms.ModelForm):
    class Meta:
        model = ArticleTag
        fields = ['title', 'directions', 'is_all_directions']


class VideoTagForm(forms.ModelForm):
    class Meta:
        model = VideoTag
        fields = ['title', 'directions', 'is_all_directions']


class AudioTagForm(forms.ModelForm):
    class Meta:
        model = AudioTag
        fields = ['title', 'directions', 'is_all_directions']


class PhotoTagForm(forms.ModelForm):
    class Meta:
        model = PhotoTag
        fields = ['title', 'directions', 'is_all_directions']


class PostGroupTagForm(forms.ModelForm):
    class Meta:
        model = PostGroupTag
        fields = ['title', 'directions', 'is_all_directions']


class ChapterTagForm(forms.ModelForm):
    class Meta:
        model = ChapterTag
        fields = ['title', 'directions', 'is_all_directions']


class PlaylistTagForm(forms.ModelForm):
    class Meta:
        model = PlaylistTag
        fields = ['title', 'directions', 'is_all_directions']


class TracklistTagForm(forms.ModelForm):
    class Meta:
        model = TracklistTag
        fields = ['title', 'directions', 'is_all_directions']


class AlbumTagForm(forms.ModelForm):
    class Meta:
        model = AlbumTag
        fields = ['title', 'directions', 'is_all_directions']
