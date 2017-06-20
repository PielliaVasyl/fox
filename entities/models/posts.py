from django.db import models

from entities.models.classes import Direction
from entities.models.links import ArticleLink, AudioLink, PhotoLink, PlaylistLink, VideoLink
from entities.models.tags import ChapterTag, AlbumTag, PlaylistTag, TracklistTag, ArticleTag, PhotoTag, \
    VideoTag, AudioTag
from entities.models.userprofile import UserProfile


class AbstractPostGroup(models.Model):
    title = models.CharField(max_length=100)

    directions = models.ManyToManyField(Direction, blank=True)

    description = models.TextField(blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='abstract_post_group_owners')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='abstract_post_group_contributors')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_directions(self):
        if self.directions.all():
            return "\n".join([p.title for p in self.directions.all()])
        return ''

    def get_tags(self):
        if self.tags.all():
            return "\n".join([p.title for p in self.tags.all()])
        return ''

    def get_owners(self):
        if self.owners.all():
            return "\n".join([p.user.username for p in self.owners.all()])
        return ''

    def get_contributors(self):
        if self.contributors.all():
            return "\n".join([p.title for p in self.contributors.all()])
        return ''


class Chapter(AbstractPostGroup):
    tags = models.ManyToManyField(ChapterTag, default=True)


class Album(AbstractPostGroup):
    tags = models.ManyToManyField(AlbumTag, default=True)


class Playlist(AbstractPostGroup):
    link = models.OneToOneField(PlaylistLink, blank=True, null=True)
    tags = models.ManyToManyField(PlaylistTag, default=True)


class Tracklist(AbstractPostGroup):
    tags = models.ManyToManyField(TracklistTag, default=True)


class AbstractPost(models.Model):
    title = models.CharField(max_length=100)

    directions = models.ManyToManyField(Direction, blank=True)

    description = models.TextField(blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='abstract_post_owners')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='abstract_post_contributors')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_directions(self):
        if self.directions.all():
            return "\n".join([p.title for p in self.directions.all()])
        return ''

    def get_tags(self):
        if self.tags.all():
            return "\n".join([p.title for p in self.tags.all()])
        return ''

    def get_groups(self):
        if self.groups.all():
            return "\n".join([p.title for p in self.groups.all()])
        return ''

    def get_owners(self):
        if self.owners.all():
            return "\n".join([p.user.username for p in self.owners.all()])
        return ''

    def get_contributors(self):
        if self.contributors.all():
            return "\n".join([p.title for p in self.contributors.all()])
        return ''

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('updated',)


class Article(AbstractPost):
    tags = models.ManyToManyField(ArticleTag, blank=True)
    link = models.OneToOneField(ArticleLink, blank=True, null=True)
    image = models.ImageField(blank=True)
    is_linked_article = models.BooleanField(default=False)
    author_of_post = models.CharField(max_length=100, blank=True)
    groups = models.ManyToManyField(Chapter, blank=True)


class Photo(AbstractPost):
    tags = models.ManyToManyField(PhotoTag, blank=True)
    link = models.OneToOneField(PhotoLink, blank=True, null=True)
    image = models.ImageField(blank=True)
    groups = models.ManyToManyField(Album, blank=True)


class Video(AbstractPost):
    tags = models.ManyToManyField(VideoTag, blank=True)
    link = models.OneToOneField(VideoLink, blank=True, null=True)
    groups = models.ManyToManyField(Playlist, blank=True)


class Audio(AbstractPost):
    tags = models.ManyToManyField(AudioTag, blank=True)
    link = models.OneToOneField(AudioLink, blank=True, null=True)
    groups = models.ManyToManyField(Tracklist, blank=True)
