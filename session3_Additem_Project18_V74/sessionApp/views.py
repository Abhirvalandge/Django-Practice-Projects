from django.shortcuts import render
from sessionApp.forms import AddItemForm

# Create your views here.
def addItem_view(request):
    form = AddItemForm()
    if request.method=='POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(60)
        age = request.session.get_expiry_age()
        date = request.session.get_expiry_date()
        print('Expiry Age: ', age)
        print('Expiry Date: ', date)
    return render(request,"testApp/add_item.html",{'form':form})


def displayItem_view(request):
    return render(request,"testApp/display_item.html")
