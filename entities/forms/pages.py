# coding: utf-8

from django import forms

from entities.models import Place, EmployersPage, EmployeesPage, School, Organization, Teacher, Person, Shop, Hall, \
    Resource
from entities.models.pages import CustomerServices

CUT_FORM_FIELDS = ['title', 'author']


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title', 'directions', 'cities', 'local_classes', 'types', 'locations', 'description', 'image',
                  'links', 'owners', 'contributors', 'author']


class EmployersPageForm(forms.ModelForm):
    class Meta:
        model = EmployersPage
        fields = ['title', 'directions', 'cities', 'description', 'image']


class EmployeesPageForm(forms.ModelForm):
    class Meta:
        model = EmployeesPage
        fields = ['title', 'directions', 'cities', 'description', 'image']


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


class CutPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = CUT_FORM_FIELDS


class CutSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = CUT_FORM_FIELDS


class CutTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = CUT_FORM_FIELDS


class CutOrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = CUT_FORM_FIELDS


class CutPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = CUT_FORM_FIELDS


class CutShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = CUT_FORM_FIELDS


class CutCustomerServicesForm(forms.ModelForm):
    class Meta:
        model = CustomerServices
        fields = CUT_FORM_FIELDS


class CutHallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = CUT_FORM_FIELDS


class CutResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = CUT_FORM_FIELDS
