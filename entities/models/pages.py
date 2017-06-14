from django.db import models

from entities.models.classes import Direction, City
from entities.models.userprofile import UserProfile
from entities.models.supportclasses import AbstractPageLink, PageLocalClasses
from entities.models.types import PlaceType, ShopType
from entities.models.locations import PlaceLocation, OrganizationLocation, ShopLocation, HallLocation
from entities.models import SchoolLocation
from entities.models.contacts import SchoolContacts, OrganizationContacts, TeacherContacts, PersonContacts, \
    ShopContacts, HallContacts, ResourceContacts


class AbstractPage(models.Model):
    title = models.CharField(max_length=100)

    directions = models.ManyToManyField(Direction, blank=True)
    cities = models.ManyToManyField(City, blank=True)

    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    links = models.ManyToManyField(AbstractPageLink, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='abstract_page_owners')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='abstract_page_contributors')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

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

    def get_links_list(self):
        if self.links.all():
            return [p.link for p in self.links.all()]
        return []

    def get_owners(self):
        if self.owners.all():
            return "\n".join([p.user.username for p in self.owners.all()])
        return ''

    def get_contributors(self):
        if self.contributors.all():
            return "\n".join([p.title for p in self.contributors.all()])
        return ''

    def get_locations(self):
        if self.locations.all():
            return "\n".join([p.title_show() for p in self.locations.all()])
        return ''

    def get_locations_address_list(self):
        if self.locations.all():
            return [p.address for p in self.locations.all()]
        return []

    def get_types(self):
        if self.types.all():
            return "\n".join([p.title for p in self.types.all()])
        return ''

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('updated',)


class Place(AbstractPage):
    locations = models.ManyToManyField(PlaceLocation, blank=True)

    local_classes = models.OneToOneField(PageLocalClasses, on_delete=models.CASCADE)

    types = models.ManyToManyField(PlaceType, blank=True)


class EmployersPage(AbstractPage):
    def get_employees(self):
        if self.employees.all():
            return "\n".join([p.title for p in self.employees.all()])
        return ''


class EmployeesPage(AbstractPage):
    def get_employers(self):
        if self.employees.all():
            return "\n".join([p.title for p in self.employees.all()])
        return ''


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
    employees = models.ManyToManyField(EmployeesPage, blank=True)

    contacts = models.OneToOneField(ShopContacts, on_delete=models.CASCADE, null=True, blank=True)

    # events = models.ManyToManyField(AbstractEvent, blank=True)


class Hall(EmployersPage):
    locations = models.ManyToManyField(HallLocation, blank=True)
    employees = models.ManyToManyField(EmployeesPage, blank=True)

    contacts = models.OneToOneField(HallContacts, on_delete=models.CASCADE, null=True, blank=True)

    # photos = models.ManyToManyField(HallPhoto, blank=True)


class Resource(EmployersPage):
    contacts = models.OneToOneField(ResourceContacts, on_delete=models.CASCADE, null=True, blank=True)