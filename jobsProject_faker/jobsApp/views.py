from django.shortcuts import render
from jobsApp.models import *

# Create your views here.
def index(request):
    return render(request,'templates/testapp/index.html')

def hydjobs1(request):
    job_list = hydjobs.objects.order_by('id')
    my_dict = {'job_list':job_list}
    return render(request,'templates/testapp/hydjobs.html',context=my_dict)

def bangjobs1(request):
    job_list = bangjobs.objects.order_by('id')
    my_dict = {'job_list':job_list}
    return render(request,'templates/testapp/bangjobs.html',context=my_dict)

def chennaijobs1(request):
    job_list = chennaijobs.objects.order_by('id')
    my_dict = {'job_list':job_list}
    return render(request,'templates/testapp/chennaijobs.html',context=my_dict)

def punejobs1(request):
    job_list = punejobs.objects.order_by('id')
    my_dict = {'job_list':job_list}
    return render(request,'templates/testapp/punejobs.html',context=my_dict)


