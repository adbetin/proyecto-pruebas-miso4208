from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import console.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)

    'websocket': AuthMiddlewareStack(
        URLRouter(
            console.routing.websocket_urlpatterns
        )
    ),
})