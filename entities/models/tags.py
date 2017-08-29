from django.db import models

from entities.models.classes import Direction


class AbstractTag(models.Model):
    title = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('title',)
        abstract = True


class GlobalTag(AbstractTag):
    pass


class CityTag(GlobalTag):
    pass


class DirectionTag(GlobalTag):
    direction = models.OneToOneField(Direction, on_delete=models.CASCADE)


class LocalTag(AbstractTag):
    pass


class DanceTag(LocalTag):
    direction = models.ForeignKey(Direction, default=Direction.objects.get(title='dance').id, on_delete=models.CASCADE)


class DanceStyleTag(DanceTag):
    pass


class DanceStyleCountTag(DanceTag):
    pass


class DanceStyleDistanceTag(DanceTag):
    pass


class DanceDirectionTag(DanceTag):
    pass


class PostTag(AbstractTag):
    directions = models.ManyToManyField(Direction, blank=True)
    is_all_directions = models.BooleanField(default=False)

    def get_directions(self):
        if self.directions.all():
            return "\n".join([p.title for p in self.directions.all()])
        return ''


class ArticleTag(PostTag):
    pass


class VideoTag(PostTag):
    pass


class AudioTag(PostTag):
    pass


class PhotoTag(PostTag):
    pass


class PostGroupTag(AbstractTag):
    directions = models.ManyToManyField(Direction, blank=True)
    is_all_directions = models.BooleanField(default=False)

    def get_directions(self):
        if self.directions.all():
            return "\n".join([p.title for p in self.directions.all()])
        return ''


class ChapterTag(PostGroupTag):
    pass


class PlaylistTag(PostGroupTag):
    pass


class TracklistTag(PostGroupTag):
    pass


class AlbumTag(PostGroupTag):
    pass
