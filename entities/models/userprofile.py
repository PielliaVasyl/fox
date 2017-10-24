from django.db import models

from django.contrib.auth.models import User, AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_facebook.models import FacebookModel

from entities.models.classes import City, Direction
from fox_knows import settings


class UserSettings(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, blank=True, null=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('updated',)


class UserProfile(AbstractUser, FacebookModel):
    description = models.TextField(blank=True)

    settings = models.OneToOneField(UserSettings, on_delete=models.CASCADE, null=True, blank=True)

    role = models.CharField(max_length=50, blank=True)

    def articles(self):
        return set(self.articles_contributor.all()) | set(self.articles_owner.all()) | set(self.articles_author.all())

    def photos(self):
        return set(self.photos_contributor.all()) | set(self.photos_owner.all()) | set(self.photos_author.all())

    def videos(self):
        return set(self.videos_contributor.all()) | set(self.videos_owner.all()) | set(self.videos_author.all())

    def audios(self):
        return set(self.audios_contributor.all()) | set(self.audios_owner.all()) | set(self.audios_author.all())

    def resources(self):
        return set(self.resources_contributor.all()) | set(self.resources_owner.all()) \
               | set(self.resources_author.all())

    def places(self):
        return set(self.places_contributor.all()) | set(self.places_owner.all()) | set(self.places_author.all())

    def organizations(self):
        return set(self.organizations_contributor.all()) | set(self.organizations_owner.all()) \
               | set(self.organizations_author.all())

    def persons(self):
        return set(self.persons_contributor.all()) | set(self.persons_owner.all()) | set(self.persons_author.all())

    def schools(self):
        return set(self.schools_contributor.all()) | set(self.schools_owner.all()) | set(self.schools_author.all())

    def teachers(self):
        return set(self.teachers_contributor.all()) | set(self.teachers_owner.all()) | set(self.teachers_author.all())

    def shops(self):
        return set(self.shops_contributor.all()) | set(self.shops_owner.all()) | set(self.shops_author.all())

    def customer_services(self):
        return set(self.customer_services_contributor.all()) | set(self.customer_services_owner.all()) \
               | set(self.customer_services_author.all())

    def halls(self):
        return set(self.halls_contributor.all()) | set(self.halls_owner.all()) | set(self.halls_author.all())

    def events(self):
        return set(self.events_contributor.all()) | set(self.events_owner.all()) | set(self.events_author.all())

    def promo_actions(self):
        return set(self.promo_actions_contributor.all()) | set(self.promo_actions_owner.all()) \
               | set(self.promo_actions_author.all())

    def name(self):
        return self.username

    def __str__(self):
        return "%s's profile" % self.username


@receiver(post_save, sender=UserProfile)
def create_user_settings(sender, instance, created, **kwargs):
    if created:
        user_settings = UserSettings.objects.create(userprofile=instance)
        instance.settings = user_settings
        instance.save()


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.get_or_create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()
