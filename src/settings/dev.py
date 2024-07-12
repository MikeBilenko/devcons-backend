from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-z_=#3tsg1fgnm!a5h_ct2p8__v*0f(arl6ul#mjh!a(%$&p*bv"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost",
    "*",
    "http://192.168.0.204:3000"
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'mbdevcons@gmail.com'
EMAIL_HOST_PASSWORD = 'cgnx yxsc dstn hkyn'
SITE_NAME = "MbDev Cons"