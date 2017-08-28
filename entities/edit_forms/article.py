from django import forms

from entities.models import Article
from entities.models.links import ArticleLink


class EditArticleTitleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title']


class EditArticleDirectionsForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['directions']


class EditArticleArticleDescriptionForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['description', 'author_of_post']


class EditArticleImageForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['image']


class EditArticleTagsForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['tags']


class EditArticleArticleLinkForm(forms.ModelForm):
    class Meta:
        model = ArticleLink
        fields = ['link']


class EditArticleLinkedForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['is_linked_article']


class EditArticleGroupsForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['groups']


class EditArticlePolicyForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['owners', 'contributors', 'author']
