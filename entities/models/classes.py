from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save


class AbstractClass(models.Model):
    title = models.CharField(max_length=100)

    # author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('title',)


class AbstractGlobalClass(AbstractClass):
    pass


class City(AbstractGlobalClass):
    pass


class Direction(AbstractGlobalClass):
    pass


class AbstractLocalClass(AbstractClass):
    directions = models.ManyToManyField(Direction)

    def get_directions(self):
        if self.directions.all():
            return "\n".join([p.title for p in self.directions.all()])
        return ''


class DanceDirection(AbstractLocalClass):
    pass


class DanceStyle(AbstractLocalClass):
    dance_direction = models.ForeignKey('DanceDirection', blank=True)


@receiver(post_save, sender=DanceStyle)
def create_initial_data_dance_style(sender, instance, created, **kwargs):
    if created and sender == 'DanceStyle':
        if Direction.objects.filter(title='Dance'):
            if Direction.objects.filter(title='Dance') not in instance.directions:
                instance.directions.add(Direction.objects.get(title='Dance'))
                instance.save()
        else:
            direction = Direction(title="Dance")
            direction.save()
            instance.directions.add(direction)
            instance.save()


@receiver(post_save, sender=DanceDirection)
def create_initial_data_dance_direction(sender, instance, created, **kwargs):
    if created and sender == 'DanceDirection':
        if Direction.objects.filter(title='Dance'):
            if Direction.objects.filter(title='Dance') not in instance.directions:
                instance.directions.add(Direction.objects.get(title='Dance'))
                instance.save()
        else:
            direction = Direction(title="Dance")
            direction.save()
            instance.directions.add(direction)
            instance.save()