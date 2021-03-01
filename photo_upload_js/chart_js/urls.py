from django.urls import path
from .views import chatView,dynamic_chartView
urlpatterns = [
    path('',chatView,name='chart-view'),
    path('dynamic/',dynamic_chartView,name='dynamic-chart'),
]