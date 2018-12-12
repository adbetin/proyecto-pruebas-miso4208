from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/terminal/(?P<execution_id>[0-9a-f-]+)$', consumers.ConsoleConsumer),
]