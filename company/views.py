from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.db.models.deletion import ProtectedError
from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from . import forms


class CompanyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Company
    template_name = 'companies/company_list.html'
    context_object_name = 'companies'
    ordering = ['name']
    paginate_by = 10
    login_url = 'account_login'
    permission_required = 'company.view_company'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class CompanyDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Company
    template_name = 'companies/company_detail.html'
    login_url = 'account_login'
    permission_required = 'company.view_company'


class CompanyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Company
    template_name = 'companies/company_create.html'
    form_class = forms.CompanyForm
    success_url = reverse_lazy('company_list')
    login_url = 'account_login'
    permission_required = 'company.create_company'


class CompanyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Company
    template_name = 'companies/company_update.html'
    form_class = forms.CompanyForm
    success_url = reverse_lazy('company_list')
    login_url = 'account_login'
    permission_required = 'company.change_company'


class CompanyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Company
    template_name = 'companies/company_delete.html'
    error_template_name = 'error/error_delete.html'
    success_url = reverse_lazy('company_list')
    login_url = 'account_login'
    permission_required = 'company.delete_company'

    def post(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError as e:
            related_objects = list(e.protected_objects)
            return render(request, self.error_template_name, {'related_objects': related_objects})
