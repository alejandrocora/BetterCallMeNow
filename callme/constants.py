DEFAULT_HEADER = 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'
DUCKDUCKGO_SEARCH_URL = 'https://html.duckduckgo.com/html?q='
GOOGLE_SEARCH_URL = 'https://www.google.com/search?q='

#COMMON_CFORM_PARAMETERS = ['contactForm']
COMMON_PHONE_PARAMETERS = ['phone', 'telephone', 'telefono', 'tfo', 'tel'] # include 'number' or maybe it will bug the request?
COMMON_NAME_PARAMETERS = ['name', 'nombre', 'contact']
COMMON_SURNAME_PARAMETERS = ['last name', 'surname', 'apellido']
COMMON_EMAIL_PARAMETERS = ['mail', 'correo']
COMMON_ORGANIZATION_PARAMETERS = ['organization', 'company', 'organizacion', 'compania']
COMMON_WEBSITE_PARAMETERS = ['site', 'web', 'sitio']
COMMON_TERMS_PARAMETERS = ['terms', 'conditions', 'checkbox', 'acceptance', 'terminos', 'condiciones']
COMMON_HOUR_PARAMETERS = ['hour', 'hora']
COMMON_TEXT_PARAMETERS = ['text', 'comments', 'area', 'mensaje']

COMMON_NAME = 'John'
COMMON_SURNAME = 'Smith'
COMMON_EMAIL = 'johnsmith@example.com'
COMMON_ORGANIZATION = 'John Company'
COMMON_WEBSITE = 'example.com'
COMMON_UNDEFINED = 'Need help!'


COMMON_PARAMETERS = {
    'name': COMMON_NAME_PARAMETERS,
    'surname': COMMON_SURNAME_PARAMETERS,
    'mail': COMMON_EMAIL_PARAMETERS,
    'organization': COMMON_ORGANIZATION_PARAMETERS,
    'site': COMMON_WEBSITE_PARAMETERS,
    'terms': COMMON_TERMS_PARAMETERS,
    'text': COMMON_TEXT_PARAMETERS
}

COMMON_PAYLOAD = {
    'name': COMMON_NAME,
    'surname': COMMON_SURNAME,
    'mail': COMMON_EMAIL,
    'organization': COMMON_ORGANIZATION,
    'site': COMMON_WEBSITE,
    'terms': 'true',
    'text': 'Hello, my name is ' + COMMON_NAME + ' ' + COMMON_SURNAME
}