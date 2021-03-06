from django import forms
from studentApp.models import StudentRegisterModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentRegisterModel
        fields='__all__'