from django.db import models

from entities.models.posts import Album, Article, Audio, Chapter, Photo, Playlist, Tracklist, Video
from entities.models.events import Event, PromoAction


class AbstractOwns(models.Model):
    events = models.ManyToManyField(Event, blank=True)
    promo_actions = models.ManyToManyField(PromoAction, blank=True)

    articles = models.ManyToManyField(Article, blank=True)
    chapters = models.ManyToManyField(Chapter, blank=True)
    photos = models.ManyToManyField(Photo, blank=True)
    albums = models.ManyToManyField(Album, blank=True)
    videos = models.ManyToManyField(Video, blank=True)
    playlists = models.ManyToManyField(Playlist, blank=True)
    audios = models.ManyToManyField(Audio, blank=True)
    tracklists = models.ManyToManyField(Tracklist, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('updated',)
        abstract = True


class PlaceOwns(AbstractOwns):
    pass


class SchoolOwns(AbstractOwns):
    pass


class OrganizationOwns(AbstractOwns):
    pass


class TeacherOwns(AbstractOwns):
    pass


class PersonOwns(AbstractOwns):
    pass


class ShopOwns(AbstractOwns):
    pass


class CustomerServicesOwns(AbstractOwns):
    pass


class HallOwns(AbstractOwns):
    pass


class ResourceOwns(AbstractOwns):
    pass
