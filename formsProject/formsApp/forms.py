from django import forms

class StudentForms(forms.Form):
    name = forms.CharField(max_length=30)
    roll_no = forms.IntegerField()