from django.shortcuts import render
from managerApp.models import Employee
from django.db.models import Q
from django.db.models.functions import Lower
from django.db.models import Avg,Sum,Max,Min,Count

# Create your views here.
def retrieve_view(request):
    #employees = Employee.objects.all()
    #employees = Employee.objects.get_emp_sal_range(12000,17000)
    employees = Employee.objects.get_emp_sorted_by('ename')
    my_dict = {'employees': employees}
    return render(request, "testApp/index.html", my_dict)

