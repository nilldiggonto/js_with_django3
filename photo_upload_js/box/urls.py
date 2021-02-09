from .views import MainView,image_upload_view,PhotoShowListView,photo_list
from django.urls import path


urlpatterns = [
    path('',MainView.as_view(),name='index'),
    path('upload/',image_upload_view,name='upload'),

    path('list/',PhotoShowListView.as_view(),name='list'),
    path('list/json/',photo_list,name='list-json'),
]


