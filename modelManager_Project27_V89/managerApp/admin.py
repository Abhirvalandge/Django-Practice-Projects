from django.contrib import admin
from managerApp.models import Employee,ProxyEmployee


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eadd']

class ProxyEmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eadd']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ProxyEmployee,ProxyEmployeeAdmin)