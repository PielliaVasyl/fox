from django.db import models

from entities.models.classes import City
from entities.models.userprofile import UserProfile


class AbstractMapCoordinates(models.Model):
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'Lat:%s, lng: %s' % (self.lat, self.lng)

    class Meta:
        ordering = ('created',)
        abstract = True


class PlaceMapCoordinates(AbstractMapCoordinates):
    def __str__(self):
        if hasattr(self, 'placelocation'):
            return 'Place: %s - Lat:%s, lng: %s' % (self.placelocation.place_set.all(), self.lat, self.lng)
        return 'Place: Lat:%s, lng: %s' % (self.lat, self.lng)


class SchoolMapCoordinates(AbstractMapCoordinates):
    def __str__(self):
        if hasattr(self, 'schoollocation'):
            return 'School: %s - Lat:%s, lng: %s' % (self.schoollocation.school_set.all(), self.lat, self.lng)
        return 'School: Lat:%s, lng: %s' % (self.lat, self.lng)


class OrganizationMapCoordinates(AbstractMapCoordinates):
    def __str__(self):
        if hasattr(self, 'organizationlocation'):
            return 'Organization: %s - Lat:%s, lng: %s' % (self.organizationlocation.organization_set.all(),
                                                           self.lat, self.lng)
        return 'Organization: Lat:%s, lng: %s' % (self.lat, self.lng)


class ShopMapCoordinates(AbstractMapCoordinates):
    def __str__(self):
        if hasattr(self, 'shoplocation'):
            return 'Shop: %s - Lat:%s, lng: %s' % (self.shoplocation.shop_set.all(), self.lat, self.lng)
        return 'Shop: Lat:%s, lng: %s' % (self.lat, self.lng)


class HallMapCoordinates(AbstractMapCoordinates):
    def __str__(self):
        if hasattr(self, 'halllocation'):
            return 'Hall: %s - Lat:%s, lng: %s' % (self.halllocation.hall_set.all(), self.lat, self.lng)
        return 'Hall: Lat:%s, lng: %s' % (self.lat, self.lng)


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
        abstract = True


class EventLocation(AbstractLocation):
    pass


class PlaceLocation(AbstractLocation):
    coordinates = models.OneToOneField(PlaceMapCoordinates, on_delete=models.CASCADE, blank=True, null=True)


class SchoolLocation(AbstractLocation):
    coordinates = models.OneToOneField(SchoolMapCoordinates, on_delete=models.CASCADE, blank=True, null=True)
    # school = models.ForeignKey('School', on_delete=models.CASCADE, related_name="locations",
    #                            related_query_name="location", blank=True, null=True)


class OrganizationLocation(AbstractLocation):
    coordinates = models.OneToOneField(OrganizationMapCoordinates, on_delete=models.CASCADE, blank=True, null=True)


class ShopLocation(AbstractLocation):
    coordinates = models.OneToOneField(ShopMapCoordinates, on_delete=models.CASCADE, blank=True, null=True)


class HallLocation(AbstractLocation):
    coordinates = models.OneToOneField(HallMapCoordinates, on_delete=models.CASCADE, blank=True, null=True)
