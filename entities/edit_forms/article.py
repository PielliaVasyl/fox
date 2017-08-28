from django import forms

from entities.models import Article


class EditArticleTitleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title']


class EditArticleDirectionsForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['directions']


class EditArticleDescriptionAndAuthorForm(forms.ModelForm):
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


class EditArticleLinkForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['link', 'is_linked_article']


class EditArticleGroupsForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['groups']


class EditArticlePolicyForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['owners', 'contributors', 'author']
