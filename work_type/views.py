from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.db.models.deletion import ProtectedError
from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from . import forms


class WorkTypeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.WorkType
    template_name = 'work_type/work_type_list.html'
    context_object_name = 'work_types'
    ordering = ['name']
    login_url = 'account_login'
    permission_required = 'work_type.view_worktype'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class WorkTypeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.WorkType
    template_name = 'work_type/work_type_detail.html'
    login_url = 'account_login'
    permission_required = 'work_type.view_worktype'


class WorkTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.WorkType
    template_name = 'work_type/work_type_create.html'
    form_class = forms.WorkTypeForm
    success_url = reverse_lazy('work_type_list')
    login_url = 'account_login'
    permission_required = 'work_type.create_worktype'


class WorkTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.WorkType
    template_name = 'work_type/work_type_update.html'
    form_class = forms.WorkTypeForm
    success_url = reverse_lazy('work_type_list')
    login_url = 'account_login'
    permission_required = 'work_type.change_worktype'


class WorkTypeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.WorkType
    template_name = 'work_type/work_type_delete.html'
    error_template_name = 'error/error_delete.html'
    success_url = reverse_lazy('work_type_list')
    login_url = 'account_login'
    permission_required = 'work_type.delete_worktype'

    def post(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError as e:
            related_objects = list(e.protected_objects)
            return render(request, self.error_template_name, {'related_objects': related_objects})
