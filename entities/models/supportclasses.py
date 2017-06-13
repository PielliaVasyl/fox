from django.db import models

from entities.models.classes import DanceDirection, DanceStyle
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


class EventLocalClasses(models.Model):
    dance_styles = models.ManyToManyField(DanceStyle)
    dance_directions = models.ManyToManyField(DanceDirection)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_directions(self):
        if self.dance_directions.all():
            return "\n".join([p.title for p in self.dance_directions.all()])
        return ''

    def __str__(self):
        return '%s' % self.abstractevent

    class Meta:
        ordering = ('updated',)


class PageLocalClasses(models.Model):
    dance_styles = models.ManyToManyField(DanceStyle)
    dance_directions = models.ManyToManyField(DanceDirection)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_directions(self):
        if self.dance_directions.all():
            return "\n".join([p.title for p in self.dance_directions.all()])
        return ''

    def __str__(self):
        return '%s - %s' % (self.get_dance_directions(), self.get_dance_styles())

    class Meta:
        ordering = ('updated',)



# class EventOrganizers(models.Model):
#     pass
