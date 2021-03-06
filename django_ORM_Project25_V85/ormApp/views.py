from django.shortcuts import render
from ormApp.models import Employee
from django.db.models import Q
from django.db.models.functions import Lower
from django.db.models import Avg,Sum,Max,Min,Count

# Create your views here.
def retrieve_view(request):
    #employees=Employee.objects.all()
    #employees = Employee.objects.filter(esal__gt=(15000))
    #employees = Employee.objects.filter(esal__gte=(15000))
    #employees = Employee.objects.filter(esal__lt=(15000))
    #employees = Employee.objects.filter(esal__lte=(15000))

    #various possibilities of field lookup
    #employees = Employee.objects.filter(id__exact=14)
    #employees = Employee.objects.filter(ename__exact='Laura Morris')
    #employees = Employee.objects.filter(ename__iexact='laura morris')
    #employees = Employee.objects.filter(ename__contains='j')
    #employees = Employee.objects.filter(ename__icontains='J')
    #employees = Employee.objects.filter(id__in=['20','21','22','23'])
    #employees = Employee.objects.filter(ename__istartswith='A')
    #employees = Employee.objects.filter(ename__iendswith='s')

    # IMPLEMENTEION OF 'OR' QUERIES
    #employees = Employee.objects.filter(esal__range=(15000,25000))| Employee.objects.filter(ename__istartswith='A')
    #employees = Employee.objects.filter(Q(esal__range=(15000,25000))| Q(ename__istartswith='D'))

    # IMPLEMENTEION OF 'AND' QUERIES
    #employees = Employee.objects.filter(esal__range=(5000, 15000),ename__istartswith='a')
    #employees = Employee.objects.filter(esal__range=(15000, 25000)) & Employee.objects.filter(ename__istartswith='A')
    #employees = Employee.objects.filter(Q(esal__range=(15000, 25000)) & Q(ename__istartswith='D'))

    # IMPLEMENTEION OF 'NOT' QUERIES
    #employees = Employee.objects.exclude(esal__range=(6000, 16000))
    #employees = Employee.objects.filter(~Q(esal__range=(6000, 16000)))

    # IMPLEMENTATION OF 'UNION' OPERATIONS FOR QUERY SET
    #qs1 = Employee.objects.filter(esal__lt=(15000))
    #qs2 = Employee.objects.filter(ename__iendswith='n')
    #employees = qs1.union(qs2)

    #How to Select only few Columns
    #employees = Employee.objects.all().values_list('ename','esal') #not working
    #employees = Employee.objects.all().values('ename','esal')
    #employees = Employee.objects.all().only('esal') #not working

    #Aggregate Functions
    #avg1 = Employee.objects.all().aggregate(Avg('esal'))
    #max = Employee.objects.all().aggregate(Max('esal'))
    #min = Employee.objects.all().aggregate(Min('esal'))
    #sum = Employee.objects.all().aggregate(Sum('esal'))
    #count = Employee.objects.all().aggregate(Count('esal'))
    #my_dict = {'avg1':avg1,'max':max,'min':min,'sum':sum,'count':count}
    #return render(request,"testApp/aggregate.html", my_dict)


    # CRUD OPERATIONS
    # 1. CREATE Operation
    #employees1 = Employee.objects.create(eno=1001,ename='Abhirva',esal=50000,eadd='Mahajnapeth').save()
    #employees = Employee.objects.all()
    #my_dict = {'employees':employees}

    # 2. UPDATE Operation
    #employees1 = Employee.objects.get(eno=1001)
    #employees = Employee.objects.all()
    #my_dict = {'employees': employees}

    # 3. DELETE Operation
    #employees1 = Employee.objects.filter(ename='Abhirva').delete()
    #employees = Employee.objects.all()

    # QUERY SET IN SORTING ORDER
    #  *Ascending Order*
    #employees = Employee.objects.all().order_by('eno')

    #  *descending Order*
    #employees = Employee.objects.all().order_by('-eno')[0:3]

    # Alphabetical Order
    #employees = Employee.objects.all().order_by('ename') # For (A to Z)
    #employees = Employee.objects.all().order_by('-ename') #for reverse(Z to A)
    employees = Employee.objects.all().order_by(Lower('ename')) #for Lower Case(a to z)

    my_dict = {'employees': employees}
    return render(request,"testApp/index.html", my_dict)

