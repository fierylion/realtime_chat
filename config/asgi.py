"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
import django
import os

from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application
import realtime_chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = ProtocolTypeRouter(
    {
        'http':get_asgi_application(),
        'websocket': URLRouter(realtime_chat.routing.websocket_urlpatterns),
    }
)
