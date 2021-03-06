from django.shortcuts import render
from empApp.models import Employee
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'empApp/index.html')

def empview(request):
    emp_list = Employee.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request, 'empApp/empview.html', context=my_dict)