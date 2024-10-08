"""
WSGI config for thotex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thotex.settings')

application = get_wsgi_application()
application = WhiteNoise(application)
# application.add_files('/static/', prefix='more-files/')
