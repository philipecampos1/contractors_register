from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.db.models.deletion import ProtectedError
from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from . import forms


class WorkerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Worker
    template_name = 'workers/worker_list.html'
    context_object_name = 'workers'
    ordering = ['name']
    paginate_by = 10
    login_url = 'account_login'
    permission_required = 'workers.view_worker'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class WorkerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Worker
    template_name = 'workers/worker_detail.html'
    login_url = 'account_login'
    permission_required = 'workers.view_worker'


class WorkerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Worker
    template_name = 'workers/worker_update.html'
    form_class = forms.WorkerForm
    success_url = reverse_lazy('worker_list')
    login_url = 'account_login'
    permission_required = 'workers.view_worker'


class WorkerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Worker
    template_name = 'workers/worker_create.html'
    form_class = forms.WorkerForm
    success_url = reverse_lazy('worker_list')
    login_url = 'account_login'
    permission_required = 'workers.create_worker'


class WorkerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Worker
    template_name = 'workers/worker_delete.html'
    error_template_name = 'error/error_delete.html'
    success_url = reverse_lazy('worker_list')
    login_url = 'account_login'
    permission_required = 'workers.delete_worker'

    def post(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError as e:
            related_objects = list(e.protected_objects)
            return render(request, self.error_template_name, {'related_objects': related_objects})
