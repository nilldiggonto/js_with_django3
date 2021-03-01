from django.shortcuts import render

# Create your views here.
def js_view(request):
    template_name= 'app_js/example.html'

    return render(request,template_name)