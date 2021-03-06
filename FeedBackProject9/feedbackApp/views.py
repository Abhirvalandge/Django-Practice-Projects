from django.shortcuts import render
from . import forms

# Create your views here.
def thankyouView(request):
    return render(request,"templates/testApp/thankyou.html")

def feedbackView(request):
    if request.method=='GET':
        form =forms.FeedBackForm()
        return render(request,"templates/testApp/feedback.html",{'form':form})
    form = forms.FeedBackForm()
    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form validation success and printing feedback info')
            print('Student Name:',form.cleaned_data['name'])
            print('Student Roll_no:',form.cleaned_data['roll_no'])
            print('Student Email:',form.cleaned_data['email'])
            print('Student Feedback:',form.cleaned_data['feedback'])
            return render(request,"templates/testApp/thankyou.html",{'name':form.cleaned_data['name']})

    return render(request,"templates/testApp/feedback.html",{'form':form})