from django.urls import path
from .views import SearchListView,post_with_photo_view

urlpatterns = [
    path('',SearchListView.as_view(),name='search-list'),
    path('up/',post_with_photo_view,name='up-post'),
]