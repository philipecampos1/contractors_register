from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render
from django.db.models.deletion import ProtectedError
from . import models
from django.urls import reverse_lazy
from . import forms


class StaircaseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Staircase
    template_name = 'staircases/staircase_list.html'
    context_object_name = 'staircases'
    ordering = ['name']
    paginate_by = 10
    login_url = 'account_login'
    permission_required = 'staircases.view_staircase'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class StaircaseDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Staircase
    template_name = 'staircases/staircase_detail.html'
    login_url = 'account_login'
    permission_required = 'staircases.view_staircase'


class StaircaseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Staircase
    template_name = 'staircases/staircase_create.html'
    form_class = forms.StaircaseForm
    success_url = reverse_lazy('staircase_list')
    login_url = 'account_login'
    permission_required = 'staircases.create_staircase'


class StaircaseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Staircase
    template_name = 'staircases/staircase_update.html'
    form_class = forms.StaircaseForm
    success_url = reverse_lazy('staircase_list')
    login_url = 'account_login'
    permission_required = 'staircases.change_staircase'


class StaircaseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Staircase
    template_name = 'staircases/staircase_delete.html'
    error_template_name = 'error/error_delete.html'
    success_url = reverse_lazy('staircase_list')
    login_url = 'account_login'
    permission_required = 'staircases.delete_staircase'

    def post(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError as e:
            related_objects = list(e.protected_objects)
            return render(request, self.error_template_name, {'related_objects': related_objects})
