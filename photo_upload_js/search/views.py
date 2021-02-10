from django.shortcuts import render
from .models import TestSearch
# Create your views here.
from django.views.generic import ListView

class SearchListView(ListView):
    model = TestSearch
    template_name = 'search/list_item.html'
