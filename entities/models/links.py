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
        abstract = True


# class AbstractEventLink(AbstractLink):
#     pass


class EventLink(AbstractLink):
    pass


class PromoActionLink(AbstractLink):
    pass

# class AbstractPageLink(AbstractLink):
#     pass


class PlaceLink(AbstractLink):
    pass


class SchoolLink(AbstractLink):
    pass


class OrganizationLink(AbstractLink):
    pass


class TeacherLink(AbstractLink):
    pass


class PersonLink(AbstractLink):
    pass


class ShopLink(AbstractLink):
    pass


class CustomerServicesLink(AbstractLink):
    pass


class HallLink(AbstractLink):
    pass


class ResourceLink(AbstractLink):
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
