import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud_fbv_Employee_Project20_V79.settings')
import django
django.setup()

from crudApp.models import *
from faker import Faker
from random import *

fake=Faker()
def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num = num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=fake.name()
        fesal=randint(10000,20000)
        feadd=fake.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eadd=feadd)
populate(25)
