from .base import *
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-z_=#3tsg1fgnm!a5h_ct2p8__v*0f(arl6ul#mjh!a(%$&p*bv"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(', ')

CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default=' ').split()
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default=' ').split()


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

try:
    from .local import *
except ImportError:
    pass



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_FROM = config("EMAIL_FROM")
SITE_NAME = config("SITE_NAME")