from django.urls import path
from .views import js_view

urlpatterns = [
    path('',js_view,name='jsview'),
]