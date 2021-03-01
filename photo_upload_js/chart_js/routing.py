from django.urls import path
from .consumers import GraphConsumer

# from .

ws_urlpatterns = [
    path('ws/graph/',GraphConsumer.as_asgi())
    
]