from entities.edit_forms.customer_services import EditCustomerServicesTitleForm, EditCustomerServicesDirectionsForm, \
    EditCustomerServicesCitiesForm, EditCustomerServicesDescriptionForm, EditCustomerServicesImageForm, \
    EditCustomerServicesCustomerServicesLocationForm, EditCustomerServicesCustomerServicesTypesForm, \
    EditCustomerServicesLinksForm, EditCustomerServicesPolicyForm, EditCustomerServicesEmployeesForm, \
    EditCustomerServicesCustomerServicesContactForm, EditCustomerServicesSocialsForm

CUSTOMER_SERVICES_EDIT_BUTTONS = [
    ('customer-services', 'title', 'Название'),
    ('customer-services', 'directions', 'Направления'),
    ('customer-services', 'cities', 'Города'),
    ('customer-services', 'types', 'Типы услуг'),
    ('customer-services', 'description', 'Описание'),
    ('customer-services', 'image', 'Изображение'),
    ('customer-services', 'customer-services-locations', 'Места'),
    ('customer-services', 'employees', 'Сотрудники'),
    ('customer-services', 'customer-services-links', 'Ссылки'),
    ('customer-services', 'customer-services-contacts', 'Контакты'),
    ('customer-services', 'policy', 'Права пользователей'),
]

CUSTOMER_SERVICES_ATTRIBUTE_FORMS = {
    'title': EditCustomerServicesTitleForm,
    'directions': EditCustomerServicesDirectionsForm,
    'cities': EditCustomerServicesCitiesForm,
    'description': EditCustomerServicesDescriptionForm,
    'image': EditCustomerServicesImageForm,
    'customer-services-locations': EditCustomerServicesCustomerServicesLocationForm,
    'types': EditCustomerServicesCustomerServicesTypesForm,
    'customer-services-links': EditCustomerServicesLinksForm,
    'policy': EditCustomerServicesPolicyForm,
    'employees': EditCustomerServicesEmployeesForm,
    'contacts': EditCustomerServicesCustomerServicesContactForm,
    'socials': EditCustomerServicesSocialsForm
}
