from django.shortcuts import render
from .models import TestSearch,PostUp
# Create your views here.
from django.views.generic import ListView
import json
from .forms import PostUpForm


class SearchListView(ListView):
    model = TestSearch
    template_name = 'search/list_item.html'

    def get_context_data(self,*args,**Kwargs):
        context = super().get_context_data(**Kwargs)
        context['json_data']= json.dumps(list(TestSearch.objects.values()))
        return context



#POST WITH PHOTO UPLOAD VIEW
def post_with_photo_view(request):
    template_name = 'search/post_up.html'
    form = PostUpForm(request.POST or None,request.FILES or None)
    context = {
        'form':form,

    }
    return render(request,template_name,context)