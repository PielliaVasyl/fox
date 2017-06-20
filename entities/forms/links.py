# coding: utf-8

from django import forms

from entities.models.links import AbstractEventLink, AbstractLink, AbstractPageLink, ArticleLink, AudioLink, \
    PhotoLink, PlaylistLink, VideoLink


class AbstractLinkForm(forms.ModelForm):
    class Meta:
        model = AbstractLink
        fields = ['link', 'author']


class AbstractEventLinkForm(forms.ModelForm):
    class Meta:
        model = AbstractEventLink
        fields = ['link', 'author']


class AbstractPageLinkForm(forms.ModelForm):
    class Meta:
        model = AbstractPageLink
        fields = ['link', 'author']


class PlaylistLinkForm(forms.ModelForm):
    class Meta:
        model = PlaylistLink
        fields = ['link', 'author']


class ArticleLinkForm(forms.ModelForm):
    class Meta:
        model = ArticleLink
        fields = ['link', 'author']


class PhotoLinkForm(forms.ModelForm):
    class Meta:
        model = PhotoLink
        fields = ['link', 'author']


class VideoLinkForm(forms.ModelForm):
    class Meta:
        model = VideoLink
        fields = ['link', 'author']


class AudioLinkForm(forms.ModelForm):
    class Meta:
        model = AudioLink
        fields = ['link', 'author']
