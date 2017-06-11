"""
WSGI config for woit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "woit.settings"

application = get_wsgi_application()

# def application(environ, response):
# 	os.environ['WOIT_ENV'] = environ['WOIT_ENV']
# 	return get_wsgi_application()(environ, response)