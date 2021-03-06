from django.shortcuts import render
from sessionApp.forms import AgeForm,NameForm,GfForm

# Create your views here.
def name_view(request):
    form = NameForm()
    return render(request,"name.html",{'form':form})


def age_view(request):
    name = request.GET['name']
    request.session['name']=name
    form = AgeForm()
    return render(request,"age.html",{'form':form})


def gfname_view(request):
    age = request.GET['age']
    request.session['age'] = age
    form = GfForm()
    return render(request, "gf.html", {'form': form})


def results_view(request):
    gfname = request.GET['gfname']
    request.session['gfname'] = gfname
    return render(request, "results.html")
