"""
ASGI config for clearance_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clearance_system.settings')

application = get_asgi_application()

###### d3v3l0p3d by z3k3_03 ##############