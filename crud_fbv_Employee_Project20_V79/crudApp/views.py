from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from crudApp.models import Employee
from crudApp.forms import EmployeeForm

# Create your views here.

def retrieve_view(request):
    employees=Employee.objects.all()
    return render(request,"testApp/index.html", {'employees':employees})


def create_view(request):
    form = EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,"templates/testApp/create.html",{'form':form})

#def save_view(request):
        #eno = request.POST.get("eno")
        #ename = request.POST.get("ename")
        #esal = request.POST.get("esal")
        #eadd = request.POST.get("eadd")
        #update_record = Employee(eno=eno, ename=ename, esal=esal, eadd=eadd).save()
        #return redirect('/')


def delete_view(request):
    id = request.GET.get("i")
    Employee.objects.filter(id=id).delete()
    return redirect('/')



#def update_view(request):
    #x=request.POST.get("u_id")
    #employees = Employee.objects.get(id=x)
    #return render(request, "testApp/update.html", {'employees':employees})

def update_view(request,id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Employee, id=id)

    # pass the object as instance in form
    form = EmployeeForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

        # add form dictionary to context
    context["form"] = form

    return render(request, "testApp/update.html", context)