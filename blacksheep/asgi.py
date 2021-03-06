"""
ASGI config for blacksheep project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
import os

# Internal:
from django.core.asgi import get_asgi_application
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blacksheep.settings')

application = get_asgi_application()
