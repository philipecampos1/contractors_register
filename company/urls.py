from django.urls import path
from . import views

urlpatterns = [
    path('company/list/', views.CompanyListView.as_view(), name='company_list'),
    path('company/create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('company/<int:pk>/update/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('company/<int:pk>/detail/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('company/<int:pk>/delete/', views.CompanyDeleteView.as_view(), name='company_delete'),

]
