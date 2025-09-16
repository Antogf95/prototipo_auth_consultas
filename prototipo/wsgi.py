"""
WSGI config for prototipo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prototipo.settings')

# application = get_wsgi_application()

import os
import sys

sys.path.append('D:/prototipo_consultas')  # Ruta donde está manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prototipo.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
