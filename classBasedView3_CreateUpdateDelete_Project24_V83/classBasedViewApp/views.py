from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from classBasedViewApp.models import CompanyModel

# Create your views here.
class CompanyListView(ListView):
    model = CompanyModel
    template_name = 'templates/testApp/companymodel_list.html'
    context_object_name = 'company_list'

class CompanyDetailView(DetailView):
    model = CompanyModel
    template_name = 'templates/testApp/companymodel_detail.html'
    context_object_name = 'companymodel_list'

class CompanyCreateView(CreateView):
    model = CompanyModel
    fields = ('name', 'ceo', 'location')
    template_name = 'templates/testApp/companymodel_form.html'
    context_object_name = 'companymodel_list'

class CompanyUpdateView(UpdateView):
    model = CompanyModel
    fields = ('name', 'ceo')
    template_name = 'templates/testApp/companymodel_form.html'
    context_object_name = 'companymodel_list'

class CompanyDeleteView(DeleteView):
    model = CompanyModel
    success_url = reverse_lazy('comapnymodel_list')
    template_name = 'templates/testApp/companymodel_confirm_delete.html'
    context_object_name = 'companymodel_list'

