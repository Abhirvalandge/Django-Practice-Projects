from django.contrib import admin
from classBasedViewApp.models import CompanyModel

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','ceo','location']

admin.site.register(CompanyModel,CompanyAdmin)