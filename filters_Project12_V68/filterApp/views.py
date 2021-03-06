from django.shortcuts import render
from filterApp.models import FilterModel

# Create your views here.
def upper_view(request):
    my_list = FilterModel.objects.all()
    return render(request,"templates/testApp/upper.html",{'my_list':my_list})


def lower_view(request):
    my_list = FilterModel.objects.all()
    return render(request, "templates/testApp/lower.html", {'my_list': my_list})


def truncute_view(request):
    my_list = FilterModel.objects.all()
    return render(request, "templates/testApp/truncate.html", {'my_list': my_list})
