from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]
INTERNAL_IPS = ['127.0.0.1', '::1','localhost']

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000',
# ]

# ALLOWED_ORIGINS = ['http://*', 'http://localhost:3000/*', 'http://localhost:3000']
# CSRF_TRUSTED_ORIGINS = ALLOWED_ORIGINS.copy()

INSTALLED_APPS += ['django_extensions','debug_toolbar']
MIDDLEWARE +=['debug_toolbar.middleware.DebugToolbarMiddleware']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
