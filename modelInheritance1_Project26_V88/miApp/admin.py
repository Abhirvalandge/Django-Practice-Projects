from django.contrib import admin
from miApp.models import ContactInfo1_Multi,Student1_Multi,Teacher1_Multi,Parent_Multilevel,Child_Multilevel,Sub_Child_Multilevel

# Register your models here.
admin.site.register(ContactInfo1_Multi)
admin.site.register(Student1_Multi)
admin.site.register(Teacher1_Multi)
admin.site.register(Parent_Multilevel)
admin.site.register(Child_Multilevel)
admin.site.register(Sub_Child_Multilevel)