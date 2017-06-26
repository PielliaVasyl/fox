from django.db import models

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save




class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    role = models.CharField(max_length=50, blank=True)

    # def article_count(self):
    #     from entities.models.posts import Article
    #     # return len([i for i in self.abstractpost_set.all() if isinstance(i, (Article,))])
    #     return [i for i in self.abstractpost_set.all()]

    def name(self):
        return self.user.name

    def __str__(self):
        return "%s's profile" % self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
