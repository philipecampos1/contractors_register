from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.db.models.deletion import ProtectedError
from django.shortcuts import render
from django.db.models import Q
from . import models
from . import forms
from django.urls import reverse_lazy


class VisitorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Visitor
    template_name = 'visitors/visitor_list.html'
    context_object_name = 'visitors'
    ordering = ['-created_at']
    paginate_by = 10
    login_url = 'account_login'
    permission_required = 'visitors.view_visitor'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(staircase__name__icontains=search_query)
            )

        return queryset


class VisitorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Visitor
    template_name = 'visitors/visitor_detail.html'
    context_object_name = 'visitor'
    login_url = 'account_login'
    permission_required = 'visitors.view_visitor'


class VisitorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Visitor
    template_name = 'visitors/visitor_create.html'
    form_class = forms.VisitorForm
    success_url = reverse_lazy('visitor_list')
    login_url = 'account_login'
    permission_required = 'visitors.create_visitor'


class VisitorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Visitor
    template_name = 'visitors/visitor_update.html'
    form_class = forms.VisitorForm
    success_url = reverse_lazy('visitor_list')
    login_url = 'account_login'
    permission_required = 'visitors.change_visitor'


class VisitorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Visitor
    template_name = 'visitors/visitor_delete.html'
    error_template_name = 'error/error_delete.html'
    success_url = reverse_lazy('visitor_list')
    login_url = 'account_login'
    permission_required = 'visitors.delete_visitor'

    def post(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError as e:
            related_objects = list(e.protected_objects)
            return render(request, self.error_template_name, {'related_objects': related_objects})
