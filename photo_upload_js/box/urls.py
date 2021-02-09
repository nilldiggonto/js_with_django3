from .views import MainView,image_upload_view
from django.urls import path


urlpatterns = [
    path('',MainView.as_view(),name='index'),
    path('upload/',image_upload_view,name='upload'),
]


