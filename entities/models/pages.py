from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from entities.models.classes import Direction, City
from entities.models.contacts import SchoolContacts, OrganizationContacts, TeacherContacts, PersonContacts, \
    ShopContacts, HallContacts, ResourceContacts, CustomerServicesContacts
from entities.models.links import ResourceLink, HallLink, CustomerServicesLink, ShopLink, PersonLink, \
    TeacherLink, OrganizationLink, SchoolLink, PlaceLink
from entities.models.locations import PlaceLocation, OrganizationLocation, ShopLocation, HallLocation, SchoolLocation, \
    CustomerServicesLocation
from entities.models.supportclasses import PageLocalClasses, PlaceLocalClasses, SchoolLocalClasses, TeacherLocalClasses, \
    OrganizationLocalClasses, PersonLocalClasses
from entities.models.types import PlaceType, ShopType, CustomerServicesType
from entities.models.userprofile import UserProfile


class AbstractPage(models.Model):
    title = models.CharField(max_length=100)

    directions = models.ManyToManyField(Direction, blank=True)
    cities = models.ManyToManyField(City, blank=True)

    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

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
        # if self.links.all():
        #     return "\n".join([p.link for p in self.links.all()])
        return ''

    def get_links_list(self):
        if self.links.all():
            return [p.link for p in self.links.all()]
        return []

    def get_owners(self):
        # if self.owners.all():
        #     return "\n".join([p.user.username for p in self.owners.all()])
        return ''

    def get_contributors(self):
        # if self.contributors.all():
        #     return "\n".join([p.title for p in self.contributors.all()])
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
        abstract = True


class Place(AbstractPage):
    locations = models.ManyToManyField(PlaceLocation, blank=True)

    local_classes = models.OneToOneField(PlaceLocalClasses, on_delete=models.CASCADE, null=True)

    types = models.ManyToManyField(PlaceType, blank=True)
    links = models.ManyToManyField(PlaceLink, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='places_owner')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='places_contributor')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='places_author')


@receiver(post_save, sender=Place)
def create_place_local_classes(sender, instance, created, **kwargs):
    if created:
        local_classes = PlaceLocalClasses.objects.create(place=instance)
        instance.local_classes = local_classes
        instance.save()


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
    local_classes = models.OneToOneField(SchoolLocalClasses, on_delete=models.CASCADE, null=True)

    locations = models.ManyToManyField(SchoolLocation, blank=True)
    employees = models.ManyToManyField(EmployeesPage, blank=True)

    links = models.ManyToManyField(SchoolLink, blank=True)
    contacts = models.OneToOneField(SchoolContacts, on_delete=models.CASCADE, null=True, blank=True)

    # events = models.ManyToManyField(AbstractEvent, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='schools_owner')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='schools_contributor')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='schools_author')


@receiver(post_save, sender=School)
def create_school_local_classes(sender, instance, created, **kwargs):
    if created:
        local_classes = SchoolLocalClasses.objects.create(school=instance)
        instance.local_classes = local_classes
        instance.save()


@receiver(post_save, sender=School)
def create_school_contacts(sender, instance, created, **kwargs):
    if created:
        contacts = SchoolContacts.objects.create(school=instance, author_id=instance.author_id)
        instance.contacts = contacts
        instance.save()


class Organization(EmployersPage):
    local_classes = models.OneToOneField(OrganizationLocalClasses, on_delete=models.CASCADE, null=True)

    locations = models.ManyToManyField(OrganizationLocation, blank=True)
    employees = models.ManyToManyField(EmployeesPage, blank=True)

    links = models.ManyToManyField(OrganizationLink, blank=True)
    contacts = models.OneToOneField(OrganizationContacts, on_delete=models.CASCADE, null=True, blank=True)

    # events = models.ManyToManyField(AbstractEvent, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='organizations_owner')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='organizations_contributor')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='organizations_author')


@receiver(post_save, sender=Organization)
def create_organization_local_classes(sender, instance, created, **kwargs):
    if created:
        local_classes = OrganizationLocalClasses.objects.create(organization=instance)
        instance.local_classes = local_classes
        instance.save()


@receiver(post_save, sender=Organization)
def create_organization_contacts(sender, instance, created, **kwargs):
    if created:
        contacts = OrganizationContacts.objects.create(organization=instance, author_id=instance.author_id)
        instance.contacts = contacts
        instance.save()


class Teacher(EmployeesPage):
    local_classes = models.OneToOneField(TeacherLocalClasses, on_delete=models.CASCADE, null=True)

    employers = models.ManyToManyField(EmployersPage, blank=True)

    links = models.ManyToManyField(TeacherLink, blank=True)
    contacts = models.OneToOneField(TeacherContacts, on_delete=models.CASCADE, null=True, blank=True)

    # events = models.ManyToManyField(AbstractEvent, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='teachers_owner')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='teachers_contributor')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='teachers_author')


@receiver(post_save, sender=Teacher)
def create_teacher_local_classes(sender, instance, created, **kwargs):
    if created:
        local_classes = TeacherLocalClasses.objects.create(teacher=instance)
        instance.local_classes = local_classes
        instance.save()


@receiver(post_save, sender=Teacher)
def create_teacher_contacts(sender, instance, created, **kwargs):
    if created:
        contacts = TeacherContacts.objects.create(teacher=instance, author_id=instance.author_id)
        instance.contacts = contacts
        instance.save()


class Person(EmployeesPage):
    local_classes = models.OneToOneField(PersonLocalClasses, on_delete=models.CASCADE, null=True)

    employers = models.ManyToManyField(EmployersPage, blank=True)

    links = models.ManyToManyField(PersonLink, blank=True)
    contacts = models.OneToOneField(PersonContacts, on_delete=models.CASCADE, null=True, blank=True)

    # events = models.ManyToManyField(AbstractEvent, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='persons_owner')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='persons_contributor')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='persons_author')


@receiver(post_save, sender=Person)
def create_person_local_classes(sender, instance, created, **kwargs):
    if created:
        local_classes = PersonLocalClasses.objects.create(person=instance)
        instance.local_classes = local_classes
        instance.save()


@receiver(post_save, sender=Person)
def create_person_contacts(sender, instance, created, **kwargs):
    if created:
        contacts = PersonContacts.objects.create(person=instance, author_id=instance.author_id)
        instance.contacts = contacts
        instance.save()


class Shop(EmployersPage):
    types = models.ManyToManyField(ShopType, blank=True)

    locations = models.ManyToManyField(ShopLocation, blank=True)
    employees = models.ManyToManyField(EmployeesPage, blank=True)

    links = models.ManyToManyField(ShopLink, blank=True)
    contacts = models.OneToOneField(ShopContacts, on_delete=models.CASCADE, null=True, blank=True)

    # events = models.ManyToManyField(AbstractEvent, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='shops_owner')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='shops_contributor')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='shops_author')


@receiver(post_save, sender=Shop)
def create_shop_contacts(sender, instance, created, **kwargs):
    if created:
        contacts = ShopContacts.objects.create(shop=instance, author_id=instance.author_id)
        instance.contacts = contacts
        instance.save()


class CustomerServices(EmployersPage):
    types = models.ManyToManyField(CustomerServicesType, blank=True)

    locations = models.ManyToManyField(CustomerServicesLocation, blank=True)
    employees = models.ManyToManyField(EmployeesPage, blank=True)

    links = models.ManyToManyField(CustomerServicesLink, blank=True)
    contacts = models.OneToOneField(CustomerServicesContacts, on_delete=models.CASCADE, null=True, blank=True)

    # events = models.ManyToManyField(AbstractEvent, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='customer_services_owner')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='customer_services_contributor')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='customer_services_author')


@receiver(post_save, sender=CustomerServices)
def create_customer_services_contacts(sender, instance, created, **kwargs):
    if created:
        contacts = CustomerServicesContacts.objects.create(customerservices=instance, author_id=instance.author_id)
        instance.contacts = contacts
        instance.save()


class Hall(EmployersPage):
    locations = models.ManyToManyField(HallLocation, blank=True)
    employees = models.ManyToManyField(EmployeesPage, blank=True)

    links = models.ManyToManyField(HallLink, blank=True)
    contacts = models.OneToOneField(HallContacts, on_delete=models.CASCADE, null=True, blank=True)

    # photos = models.ManyToManyField(HallPhoto, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='halls_owner')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='halls_contributor')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='halls_author')


@receiver(post_save, sender=Hall)
def create_hall_contacts(sender, instance, created, **kwargs):
    if created:
        contacts = HallContacts.objects.create(hall=instance, author_id=instance.author_id)
        instance.contacts = contacts
        instance.save()


class Resource(EmployersPage):
    employees = models.ManyToManyField(EmployeesPage, blank=True)

    links = models.ManyToManyField(ResourceLink, blank=True)
    contacts = models.OneToOneField(ResourceContacts, on_delete=models.CASCADE, null=True, blank=True)

    owners = models.ManyToManyField(UserProfile, blank=True, related_name='resources_owner')
    contributors = models.ManyToManyField(UserProfile, blank=True, related_name='resources_contributor')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='resources_author')


@receiver(post_save, sender=Resource)
def create_resource_contacts(sender, instance, created, **kwargs):
    if created:
        contacts = ResourceContacts.objects.create(resource=instance, author_id=instance.author_id)
        instance.contacts = contacts
        instance.save()
