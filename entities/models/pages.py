from django.db import models

from entities.models import Direction
from entities.models import City
from entities.models import UserProfile
from entities.models import AbstractPageLink
from entities.models import PageLocalClasses
from entities.models import PlaceType
from entities.models import PlaceLocation
from entities.models import SchoolLocation
from entities.models import SchoolContacts
from entities.models import OrganizationLocation
from entities.models import OrganizationContacts
from entities.models import TeacherContacts
from entities.models import PersonContacts
from entities.models import ShopLocation
from entities.models import ShopContacts
from entities.models import ShopType
from entities.models import HallLocation
from entities.models import HallContacts
from entities.models import ResourceContacts


class AbstractPage(models.Model):
    title = models.CharField(max_length=100)

    directions = models.ManyToManyField(Direction, blank=True)
    cities = models.ManyToManyField(City, blank=True)

    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    links = models.ManyToManyField(AbstractPageLink, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='abstract_event_owners')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='abstract_event_contributors')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('updated',)


class Place(AbstractPage):

    local_classes = models.OneToOneField(PageLocalClasses, on_delete=models.CASCADE)

    types = models.ManyToManyField(PlaceType, blank=True)
    locations = models.ManyToManyField(PlaceLocation, blank=True)


class EmployersPage(AbstractPage):
    pass


class EmployeesPage(AbstractPage):
    pass


class School(EmployersPage):
    local_classes = models.OneToOneField(PageLocalClasses, on_delete=models.CASCADE)

    locations = models.ManyToManyField(SchoolLocation, blank=True)
    employees = models.ManyToManyField(EmployeesPage, blank=True)

    contacts = models.OneToOneField(SchoolContacts, on_delete=models.CASCADE, null=True, blank=True)

    # events = models.ManyToManyField(AbstractEvent, blank=True)


class Organization(EmployersPage):
    local_classes = models.OneToOneField(PageLocalClasses, on_delete=models.CASCADE)

    locations = models.ManyToManyField(OrganizationLocation, blank=True)
    employees = models.ManyToManyField(EmployeesPage, blank=True)

    contacts = models.OneToOneField(OrganizationContacts, on_delete=models.CASCADE, null=True, blank=True)

    # events = models.ManyToManyField(AbstractEvent, blank=True)


class Teacher(EmployeesPage):
    local_classes = models.OneToOneField(PageLocalClasses, on_delete=models.CASCADE)

    employers = models.ManyToManyField(EmployersPage, blank=True)

    contacts = models.OneToOneField(TeacherContacts, on_delete=models.CASCADE, null=True, blank=True)

    # events = models.ManyToManyField(AbstractEvent, blank=True)


class Person(EmployeesPage):
    local_classes = models.OneToOneField(PageLocalClasses, on_delete=models.CASCADE)

    employers = models.ManyToManyField(EmployersPage, blank=True)

    contacts = models.OneToOneField(PersonContacts, on_delete=models.CASCADE, null=True, blank=True)

    # events = models.ManyToManyField(AbstractEvent, blank=True)


class Shop(EmployersPage):
    types = models.ManyToManyField(ShopType, blank=True)

    locations = models.ManyToManyField(ShopLocation, blank=True)

    contacts = models.OneToOneField(ShopContacts, on_delete=models.CASCADE, null=True, blank=True)

    # events = models.ManyToManyField(AbstractEvent, blank=True)


class Hall(EmployersPage):
    locations = models.ManyToManyField(HallLocation, blank=True)

    contacts = models.OneToOneField(HallContacts, on_delete=models.CASCADE, null=True, blank=True)

    # photos = models.ManyToManyField(HallPhoto, blank=True)


class Resource(EmployersPage):
    contacts = models.OneToOneField(ResourceContacts, on_delete=models.CASCADE, null=True, blank=True)