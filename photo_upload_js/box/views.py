from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import TemplateView
from .models import BoxforImage
# Create your views here.

class MainView(TemplateView):
    template_name = 'box/index.html'


def image_upload_view(request):
    print('abc')
    if request.method == 'POST':
        box_file = request.FILES.get('file')
        BoxforImage.objects.create(upload=box_file)
        return HttpResponse('upload')
    return JsonResponse({'get':'not allowed'})
    # return HttpResponse('upload')

