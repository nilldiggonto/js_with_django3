from django.shortcuts import render
from .models import Salary

from django.http import JsonResponse


# Create your views here.
def chatView(request):
    template_name = 'chart/chart.html'

    qs = Salary.objects.all()

    month = []
    salary = []
    for q in qs:
        month.append(q.month)
        salary.append(q.earing)
    
    context = {
        'qs':qs,
        'month':month,
        'salary':salary
    }

    print(context['month'])

    return render(request,template_name,context)