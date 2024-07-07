from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models.deletion import ProtectedError
from django.shortcuts import render
from django.db.models import Q
from . import models
from . import forms
from django.urls import reverse_lazy


class ContractorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Contractor
    template_name = 'contractors/contractor_list.html'
    context_object_name = 'contractors'
    ordering = ['-created_at']
    paginate_by = 10
    login_url = 'account_login'
    permission_required = 'contractors.view_contractor'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')

        if search_query:
            queryset = queryset.filter(
                Q(work_code__icontains=search_query) | Q(company__name__icontains=search_query)
            )

        return queryset


class ContractorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Contractor
    template_name = 'contractors/contractor_detail.html'
    context_object_name = 'contractor'
    login_url = 'account_login'
    permission_required = 'contractors.view_contractor'


class ContractorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Contractor
    template_name = 'contractors/contractor_create.html'
    form_class = forms.ContractorForm
    success_url = reverse_lazy('contractor_list')
    login_url = 'account_login'
    permission_required = 'contractors.create_contractor'


class ContractorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Contractor
    template_name = 'contractors/contractor_update.html'
    form_class = forms.ContractorForm
    success_url = reverse_lazy('contractor_list')
    login_url = 'account_login'
    permission_required = 'contractors.change_contractor'


class ContractorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Contractor
    template_name = 'contractors/contractor_delete.html'
    error_template_name = 'error/error_delete.html'
    success_url = reverse_lazy('contractor_list')
    login_url = 'account_login'
    permission_required = 'contractors.delete_contractor'

    def post(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError as e:
            related_objects = list(e.protected_objects)
            return render(request, self.error_template_name, {'related_objects': related_objects})
