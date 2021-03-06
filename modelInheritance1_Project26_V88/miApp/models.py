from django.db import models

# Create your models here.
# 1. Abstract Base Class Model Inheritance
class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=264)
    class Meta:
        abstract = True

class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher(ContactInfo):
    subject = models.CharField(max_length=128)
    salary = models.IntegerField()


# 2. Multi Table Inheritance
class ContactInfo1_Multi(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=264)

class Student1_Multi(ContactInfo1_Multi):
    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher1_Multi(ContactInfo1_Multi):
    subject = models.CharField(max_length=128)
    salary = models.IntegerField()


# 3. Multilevel Inheritance
class Parent_Multilevel(models.Model):
    fb1 = models.CharField(max_length=64)
    fb2 = models.CharField(max_length=64)

class Child_Multilevel(Parent_Multilevel):
    fb3 = models.CharField(max_length=64)
    fb4 = models.CharField(max_length=64)

class Sub_Child_Multilevel(Child_Multilevel):
    fb5 = models.CharField(max_length=64)


# 4. Proxy Model Inheritance
