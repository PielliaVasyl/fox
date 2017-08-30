from django.contrib import admin


from entities.forms.pages import PlaceForm, EmployersPageForm, EmployeesPageForm, SchoolForm, \
    OrganizationForm, TeacherForm, PersonForm, ShopForm, HallForm, ResourceForm, CustomerServicesForm
from entities.models.pages import Place, EmployersPage, EmployeesPage, School, Organization, Teacher, \
    Person, Shop, Hall, Resource, CustomerServices


# class AbstractPageAdmin(admin.ModelAdmin):
#     list_display = ['title', 'get_directions', 'get_cities', 'description', 'image', 'get_links',
#                     'get_owners', 'get_contributors', 'author', 'created', 'updated']
#     form = AbstractPageForm
#
# admin.site.register(AbstractPage, AbstractPageAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'local_classes', 'get_types', 'get_locations',
                    'description', 'image', 'get_links', 'owns', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = PlaceForm

admin.site.register(Place, PlaceAdmin)


class EmployersPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'description', 'image', 'get_links', 'get_owners',
                    'get_contributors', 'created', 'updated']
    form = EmployersPageForm

admin.site.register(EmployersPage, EmployersPageAdmin)


class EmployeesPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'description', 'image', 'get_links', 'get_owners',
                    'get_contributors', 'created', 'updated']
    form = EmployeesPageForm

admin.site.register(EmployeesPage, EmployeesPageAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'local_classes', 'get_locations', 'get_employees',
                    'description', 'image', 'get_links', 'contacts', 'owns', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = SchoolForm

admin.site.register(School, SchoolAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'local_classes', 'get_locations', 'get_employees',
                    'description', 'image', 'get_links', 'contacts', 'owns', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = OrganizationForm

admin.site.register(Organization, OrganizationAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'local_classes', 'get_employers', 'description', 'image',
                    'get_links', 'contacts', 'owns', 'get_owners', 'get_contributors', 'author', 'created', 'updated']
    form = TeacherForm

admin.site.register(Teacher, TeacherAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'local_classes', 'get_employers', 'description', 'image',
                    'get_links', 'contacts', 'owns', 'get_owners', 'get_contributors', 'author', 'created', 'updated']
    form = PersonForm

admin.site.register(Person, PersonAdmin)


class ShopAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'get_types', 'get_locations', 'get_employees',
                    'description', 'image', 'get_links', 'contacts', 'owns', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = ShopForm

admin.site.register(Shop, ShopAdmin)


class CustomerServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'get_types', 'get_locations', 'get_employees',
                    'description', 'image', 'get_links', 'contacts', 'owns', 'get_owners', 'get_contributors',
                    'author', 'created', 'updated']
    form = CustomerServicesForm

admin.site.register(CustomerServices, CustomerServicesAdmin)


class HallAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'get_locations', 'get_employees', 'description',
                    'image', 'get_links', 'contacts', 'owns', 'get_owners', 'get_contributors', 'author', 'created',
                    'updated']
    form = HallForm

admin.site.register(Hall, HallAdmin)


class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_directions', 'get_cities', 'description', 'image', 'get_links', 'contacts', 'owns',
                    'get_owners', 'get_contributors', 'author', 'created', 'updated']
    form = ResourceForm

admin.site.register(Resource, ResourceAdmin)
