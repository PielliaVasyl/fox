from entities.edit_forms.shop import EditShopTitleForm, EditShopDirectionsForm, EditShopCitiesForm, \
    EditShopDescriptionForm, EditShopImageForm, EditShopShopLocationForm, EditShopShopTypesForm, EditShopLinksForm, \
    EditShopPolicyForm, EditShopEmployeesForm, EditShopShopContactForm, EditShopSocialsForm

SHOP_EDIT_BUTTONS = [
    ('shop', 'title', 'Название'),
    ('shop', 'directions', 'Направления'),
    ('shop', 'cities', 'Города'),
    ('shop', 'types', 'Типы магазина'),
    ('shop', 'description', 'Описание'),
    ('shop', 'image', 'Изображение'),
    ('shop', 'shop-locations', 'Места'),
    ('shop', 'employees', 'Сотрудники'),
    ('shop', 'shop-links', 'Ссылки'),
    ('shop', 'shop-contacts', 'Контакты'),
    ('shop', 'policy', 'Права пользователей'),
]

SHOP_ATTRIBUTE_FORMS = {
    'title': EditShopTitleForm,
    'directions': EditShopDirectionsForm,
    'cities': EditShopCitiesForm,
    'description': EditShopDescriptionForm,
    'image': EditShopImageForm,
    'shop-locations': EditShopShopLocationForm,
    'types': EditShopShopTypesForm,
    'shop-links': EditShopLinksForm,
    'policy': EditShopPolicyForm,
    'employees': EditShopEmployeesForm,
    'contacts': EditShopShopContactForm,
    'socials': EditShopSocialsForm
}
