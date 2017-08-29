# coding: utf-8

from entities.forms.classes import AbstractClassForm, AbstractGlobalClassForm, CityForm, DirectionForm, \
    AbstractLocalClassForm, DanceDirectionClassForm, DanceDirectionClassForm

from entities.forms.tags import AbstractTagForm, GlobalTagForm, CityTagForm, DirectionTagForm, LocalTagForm, \
    DanceTagForm, DanceStyleTagForm, DanceStyleCountTagForm, DanceStyleDistanceTagForm, DanceDirectionTagForm, \
    PostTagForm, ArticleTagForm, VideoTagForm, AudioTagForm, PhotoTagForm, PostGroupTagForm, ChapterTagForm, \
    PlaylistTagForm, TracklistTagForm, AlbumTagForm

from entities.forms.links import AbstractLinkForm, EventLinkForm, PromoActionLinkForm, PlaceLinkForm, SchoolLinkForm, \
    OrganizationLinkForm, TeacherLinkForm, PersonLinkForm, ShopLinkForm, CustomerServicesLinkForm, HallLinkForm, \
    ResourceLinkForm, PlaylistLinkForm, ArticleLinkForm, PhotoLinkForm, VideoLinkForm, AudioLinkForm

from entities.forms.supportclasses import EventLocalClassesForm, PageLocalClassesForm

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

from entities.forms.events import EventForm, PromoActionForm

from entities.forms.pages import PlaceForm, EmployersPageForm, EmployeesPageForm, SchoolForm, \
    OrganizationForm, TeacherForm, PersonForm, ShopForm, CustomerServicesForm, HallForm, ResourceForm

from entities.forms.posts import AlbumForm, ArticleForm, AudioForm, ChapterForm, PhotoForm, PlaylistForm, \
    TracklistForm, VideoForm, DanceDirectionForm, DanceStyleForm
