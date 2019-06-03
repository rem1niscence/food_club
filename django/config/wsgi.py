"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

assert os.getenv('DJANGO_SETTINGS_MODULE') is not None, (
    'Please provide a DJANGO_SETTINGS_MODULE environment variable with a value'
)

application = get_wsgi_application()
