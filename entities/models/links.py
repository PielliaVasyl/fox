from django.db import models

from entities.models.userprofile import UserProfile


class AbstractLink(models.Model):
    link = models.URLField()

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.link

    class Meta:
        ordering = ('link',)


class AbstractEventLink(AbstractLink):
    pass


class AbstractPageLink(AbstractLink):
    pass


class PlaylistLink(AbstractLink):
    pass


class ArticleLink(AbstractLink):
    pass


class PhotoLink(AbstractLink):
    pass


class VideoLink(AbstractLink):
    pass


class AudioLink(AbstractLink):
    pass


class DanceStyleAuthorLink(AbstractLink):
    pass
