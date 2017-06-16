# coding: utf-8

from entities.forms.classes import AbstractClassForm, AbstractGlobalClassForm, CityForm, DirectionForm, \
    AbstractLocalClassForm, DanceDirectionForm, DanceStyleForm

from entities.forms.supportclasses import AbstractLinkForm, AbstractEventLinkForm, AbstractPageLinkForm, \
    EventLocalClassesForm, PageLocalClassesForm

from entities.forms.types import AbstractTypeForm, EventTypeForm, PriceTypeForm, ExperienceLevelForm, \
    RepeatsTypeForm, DayOfTheWeekForm, PlaceTypeForm, ShopTypeForm, CustomerServicesTypeForm

from entities.forms.locations import AbstractMapCoordinatesForm, PlaceMapCoordinatesForm, SchoolMapCoordinatesForm, \
    OrganizationMapCoordinatesForm, ShopMapCoordinatesForm, HallMapCoordinatesForm, AbstractLocationForm, \
    EventLocationForm, PlaceLocationForm, SchoolLocationForm, OrganizationLocationForm, ShopLocationForm, \
    HallLocationForm

from entities.forms.contacts import AbstractSocialLinkForm, SocialLinkFBForm, SocialLinkVKForm, \
    SocialLinkInstagramForm, SocialLinkTwitterForm, SocialsForm, PhoneNumberForm, AbstractContactsForm, \
    SchoolContactsForm, OrganizationContactsForm, TeacherContactsForm, PersonContactsForm, ShopContactsForm, \
    HallContactsForm, ResourceContactsForm

from entities.forms.events import AbstractEventForm, EventForm, PromoActionForm

from entities.forms.pages import AbstractPageForm, PlaceForm, EmployersPageForm, EmployeesPageForm, SchoolForm, \
    OrganizationForm, TeacherForm, PersonForm, ShopForm, CustomerServicesForm, HallForm, ResourceForm
