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



def dynamic_chartView(request):

    # def connect(self):
    #     self.accept()

    # for i in range(1000):
    #     self.send(json.dumps({'value':randint(-20,20)}))

    template_name = 'chart/dynamic.html'

    context = {

    }

    return render(request,template_name,context)