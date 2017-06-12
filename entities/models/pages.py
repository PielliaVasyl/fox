# from django.db import models
#
# from entities.models import Direction
# from entities.models import UserProfile
#
#
# class AbstractPage(models.Model):
#     title = models.CharField(max_length=100)
#
#     directions = models.ManyToManyField(Direction, blank=True)
#
#     description = models.TextField(blank=True)
#     image = models.ImageField(blank=True)
#
#     owners = models.ManyToManyField(UserProfile, blank=True, related_name='abstract_event_owners')
#     contributors = models.ManyToManyField(UserProfile, blank=True, related_name='abstract_event_contributors')
#     author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now=False, auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#
#     def __str__(self):
#         return '%s' % self.title
#
#     class Meta:
#         ordering = ('updated',)
