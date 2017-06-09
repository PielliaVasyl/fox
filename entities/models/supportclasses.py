from django.db import models
from django.template.defaultfilters import truncatechars

from entities.models import City
from entities.models import DanceDirection
from entities.models import DanceStyle
from entities.models import UserProfile


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

    class Meta:
        ordering = ('updated',)


class AbstractType(models.Model):
    description = models.TextField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('created',)


class EventType(AbstractType):
    FESTIVAL = 'FESTIVAL'
    COMPETITION = 'COMPETITION'
    MASTERCLASS = 'MASTERCLASS'
    OPEN_AIR = 'OPEN_AIR'
    PARTY = 'PARTY'
    GROUP_CLASSES = 'GROUP_CLASSES'
    OPEN_LESSON = 'OPEN_LESSON'

    TITLE_CHOICES = (
        (FESTIVAL, 'Фестивать'),
        (COMPETITION, 'Конкурс'),
        (MASTERCLASS, 'Мастер-класс'),
        (OPEN_AIR, 'Open air'),
        (PARTY, 'Вечеринка'),
        (GROUP_CLASSES, 'Групповые занятия'),
        (OPEN_LESSON, 'Открытый урок')
    )
    TITLE_DICT = {
        FESTIVAL: 'Фестивать',
        COMPETITION: 'Конкурс',
        MASTERCLASS: 'Мастер-класс',
        OPEN_AIR: 'Open air',
        PARTY: 'Вечеринка',
        GROUP_CLASSES: 'Групповые занятия',
        OPEN_LESSON: 'Открытый урок'
    }
    title = models.CharField(max_length=20, choices=TITLE_CHOICES, default=MASTERCLASS)

    def title_show(self):
        title_show_dict = {
            self.FEST: 'Фестивать',
            self.COMPETITION: 'Конкурс',
            self.MASTERCLASS: 'Мастер-класс',
            self.OPENAIR: 'Open air',
            self.PARTY: 'Вечеринка',
            self.GROUP_CLASSES: 'Групповые занятия',
            self.OPEN_LESSON: 'Открытый урок'
        }
        return "%s" % title_show_dict.get(str(self.title), str(self.title))


class PriceType(AbstractType):
    PAID = 'PAID'
    FREE = 'FREE'
    SHAREWARE = 'SHAREWARE'  # условно-бесплатное - получение билетов при репосте и выигрыше в лотерее
    FIRST_LESSON_FREE = 'FIRST_LESSON_FREE'

    TITLE_CHOICES = (
        (PAID, 'Платно'),
        (FREE, 'Бесплатно'),
        (SHAREWARE, 'Условно-бесплатно'),
        (FIRST_LESSON_FREE, 'Первое занятие бесплатно')
    )
    TITLE_DICT = {
        PAID: 'Платно',
        FREE: 'Бесплатно',
        SHAREWARE: 'Условно-бесплатно',
        FIRST_LESSON_FREE: 'Первое занятие бесплатно'
    }
    title = models.CharField(max_length=20, choices=TITLE_CHOICES, default=PAID)

    def title_show(self):
        title_show_dict = {
            self.PAID: 'Платно',
            self.FREE: 'Бесплатно',
            self.SHAREWARE: 'Условно-бесплатно',
            self.FIRST_LESSON_FREE: 'Первое занятие бесплатно'
        }
        return "%s" % title_show_dict.get(str(self.title), str(self.title))


class ExperienceLevel(AbstractType):
    NEW = 'NEW'
    INTERMEDIATE = 'INM'
    ADVANCED = 'ADV'
    SHOW = 'SHW'
    PRACTICE = 'PRC'

    TITLE_CHOICES = (
        (NEW, 'Начинающий'),
        (INTERMEDIATE, 'Средний'),
        (ADVANCED, 'Опытный'),
        (SHOW, 'Шоу'),
        (PRACTICE, 'Практика'),
    )
    TITLE_DICT = {
        NEW: 'Начинающий',
        INTERMEDIATE: 'Средний',
        ADVANCED: 'Опытный',
        SHOW: 'Шоу',
        PRACTICE: 'Практика',
    }
    title = models.CharField(max_length=3, choices=TITLE_CHOICES, default=NEW)

    def title_show(self):
        title_show_dict = {
            self.NEW: 'Начинающий',
            self.INTERMEDIATE: 'Средний',
            self.ADVANCED: 'Опытный',
            self.SHOW: 'Шоу',
            self.PRACTICE: 'Практика'
        }
        return "%s" % title_show_dict.get(str(self.title), str(self.title))


class RepeatsType(AbstractType):
    ONCE = 'ONCE'
    WEEKLY = 'WEEKLY'

    TITLE_CHOICES = (
        (ONCE, 'Один раз'),
        (WEEKLY, 'Еженедельно'),
    )
    TITLE_DICT = {
        ONCE: 'Один раз',
        WEEKLY: 'Еженедельно',
    }
    title = models.CharField(max_length=10, choices=TITLE_CHOICES, default=ONCE)

    def title_show(self):
        title_show_dict = {
            self.ONCE: 'Один раз',
            self.WEEKLY: 'Еженедельно'
        }
        return "%s" % title_show_dict.get(str(self.title), str(self.title))


class DayOfTheWeek(AbstractType):
    MONDAY = 'MON'
    TUESDAY = 'TUE'
    WEDNESDAY = 'WED'
    THURSDAY = 'THU'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    SUNDAY = 'SUN'

    TITLE_CHOICES = (
        (MONDAY, 'Понедельник'),
        (TUESDAY, 'Вторник'),
        (WEDNESDAY, 'Среда'),
        (THURSDAY, 'Четверг'),
        (FRIDAY, 'Пятница'),
        (SATURDAY, 'Суббота'),
        (SUNDAY, 'Воскресенье'),
    )
    TITLE_DICT = {
        'MON': 'Пн',
        'TUE': 'Вт',
        'WED': 'Ср',
        'THU': 'Чт',
        'FRI': 'Пт',
        'SAT': 'Сб',
        'SUN': 'Вс'
    }
    DAY_TO_NUM = {
        'MON': 1,
        'TUE': 2,
        'WED': 3,
        'THU': 4,
        'FRI': 5,
        'SAT': 6,
        'SUN': 7
    }
    title = models.CharField(max_length=3, choices=TITLE_CHOICES, blank=True)

    def title_show(self):
        title_show_dict = {
            'MON': 'Пн',
            'TUE': 'Вт',
            'WED': 'Ср',
            'THU': 'Чт',
            'FRI': 'Пт',
            'SAT': 'Сб',
            'SUN': 'Вс'
        }
        return "%s" % title_show_dict.get(str(self.title), str(self.title))


class AbstractLocation(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    note = models.CharField(max_length=100, blank=True)

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        if self.address:
            return '%s, %s by %s' % (self.city.title, self.address, self.author)
        return '%s by %s' % (self.city.title, self.author)

    def title_show(self):
        if self.address:
            return '%s, %s' % (self.address, self.city.title)
        return '%s' % (self.city.title,)

    class Meta:
        ordering = ('created',)


class EventLocation(AbstractLocation):
    pass


# class EventOrganizers(models.Model):
#     pass
