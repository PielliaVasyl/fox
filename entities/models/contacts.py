from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from entities.models.userprofile import UserProfile


class AbstractSocialLink(models.Model):
    link = models.URLField()

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.link

    class Meta:
        ordering = ('created',)
        abstract = True


class SocialLinkFB(AbstractSocialLink):
    pass


class SocialLinkVK(AbstractSocialLink):
    pass


class SocialLinkInstagram(AbstractSocialLink):
    pass


class SocialLinkTwitter(AbstractSocialLink):
    pass


class Socials(models.Model):
    fb = models.ManyToManyField(SocialLinkFB, blank=True)
    vk = models.ManyToManyField(SocialLinkVK, blank=True)
    instagram = models.ManyToManyField(SocialLinkInstagram, blank=True)
    twitter = models.ManyToManyField(SocialLinkTwitter, blank=True)

    def get_fbs(self):
        if self.fb.all():
            return "\n".join([p.link for p in self.fb.all()])
        return ''

    def get_vks(self):
        if self.fb.all():
            return "\n".join([p.link for p in self.vk.all()])
        return ''

    def get_instagrams(self):
        if self.fb.all():
            return "\n".join([p.link for p in self.instagram.all()])
        return ''

    def get_twitters(self):
        if self.fb.all():
            return "\n".join([p.link for p in self.twitter.all()])
        return ''

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    # def __str__(self):
        # return '%s' % self.abstractcontacts

    class Meta:
        ordering = ('updated',)


class PhoneNumber(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Введите номер телефона в формате: '+380XXXXXXX'. Разрешено до 15 цифр.")
    phone_number = models.CharField(max_length=16, validators=[phone_regex], blank=True)  # validators should be a list

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.phone_number

    class Meta:
        ordering = ('created',)


class AbstractContacts(models.Model):
    phone_numbers = models.ManyToManyField(PhoneNumber, blank=True)

    socials = models.OneToOneField(Socials, on_delete=models.CASCADE, blank=True, null=True)

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_phone_numbers(self):
        if self.phone_numbers.all():
            return "\n".join([p.phone_number for p in self.phone_numbers.all()])
        return ''

    class Meta:
        ordering = ('updated',)
        abstract = True


class SchoolContacts(AbstractContacts):
    pass
    # def __str__(self):
    #     return '%s' % self.school


@receiver(post_save, sender=SchoolContacts)
def create_school_contacts(sender, instance, created, **kwargs):
    if created:
        socials = Socials.objects.create(schoolcontacts=instance, author_id=instance.author_id)
        instance.socials = socials
        instance.save()


class OrganizationContacts(AbstractContacts):
    pass
    # def __str__(self):
    #     return '%s' % self.organization


class TeacherContacts(AbstractContacts):
    pass
    # def __str__(self):
    #     return '%s' % self.teacher


class PersonContacts(AbstractContacts):
    pass
    # def __str__(self):
    #     return '%s' % self.person


class ShopContacts(AbstractContacts):
    pass
    # def __str__(self):
    #     return '%s' % self.shop


class HallContacts(AbstractContacts):
    pass
    # def __str__(self):
    #     return '%s' % self.hall


class ResourceContacts(AbstractContacts):
    pass
    # def __str__(self):
    #     return '%s' % self.resource
