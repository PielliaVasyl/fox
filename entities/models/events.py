from datetime import date

from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import activate
from django.template.defaultfilters import date as date_filter

from algoritms.get_status import get_auto_status
from entities.models.classes import City, Direction
from entities.models.links import PromoActionLink, EventLink
from entities.models.locations import EventLocation
from entities.models.supportclasses import EventLocalClasses
from entities.models.types import DayOfTheWeek, EventType, ExperienceLevel, PriceType, RepeatsType
from entities.models.userprofile import UserProfile


def _get_date_show(self):
    activate('ru')
    if self.start_date and self.end_date:
        if self.start_date == self.end_date:
            return '{0} {1}'.format(self.start_date.strftime('%d'), date_filter(self.start_date, 'F').lower()[:3])
        elif self.start_date.month == self.end_date.month:
            return '{0} - {1} {2}'.format(self.start_date.strftime('%d'), self.end_date.strftime('%d'),
                                          date_filter(self.start_date, 'F').lower()[:3])
        return '{0} {1} - {2} {3}'.format(self.start_date.strftime('%d'),
                                          date_filter(self.start_date, 'F').lower()[:3],
                                          self.end_date.strftime('%d'),
                                          date_filter(self.end_date, 'F').lower()[:3])
    if self.start_date:
        return 'c {0} {1}'.format(self.start_date.strftime('%d'),
                                  date_filter(self.start_date, 'F').lower()[:3])
    if self.end_date:
        return 'по {0} {1}'.format(self.end_date.strftime('%d'),
                                   date_filter(self.end_date, 'F').lower()[:3])


class AbstractEvent(models.Model):
    title = models.CharField(max_length=100)

    directions = models.ManyToManyField(Direction, blank=True)
    cities = models.ManyToManyField(City, blank=True)

    local_classes = models.OneToOneField(EventLocalClasses, on_delete=models.CASCADE, null=True)

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
    _status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=AUTO, blank=True, null=True,
                               db_column='status')

    @property
    def status(self):
        if self._status:
            return self.STATUS_DICT.get(self._status, 'Статус неизвестен')
        else:
            return get_auto_status(self.start_date, self.end_date)

    @status.setter
    def status(self, value):
        self._status = value

    # links = models.ManyToManyField(AbstractEventLink, blank=True)

    # organizers = models.ForeignKey(EventOrganizers, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def date_show(self):
        return _get_date_show(self) or 'Неизвестно'

    @staticmethod
    def day_show(number_days):
        return {
            '1': 'день',
            '2': 'дня',
            '3': 'дня',
            '4': 'дня',
            '5': 'дней',
            '6': 'дней',
            '7': 'дней',
            '8': 'дней',
            '9': 'дней',
            '10': 'дней',
            '11': 'дней',
            '12': 'дней',
            '13': 'дней',
            '14': 'дней',
        }.get(str(number_days), 'день')

    def duration_show(self):
        if self.start_date and self.end_date:
            number_days = int((self.end_date - self.start_date).days) + 1
            return '%s %s' % (str(number_days),
                              self.day_show(number_days),)
        return 'продолжительность неизвестна'

    # def get_start_date_day_of_week(self):
    #     if self.start_date:
    #         return ''.join(self.start_date.strftime("%A"))
    #     return ''
    #
    # def get_end_date_day_of_week(self):
    #     if self.end_date:
    #         return ''.join(self.end_date.strftime("%A"))
    #     return ''

    def status_icon(self):
        status_icon_dict = {
            'Запланировано': 'fa-calendar-check-o',
            'Отменено': 'fa-times',
            'Перенесено': 'fa-clock-o',
            'Проводится': 'fa-play',
            'Завершено': 'fa-check'
        }
        return "%s" % status_icon_dict.get(self.status, 'fa-dot-circle-o')

    def status_label_color(self):
        status_label_color_dict = {
            'Запланировано': 'info',
            'Отменено': 'danger',
            'Перенесено': 'warning',
            'Проводится': 'success',
            'Завершено': 'primary'
        }
        return "%s" % status_label_color_dict.get(self.status, 'default')

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
        abstract = True


class Event(AbstractEvent):
    types = models.ManyToManyField(EventType, blank=True)
    locations = models.ManyToManyField(EventLocation, blank=True)

    links = models.ManyToManyField(EventLink, blank=True)

    price_types = models.ManyToManyField(PriceType, blank=True)
    experience_levels = models.ManyToManyField(ExperienceLevel, blank=True)

    repeats_type = models.ForeignKey(RepeatsType, on_delete=models.CASCADE, null=True)
    schedule = models.ManyToManyField(DayOfTheWeek, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='events_owner')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='events_contributor')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, related_name='events_author')

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
    links = models.ManyToManyField(PromoActionLink, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='promo_actions_owner')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='promo_actions_contributor')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, related_name='promo_actions_author')
