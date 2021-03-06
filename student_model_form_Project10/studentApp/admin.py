from django.contrib import admin
from studentApp.models import StudentRegisterModel

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','marks']
admin.site.register(StudentRegisterModel,StudentAdmin)
