# coding: utf-8

from django import forms

from entities.models import AbstractPage, Place, EmployersPage, EmployeesPage, School, Organization, Teacher, \
    Person, Shop, Hall, Resource


class AbstractPageForm(forms.ModelForm):
    class Meta:
        model = AbstractPage
        fields = ['title', 'directions', 'cities', 'description', 'image', 'links', 'owners', 'contributors', 'author']


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title', 'directions', 'cities', 'local_classes', 'types', 'locations', 'description', 'image',
                  'links', 'owners', 'contributors', 'author']


class EmployersPageForm(forms.ModelForm):
    class Meta:
        model = EmployersPage
        fields = ['title', 'directions', 'cities', 'description', 'image', 'links', 'owners', 'contributors', 'author']


class EmployeesPageForm(forms.ModelForm):
    class Meta:
        model = EmployeesPage
        fields = ['title', 'directions', 'cities', 'description', 'image', 'links', 'owners', 'contributors', 'author']


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['title', 'directions', 'cities', 'local_classes', 'locations', 'employees', 'description', 'image',
                  'links', 'contacts', 'owners', 'contributors', 'author']


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['title', 'directions', 'cities', 'local_classes', 'locations', 'employees', 'description', 'image',
                  'links', 'contacts', 'owners', 'contributors', 'author']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['title', 'directions', 'cities', 'local_classes', 'employers', 'description', 'image',
                  'links', 'contacts', 'owners', 'contributors', 'author']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['title', 'directions', 'cities', 'local_classes', 'employers', 'description', 'image',
                  'links', 'contacts', 'owners', 'contributors', 'author']


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'directions', 'cities', 'types', 'locations', 'employees', 'description',
                  'image', 'links', 'contacts', 'owners', 'contributors', 'author']


class CustomerServicesForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'directions', 'cities', 'types', 'locations', 'employees', 'description',
                  'image', 'links', 'contacts', 'owners', 'contributors', 'author']


class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['title', 'directions', 'cities', 'locations', 'employees', 'description',
                  'image', 'links', 'contacts', 'owners', 'contributors', 'author']


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'directions', 'cities', 'description', 'image', 'links', 'contacts', 'owners',
                  'contributors', 'author']
