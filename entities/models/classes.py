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
        # abstract = True


class AbstractGlobalClass(AbstractClass):
    pass
    # class Meta:
    #     abstract = True


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

    # class Meta:
    #     abstract = True


class DanceDirectionClass(AbstractLocalClass):
    pass


class DanceStyleClass(AbstractLocalClass):
    dance_direction = models.ForeignKey('DanceDirectionClass', blank=True, null=True)


@receiver(post_save, sender=DanceStyleClass)
def create_initial_data_dance_style_class(sender, instance, created, **kwargs):
    if created and sender == 'DanceStyleClass':
        if Direction.objects.filter(title='Dance'):
            if Direction.objects.filter(title='Dance') not in instance.directions:
                instance.directions.add(Direction.objects.get(title='Dance'))
                instance.save()
        else:
            direction = Direction(title="Dance")
            direction.save()
            instance.directions.add(direction)
            instance.save()


@receiver(post_save, sender=DanceDirectionClass)
def create_initial_data_dance_direction_class(sender, instance, created, **kwargs):
    if created and sender == 'DanceDirectionClass':
        if Direction.objects.filter(title='Dance'):
            if Direction.objects.filter(title='Dance') not in instance.directions:
                instance.directions.add(Direction.objects.get(title='Dance'))
                instance.save()
        else:
            direction = Direction(title="Dance")
            direction.save()
            instance.directions.add(direction)
            instance.save()
