from django.shortcuts import render
from . import forms

# Create your views here.
def registerForms(request):
    form = forms.StudentForms()
    my_dict = {'form':form}
    return render(request, "testApp/register.html",context=my_dict)