from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>This is Class Based View Response.</h1>')

class HelloWorldTemplateView(TemplateView):
    template_name = 'testApp/results.html'


class HelloWorldTemplateContext(TemplateView):
    template_name = 'testApp/info.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['name']='Abhirva'
        context['subject']='Python'
        context['marks']=100
        return context
