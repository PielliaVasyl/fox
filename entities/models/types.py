from django.db import models
from django.template.defaultfilters import truncatechars


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
            self.FESTIVAL: 'Фестивать',
            self.COMPETITION: 'Конкурс',
            self.MASTERCLASS: 'Мастер-класс',
            self.OPEN_AIR: 'Open air',
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


class PlaceType(AbstractType):
    OPEN_AIR = 'OPEN_AIR'

    TITLE_CHOICES = (
        (OPEN_AIR, 'Open air'),
    )
    TITLE_DICT = {
        OPEN_AIR: 'Open air',
    }
    title = models.CharField(max_length=20, choices=TITLE_CHOICES, default=OPEN_AIR)

    def title_show(self):
        title_show_dict = {
            self.OPEN_AIR: 'Open air',
        }
        return "%s" % title_show_dict.get(str(self.title), str(self.title))


class ShopType(AbstractType):
    SHOP = 'SHOP'
    INTERNET_SHOP = 'INTERNET_SHOP'

    TITLE_CHOICES = (
        (SHOP, 'Магазин'),
        (INTERNET_SHOP, 'Интернет-магазин'),
    )
    TITLE_DICT = {
        SHOP: 'Магазин',
        INTERNET_SHOP: 'Интернет-магазин'
    }
    title = models.CharField(max_length=20, choices=TITLE_CHOICES, default=SHOP)

    def title_show(self):
        title_show_dict = {
            self.SHOP: 'Магазин',
            self.INTERNET_SHOP: 'Интернет-магазин',
        }
        return "%s" % title_show_dict.get(str(self.title), str(self.title))


class CustomerServicesType(AbstractType):
    BARBERSHOP = 'BARBERSHOP'
    ATELIER = 'ATELIER'

    TITLE_CHOICES = (
        (BARBERSHOP, 'Парикмахерская'),
        (ATELIER, 'Ателье'),
    )
    TITLE_DICT = {
        BARBERSHOP: 'Парикмахерская',
        ATELIER: 'Ателье'
    }
    title = models.CharField(max_length=20, choices=TITLE_CHOICES, default=BARBERSHOP)

    def title_show(self):
        title_show_dict = {
            self.BARBERSHOP: 'Парикмахерская',
            self.ATELIER: 'Ателье',
        }
        return "%s" % title_show_dict.get(str(self.title), str(self.title))


class DanceStyleCountType(AbstractType):
    SOLO = 'SOLO'
    PARTNER = 'PARTNER'
    GROUP = 'GROUP'

    TITLE_SHOW = {
        SOLO: 'Одиночный',
        PARTNER: 'Парный',
        GROUP: 'Групповой'
    }

    TITLE_CHOICES = (
        (SOLO, 'Одиночный'),
        (PARTNER, 'Парный'),
        (GROUP, 'Групповой')
    )

    title = models.CharField(max_length=10, choices=TITLE_CHOICES, blank=True)

    def title_show(self):
        title_show_dict = {k: v for k, v in self.TITLE_CHOICES}
        return "%s" % title_show_dict.get(self.title, self.title)

    def __str__(self):
        return '%s' % self.title


class DanceStyleDistanceType(AbstractType):
    CLOSE = 'CLOSE'
    AVERAGE = 'AVERAGE'
    DISTANT = 'DISTANT'

    TITLE_SHOW = {
        CLOSE: 'Близкая',
        AVERAGE: 'Средняя',
        DISTANT: 'Далекая'
    }

    TITLE_CHOICES = (
        (CLOSE, 'Близкая'),
        (AVERAGE, 'Средняя'),
        (DISTANT, 'Далекая')
    )

    title = models.CharField(max_length=10, choices=TITLE_CHOICES, blank=True)

    def title_show(self):
        title_choices_dict = {k: v for k, v in self.TITLE_CHOICES}
        return "%s" % title_choices_dict.get(self.title, self.title)

    def __str__(self):
        return '%s' % self.title
