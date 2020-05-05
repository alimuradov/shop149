import os

from django.conf import settings
from django.conf.urls.static import static

# from .urls import urlpatterns


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from .settings import INSTALLED_APPS, MIDDLEWARE

DEBUG=True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.88.160', '*', '0.0.0.0'] 


if DEBUG:   
    INSTALLED_APPS += (
        'debug_toolbar',
    )

    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
