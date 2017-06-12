from django.core.validators import RegexValidator
from django.db import models

from entities.models import UserProfile


class AbstractSocialLink(models.Model):
    link = models.URLField()

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.link

    class Meta:
        ordering = ('created',)


class SocialLinkFB(AbstractSocialLink):
    pass


class SocialLinkVK(AbstractSocialLink):
    pass


class SocialLinkInstagram(AbstractSocialLink):
    pass


class SocialLinkTwitter(AbstractSocialLink):
    pass


class Socials(models.Model):
    title = models.CharField(max_length=50)
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

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('title',)


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

    def get_phone_numbers(self):
        if self.phone_numbers.all():
            return "\n".join([p.phone_number for p in self.phone_numbers.all()])
        return ''

    socials = models.ForeignKey(Socials, on_delete=models.CASCADE, blank=True, null=True)

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('updated',)


class SchoolContacts(AbstractContacts):
    def __str__(self):
        return '%s' % self.school


class OrganizationContacts(AbstractContacts):
    def __str__(self):
        return '%s' % self.organization


class TeacherContacts(AbstractContacts):
    def __str__(self):
        return '%s' % self.teacher


class PersonContacts(AbstractContacts):
    def __str__(self):
        return '%s' % self.person


class ShopContacts(AbstractContacts):
    def __str__(self):
        return '%s' % self.shop


class HallContacts(AbstractContacts):
    def __str__(self):
        return '%s' % self.hall


class ResourceContacts(AbstractContacts):
    def __str__(self):
        return '%s' % self.resource
