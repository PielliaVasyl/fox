from datetime import date

from django.db import models
from django.template.defaultfilters import truncatechars

from algoritms.get_status import get_auto_status
from entities.models import AbstractEventLink
from entities.models import City
from entities.models import DayOfTheWeek
from entities.models import Direction
from entities.models import EventLocalClasses
from entities.models import EventLocation
from entities.models import EventType
from entities.models import ExperienceLevel
from entities.models import PriceType
from entities.models import RepeatsType
from entities.models import UserProfile


class AbstractEvent(models.Model):
    title = models.CharField(max_length=100)

    directions = models.ManyToManyField(Direction, blank=True)
    cities = models.ManyToManyField(City, blank=True)

    local_classes = models.ForeignKey(EventLocalClasses, on_delete=models.CASCADE)

    description = models.TextField(blank=True)
    note = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    video = models.URLField(blank=True)

    start_date = models.DateField(default=date.today, blank=True)
    end_date = models.DateField(default=date.today, blank=True)

    AUTO = None
    DENIED = 'DENIED'
    POSTPONED = 'POSTPONED'

    STATUS_DICT = {
        DENIED: 'Отменено',
        POSTPONED: 'Перенесено'
    }
    STATUS_CHOICES = (
        (AUTO, 'Определяется автоматически'),
        (DENIED, 'Отменено'),
        (POSTPONED, 'Перенесено'),
    )
    _status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=AUTO, blank=True, db_column='status')

    @property
    def status(self):
        if self._status:
            return self.STATUS_DICT.get(self._status, 'Статус неизвестен')
        else:
            return get_auto_status(self.start_date, self.end_date)

    @status.setter
    def status(self, value):
        self._status = value

    links = models.ManyToManyField(AbstractEventLink, blank=True)

    # organizers = models.ForeignKey(EventOrganizers, on_delete=models.CASCADE)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='abstract_event_owners')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='abstract_event_contributors')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    def get_directions(self):
        if self.directions.all():
            return "\n".join([p.title for p in self.directions.all()])
        return ''

    def get_cities(self):
        if self.cities.all():
            return "\n".join([p.title for p in self.cities.all()])
        return ''

    def get_links(self):
        if self.links.all():
            return "\n".join([p.link for p in self.links.all()])
        return ''

    def get_owners(self):
        if self.owners.all():
            return "\n".join([p.user.username for p in self.owners.all()])
        return ''

    def get_contributors(self):
        if self.contributors.all():
            return "\n".join([p.user.username for p in self.contributors.all()])
        return ''

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('updated',)


class Event(AbstractEvent):
    types = models.ManyToManyField(EventType, blank=True)
    locations = models.ManyToManyField(EventLocation, blank=True)

    price_types = models.ManyToManyField(PriceType, blank=True)
    experience_levels = models.ManyToManyField(ExperienceLevel, blank=True)

    repeats_type = models.ForeignKey(RepeatsType, on_delete=models.CASCADE)
    schedule = models.ManyToManyField(DayOfTheWeek, blank=True)

    def get_types(self):
        if self.types.all():
            return "\n".join([p.title for p in self.types.all()])
        return ''

    def get_locations(self):
        if self.locations.all():
            return "\n".join([p.title_show() for p in self.locations.all()])
        return ''

    def get_price_types(self):
        if self.price_types.all():
            return "\n".join([p.title for p in self.price_types.all()])
        return ''

    def get_experience_levels(self):
        if self.experience_levels.all():
            return "\n".join([p.title for p in self.experience_levels.all()])
        return ''

    def get_schedule(self):
        if self.schedule.all():
            return "\n".join([p.title for p in self.schedule.all()])
        return ''


class PromoAction(AbstractEvent):
    pass
