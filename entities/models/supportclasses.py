from django.db import models

from entities.models.classes import DanceDirectionClass, DanceStyleClass


class EventLocalClasses(models.Model):
    dance_styles = models.ManyToManyField(DanceStyleClass, blank=True)
    dance_directions = models.ManyToManyField(DanceDirectionClass, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_directions(self):
        if self.dance_directions.all():
            return "\n".join([p.title for p in self.dance_directions.all()])
        return ''

    def __str__(self):
        return '%s, %s' % (self.dance_styles.all(), self.dance_directions.all())

    class Meta:
        ordering = ('updated',)


class PromoActionLocalClasses(models.Model):
    dance_styles = models.ManyToManyField(DanceStyleClass, blank=True)
    dance_directions = models.ManyToManyField(DanceDirectionClass, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_directions(self):
        if self.dance_directions.all():
            return "\n".join([p.title for p in self.dance_directions.all()])
        return ''

    def __str__(self):
        return '%s, %s' % (self.dance_styles.all(), self.dance_directions.all())

    class Meta:
        ordering = ('updated',)


class PageLocalClasses(models.Model):
    dance_styles = models.ManyToManyField(DanceStyleClass)
    dance_directions = models.ManyToManyField(DanceDirectionClass)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_styles_list(self):
        if self.dance_styles.all():
            return [p.title for p in self.dance_styles.all()]
        return []

    def get_dance_directions(self):
        if self.dance_directions.all():
            return "\n".join([p.title for p in self.dance_directions.all()])
        return ''

    def __str__(self):
        return '%s - %s' % (self.get_dance_directions(), self.get_dance_styles())

    class Meta:
        ordering = ('updated',)


class PlaceLocalClasses(models.Model):
    dance_styles = models.ManyToManyField(DanceStyleClass)
    dance_directions = models.ManyToManyField(DanceDirectionClass)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_styles_list(self):
        if self.dance_styles.all():
            return [p.title for p in self.dance_styles.all()]
        return []

    def get_dance_directions(self):
        if self.dance_directions.all():
            return "\n".join([p.title for p in self.dance_directions.all()])
        return ''

    def __str__(self):
        return '%s - %s' % (self.get_dance_directions(), self.get_dance_styles())

    class Meta:
        ordering = ('updated',)


class SchoolLocalClasses(models.Model):
    dance_styles = models.ManyToManyField(DanceStyleClass)
    dance_directions = models.ManyToManyField(DanceDirectionClass)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_styles_list(self):
        if self.dance_styles.all():
            return [p.title for p in self.dance_styles.all()]
        return []

    def get_dance_directions(self):
        if self.dance_directions.all():
            return "\n".join([p.title for p in self.dance_directions.all()])
        return ''

    def __str__(self):
        return '%s - %s' % (self.get_dance_directions(), self.get_dance_styles())

    class Meta:
        ordering = ('updated',)


class OrganizationLocalClasses(models.Model):
    dance_styles = models.ManyToManyField(DanceStyleClass)
    dance_directions = models.ManyToManyField(DanceDirectionClass)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_styles_list(self):
        if self.dance_styles.all():
            return [p.title for p in self.dance_styles.all()]
        return []

    def get_dance_directions(self):
        if self.dance_directions.all():
            return "\n".join([p.title for p in self.dance_directions.all()])
        return ''

    def __str__(self):
        return '%s - %s' % (self.get_dance_directions(), self.get_dance_styles())

    class Meta:
        ordering = ('updated',)


class TeacherLocalClasses(models.Model):
    dance_styles = models.ManyToManyField(DanceStyleClass)
    dance_directions = models.ManyToManyField(DanceDirectionClass)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_styles_list(self):
        if self.dance_styles.all():
            return [p.title for p in self.dance_styles.all()]
        return []

    def get_dance_directions(self):
        if self.dance_directions.all():
            return "\n".join([p.title for p in self.dance_directions.all()])
        return ''

    def __str__(self):
        return '%s - %s' % (self.get_dance_directions(), self.get_dance_styles())

    class Meta:
        ordering = ('updated',)


class PersonLocalClasses(models.Model):
    dance_styles = models.ManyToManyField(DanceStyleClass)
    dance_directions = models.ManyToManyField(DanceDirectionClass)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_styles_list(self):
        if self.dance_styles.all():
            return [p.title for p in self.dance_styles.all()]
        return []

    def get_dance_directions(self):
        if self.dance_directions.all():
            return "\n".join([p.title for p in self.dance_directions.all()])
        return ''

    def __str__(self):
        return '%s - %s' % (self.get_dance_directions(), self.get_dance_styles())

    class Meta:
        ordering = ('updated',)
